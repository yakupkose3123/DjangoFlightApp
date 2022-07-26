from .base import * #?base.py içineki her şeyi import et


THIRD_PARTY_APPS = [
    "debug_toolbar",   #! For debug-toolbar
]

INSTALLED_APPS += THIRD_PARTY_APPS


THIRD_PARTY_MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",  #! For debug-toolbar
]

MIDDLEWARE += THIRD_PARTY_MIDDLEWARE

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#! For debug-toolbar
INTERNAL_IPS = [
 "127.0.0.1",
]
