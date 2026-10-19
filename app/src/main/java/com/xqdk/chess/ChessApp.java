package com.xqdk.chess;

import android.app.Application;
import android.content.Context;

import com.xqdk.chess.i18n.LocaleHelper;

public class ChessApp extends Application {
    private static Context appContext;

    /** Get the application context (locale-wrapped). */
    public static Context getContext() {
        return appContext;
    }

    @Override
    protected void attachBaseContext(Context base) {
        super.attachBaseContext(LocaleHelper.INSTANCE.wrap(base));
    }

    @Override
    public void onCreate() {
        super.onCreate();
        appContext = this;
    }
}
