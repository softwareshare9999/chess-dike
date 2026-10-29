package com.xqdk.chess;

import android.app.Application;
import android.content.Context;
import android.content.res.Configuration;

import com.xqdk.chess.i18n.LocaleHelper;
import com.xqdk.chess.i18n.MoveNotation;

public class ChessApp extends Application {
    private static Context appContext;

    /**
     * Get the application context. Locale-wrapped so that code running outside an
     * Activity (the foreground service, overlay panel, notification channel) resolves
     * strings in the user-selected app language rather than the system default.
     */
    public static Context getContext() {
        return appContext;
    }

    public ChessApp() {
        appContext = this;
    }

    @Override
    protected void attachBaseContext(Context base) {
        super.attachBaseContext(LocaleHelper.INSTANCE.wrap(base));
        appContext = this;
    }

    @Override
    public void onCreate() {
        super.onCreate();
        // Notation words (平/进/退, file numerals) follow the app language;
        // board glyphs stay Chinese.
        MoveNotation.install();
    }

    @Override
    public void onConfigurationChanged(Configuration newConfig) {
        super.onConfigurationChanged(newConfig);
        // Keep the wrapper's base context in step with app language changes.
        appContext = LocaleHelper.INSTANCE.wrap(getBaseContext());
        MoveNotation.install();
    }
}
