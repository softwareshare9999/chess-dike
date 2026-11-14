package com.xqdk.chess

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.widget.Button
import android.widget.LinearLayout
import com.xqdk.chess.i18n.LocaleAwareActivity
import com.xqdk.chess.i18n.LocaleHelper
import com.xqdk.chess.i18n.MoveNotation

/**
 * 开局分流落地页（2026-11-09 用户拍板，参照象棋鱼 MainActivity 模式）：启动后按
 * "学习模式 / 连线模式"分流，帮助/关于入口与检查更新（2026-11-10 自连线页上移，
 * 版本页脚）都在本页。
 * 免责弹窗随 launcher 语义一并迁入：每次冷启动必弹（savedInstanceState 守卫=
 * 配置重建走恢复路径不重弹；isTaskRoot 守卫=singleTask 复用/通知唤起不重弹），
 * 弹窗在屏时旋转由 onResume 补弹兜底（体检 P1 旁路缺口语义原样保留）。
 *
 * 本 fork 的本地化改造（上游原文全为硬编码中文 + 无语言入口）：
 * - 继承 LocaleAwareActivity：落地页是新的 launcher，若不接语言包装，用户切到
 *   越南语后进 App 第一屏仍是中文，等于本地化整体失效；
 * - 全部 UI 文案走字符串资源（values/ 越南语默认、values-zh-rCN/ 中文）；
 * - 语言选择入口随帮助/关于一并迁入本页（原在连线页，连线页已不再是入口）；
 * - 检查更新失败按 UpdateFailure 取本地化文案（上游写法用 result.message，
 *   而 fork 的网络层只回类型、文案留在 UI 层，直接搬会编译不过）。
 */
class LauncherActivity : LocaleAwareActivity() {

    companion object {
        /** 免责同意态的 savedInstanceState 键（仅跨配置重建传递，不持久化——冷启动必重弹） */
        private const val KEY_DISCLAIMER_AGREED = "disclaimer_agreed"
    }

    /** 免责同意态（仅本实例内存，经 savedInstanceState 跨配置重建） */
    private var disclaimerAgreed = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_launcher)

        // 每次应用启动必弹；savedInstanceState/isTaskRoot 双守卫语义从连线页原样迁入
        if (savedInstanceState == null && isTaskRoot()) {
            maybeShowDisclaimer()
        } else {
            disclaimerAgreed = savedInstanceState?.getBoolean(KEY_DISCLAIMER_AGREED, false) ?: false
            if (!disclaimerAgreed) maybeShowDisclaimer()
        }

        findViewById<LinearLayout>(R.id.card_learn).setOnClickListener {
            startActivity(Intent(this, com.xqdk.chess.learn.LearnActivity::class.java))
        }
        findViewById<LinearLayout>(R.id.card_assist).setOnClickListener {
            startActivity(Intent(this, com.xqdk.chess.assist.ui.AssistActivity::class.java))
        }

        findViewById<Button>(R.id.button_help).setOnClickListener {
            // 帮助页按当前语言选资源（越南语 help.html / 中文 help-zh.html）
            val helpAsset = if (LocaleHelper.isChinese(this)) "help-zh.html" else "help.html"
            val intent = Intent(this, com.xqdk.chess.views.WebviewActivity::class.java).apply {
                putExtra("url", "file:///android_asset/$helpAsset")
            }
            startActivity(intent)
        }
        findViewById<Button>(R.id.button_about).setOnClickListener { showAboutDialog() }
        findViewById<Button>(R.id.button_language).setOnClickListener { showLanguageDialog() }

        // 版本页脚：versionName 含构建元数据（describe 推导），构建日期是检查更新的比较口径
        findViewById<android.widget.TextView>(R.id.tv_version_footer).text =
            getString(R.string.version_footer, BuildConfig.VERSION_NAME, BuildConfig.BUILD_DATE)
        setupUpdateCheck()
    }

    /**
     * 检查更新：仅手动触发（不主动检查是产品拍板），自连线页上移（2026-11-10 用户
     * 拍板"移动到首页"）。查询走独立线程（AppUpdateChecker.check 为网络 IO，3s 超时），
     * 结果回主线程弹窗/Toast；按钮检查期间禁用防重复点击。失败如实提示——
     * api.github.com 在中国大陆通常需可访问 GitHub 的网络环境
     */
    private fun setupUpdateCheck() {
        val btnUpdate = findViewById<Button>(R.id.btn_check_update)
        btnUpdate.setOnClickListener {
            btnUpdate.isEnabled = false
            btnUpdate.text = getString(R.string.update_checking)
            val checker = com.xqdk.chess.assist.AppUpdateChecker(BuildConfig.BUILD_DATE)
            // 一次性线程（查询完毕自然回收，不留滞留池）
            Thread {
                val result = checker.check()
                runOnUiThread {
                    btnUpdate.isEnabled = true
                    btnUpdate.text = getString(R.string.update_check_button)
                    when (result) {
                        is com.xqdk.chess.assist.UpdateResult.UpToDate ->
                            android.widget.Toast.makeText(this,
                                getString(R.string.update_up_to_date, BuildConfig.BUILD_DATE),
                                android.widget.Toast.LENGTH_SHORT).show()
                        is com.xqdk.chess.assist.UpdateResult.Newer ->
                            androidx.appcompat.app.AlertDialog.Builder(this)
                                .setTitle(getString(R.string.update_found_title, result.tag))
                                .setMessage(
                                    getString(R.string.update_found_message,
                                        result.date, BuildConfig.BUILD_DATE)
                                )
                                .setPositiveButton(getString(R.string.update_open_page)) { _, _ ->
                                    runCatching {
                                        startActivity(
                                            Intent(Intent.ACTION_VIEW, Uri.parse(
                                                com.xqdk.chess.assist.AppUpdateChecker.RELEASES_PAGE))
                                        )
                                    }
                                }
                                .setNegativeButton(getString(R.string.cancel), null)
                                .show()
                        is com.xqdk.chess.assist.UpdateResult.Failure ->
                            android.widget.Toast.makeText(this, updateFailureText(result.reason),
                                android.widget.Toast.LENGTH_LONG).show()
                    }
                }
            }.start()
        }
    }

    /** 更新查询失败原因 → 本地化文案（网络层只回类型，文案留在 UI 层） */
    private fun updateFailureText(reason: com.xqdk.chess.assist.UpdateFailure): String =
        getString(
            when (reason) {
                com.xqdk.chess.assist.UpdateFailure.TIMEOUT -> R.string.update_fail_timeout
                com.xqdk.chess.assist.UpdateFailure.RATE_LIMIT -> R.string.update_fail_rate_limit
                com.xqdk.chess.assist.UpdateFailure.NOT_FOUND -> R.string.update_fail_not_found
                com.xqdk.chess.assist.UpdateFailure.UNREACHABLE -> R.string.update_fail_unreachable
                com.xqdk.chess.assist.UpdateFailure.NO_RELEASE -> R.string.update_fail_no_release
                com.xqdk.chess.assist.UpdateFailure.OTHER -> R.string.update_fail_other
            }
        )

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        outState.putBoolean(KEY_DISCLAIMER_AGREED, disclaimerAgreed)
    }

    /**
     * 免责声明弹窗：每次启动必弹（无可跳过、无持久化跳过），明确"仅供学习研究、
     * 禁止用于对局平台"等使用边界；同意后进入落地页，不同意直接退出应用。
     */
    private fun maybeShowDisclaimer() {
        androidx.appcompat.app.AlertDialog.Builder(this)
            .setTitle(R.string.disclaimer_title)
            .setMessage(getString(R.string.disclaimer_body))
            .setCancelable(false)
            .setPositiveButton(R.string.disclaimer_agree) { d, _ ->
                disclaimerAgreed = true
                d.dismiss()
            }
            .setNegativeButton(R.string.disclaimer_disagree) { _, _ ->
                finishAffinity()
            }
            .show()
    }

    /** 关于：本地对话框（特色功能 + 免责声明 + 鸣谢），不依赖外部站点 */
    private fun showAboutDialog() {
        val text = getString(R.string.about_body, BuildConfig.VERSION_NAME) +
            "\n" + getString(R.string.disclaimer_body) + "\n\n" +
            getString(R.string.credits_body)
        androidx.appcompat.app.AlertDialog.Builder(this)
            .setTitle(R.string.about_title)
            .setIcon(R.drawable.ic_launcher)
            .setMessage(text)
            .setPositiveButton(R.string.i_know, null)
            .show()
    }

    /** 语言切换：持久化后重建 Activity（落地页是 launcher，重建即生效） */
    private fun showLanguageDialog() {
        val options = arrayOf(
            getString(R.string.language_vietnamese),
            getString(R.string.language_chinese),
        )
        val current = if (LocaleHelper.isChinese(this)) 1 else 0
        androidx.appcompat.app.AlertDialog.Builder(this)
            .setTitle(R.string.language)
            .setSingleChoiceItems(options, current) { d, which ->
                d.dismiss()
                val target = if (which == 1) LocaleHelper.LANG_ZH else LocaleHelper.LANG_VI
                if (target == LocaleHelper.getLanguage(this)) return@setSingleChoiceItems
                LocaleHelper.setLanguage(this, target)
                MoveNotation.install()
                // 重建任务栈：服务与悬浮窗仍在跑，仅界面换语言
                recreate()
            }
            .setNegativeButton(R.string.cancel, null)
            .show()
    }
}
