from __future__ import absolute_import, unicode_literals
from .base import *
import os
import environ


env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env(os.path.join(BASE_DIR, './.env'))

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

WHITENOISE_USE_FINDERS = True
WHITENOISE_MANIFEST_STRICT = False
WHITENOISE_ALLOW_ALL_ORIGINS = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

try:
    from .local import *
except ImportError:
    pass
