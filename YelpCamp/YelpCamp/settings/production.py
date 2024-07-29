"""本番環境用の設定ファイル"""

from dotenv import load_dotenv

from .base import *

load_dotenv()

DEBUG = False
ALLOWED_HOSTS = [os.environ.get("DJANGO_ALLOWED_HOSTS")]
# ALLOWED_HOSTS = ["*"]


NGINX_DIR = Path("/usr/share/nginx/html")
STATIC_ROOT = NGINX_DIR / "static"
MEDIA_ROOT = NGINX_DIR / "media"

# ロギング設定
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    # フォーマッタ定義
    "formatters": {
        "prod": {
            "format": " {asctime} {name}:[{levelname}]\n{message}",
            "style": "{",
        },
    },
    # ハンドラ定義
    "handlers": {
        # コンソール出力用
        "file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": BASE_DIR / "logs/django.log",
            "formatter": "prod",
            "when": "D",
            "interval": 1,
            "backupCount": 7,
        },
    },
    # ロガー定義
    "loggers": {
        # Djangoが出力するログ全般を扱うロガー
        "django": {
            "handlers": ["file"],
            "level": "INFO",
        },
        # 自作アプリが出力するログを扱うロガー
        "campgrounds": {
            "handlers": ["file"],
            "level": "INFO",
        },
    },
}

# CORS設定
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = ["https://yelpcamp-react.vercel.app/"]
