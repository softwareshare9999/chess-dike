package com.xqdk.chess

import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.Button
import androidx.appcompat.app.AlertDialog
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.xqdk.chess.assist.ui.AssistActivity
import com.xqdk.chess.assist.ui.QiGridDrawable
import com.xqdk.chess.i18n.LocaleAwareActivity
import com.xqdk.chess.i18n.LocaleHelper
import com.xqdk.chess.views.WebviewActivity

class MainActivity : LocaleAwareActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        findViewById<View>(R.id.main).background = QiGridDrawable(this)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        maybeShowDisclaimer()

        findViewById<Button>(R.id.button_play).setOnClickListener {
            startActivity(Intent(this, GameActivity::class.java))
        }
        findViewById<Button>(R.id.button_link).setOnClickListener {
            startActivity(Intent(this, AssistActivity::class.java))
        }
        findViewById<Button>(R.id.button_learn).setOnClickListener {
            startActivity(Intent(this, ManualActivity::class.java))
        }
        findViewById<Button>(R.id.button_help).setOnClickListener {
            val helpFile = if (LocaleHelper.isChinese(this)) "help-zh.html" else "help.html"
            startActivity(Intent(this, WebviewActivity::class.java).apply {
                putExtra("url", "file:///android_asset/$helpFile")
            })
        }
        findViewById<Button>(R.id.button_about).setOnClickListener {
            showAboutDialog()
        }
    }

    private fun maybeShowDisclaimer() {
        AlertDialog.Builder(this)
            .setTitle(R.string.disclaimer_title)
            .setMessage(R.string.disclaimer_body)
            .setCancelable(false)
            .setPositiveButton(R.string.disclaimer_agree) { d, _ -> d.dismiss() }
            .setNegativeButton(R.string.disclaimer_disagree) { _, _ -> finishAffinity() }
            .setNeutralButton(R.string.language) { _, _ -> showLanguageDialog() }
            .show()
    }

    private fun showLanguageDialog() {
        val labels = arrayOf(
            getString(R.string.language_vietnamese),
            getString(R.string.language_chinese),
        )
        val codes = arrayOf(LocaleHelper.LANG_VI, LocaleHelper.LANG_ZH)
        val current = if (LocaleHelper.isChinese(this)) 1 else 0
        AlertDialog.Builder(this)
            .setTitle(R.string.language)
            .setSingleChoiceItems(labels, current) { dialog, which ->
                LocaleHelper.setLanguage(this, codes[which])
                dialog.dismiss()
                recreate()
            }
            .setNegativeButton(R.string.cancel, null)
            .show()
    }

    private fun showAboutDialog() {
        val text = getString(R.string.about_body, BuildConfig.VERSION_NAME) +
            getString(R.string.disclaimer_body) + "\n\n" +
            getString(R.string.credits_body)
        AlertDialog.Builder(this)
            .setTitle(R.string.about_title)
            .setMessage(text)
            .setPositiveButton(R.string.i_know, null)
            .setNeutralButton(R.string.language) { _, _ -> showLanguageDialog() }
            .show()
    }
}
