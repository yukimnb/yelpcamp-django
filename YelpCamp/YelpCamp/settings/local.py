"""開発環境用の設定ファイル"""

from .base import *

DEBUG = True
ALLOWED_HOSTS = []

# ロギング設定
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    # フォーマッタ定義
    "formatters": {
        "dev": {
            "format": " {asctime} {name}:[{levelname}]\n{message}",
            "style": "{",
        },
    },
    # ハンドラ定義
    "handlers": {
        # コンソール出力用
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "dev",
        },
    },
    # ロガー定義
    "loggers": {
        # Djangoが出力するログ全般を扱うロガー
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
        # 自作アプリが出力するログを扱うロガー
        "campgrounds": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
        # 発行されるSQLを出力するロガー
        # "django.db.backends": {
        #     "handlers": ["console"],
        #     "level": "DEBUG",
        # },
    },
}


# django-debug-toolbar設定
def show_toobar(request):
    return True


INSTALLED_APPS += ("debug_toolbar",)
MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toobar,
}
