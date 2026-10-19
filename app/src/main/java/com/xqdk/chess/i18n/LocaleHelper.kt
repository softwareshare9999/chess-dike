package com.xqdk.chess.i18n

import android.content.Context
import android.content.res.Configuration
import android.os.Build
import java.util.Locale

/**
 * App language: Vietnamese is the default; Chinese (zh) stays available via resources.
 */
object LocaleHelper {
    const val PREFS = "xqdk_locale"
    const val KEY_LANG = "app_language"
    const val LANG_VI = "vi"
    const val LANG_ZH = "zh"

    fun getLanguage(context: Context): String {
        val prefs = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
        return prefs.getString(KEY_LANG, LANG_VI) ?: LANG_VI
    }

    fun setLanguage(context: Context, language: String) {
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
            .edit()
            .putString(KEY_LANG, if (language == LANG_ZH) LANG_ZH else LANG_VI)
            .apply()
    }

    fun wrap(context: Context): Context {
        val lang = getLanguage(context)
        val locale = if (lang == LANG_ZH) Locale.SIMPLIFIED_CHINESE else Locale("vi")
        Locale.setDefault(locale)
        val config = Configuration(context.resources.configuration)
        config.setLocale(locale)
        return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
            context.createConfigurationContext(config)
        } else {
            @Suppress("DEPRECATION")
            context.resources.updateConfiguration(config, context.resources.displayMetrics)
            context
        }
    }

    fun isChinese(context: Context): Boolean = getLanguage(context) == LANG_ZH
}
