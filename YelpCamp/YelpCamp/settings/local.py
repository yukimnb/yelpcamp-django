"""開発環境用の設定ファイル"""

from .base import *

DEBUG = True
ALLOWED_HOSTS = []

# ロギング設定


def show_toobar(request):
    return True


INSTALLED_APPS += ("debug_toolbar",)
MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toobar,
}
