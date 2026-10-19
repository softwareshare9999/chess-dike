package com.xqdk.chess.i18n

import android.content.Context
import androidx.appcompat.app.AppCompatActivity

/** Applies the persisted app language (Vietnamese default) to every activity. */
open class LocaleAwareActivity : AppCompatActivity() {
    override fun attachBaseContext(newBase: Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }
}
