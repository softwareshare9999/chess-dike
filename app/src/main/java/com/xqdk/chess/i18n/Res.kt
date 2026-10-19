package com.xqdk.chess.i18n

import android.content.Context
import com.xqdk.chess.ChessApp
import com.xqdk.chess.R

/** Short accessors for localized strings from application context. */
object Res {
    @JvmStatic
    fun ctx(): Context = ChessApp.getContext()

    @JvmStatic
    fun get(id: Int): String = ctx().getString(id)

    @JvmStatic
    fun get(id: Int, vararg args: Any?): String = ctx().getString(id, *args)

    @JvmStatic
    fun enginePrefix(info: String): String = get(R.string.engine_label_prefix, info)
}
