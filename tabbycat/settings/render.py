import os
import dj_database_url


# ==============================================================================
# Render per https://render.com/docs/deploy-django
# ==============================================================================

if os.environ.get('DJANGO_SECRET_KEY'):
    SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# ==============================================================================
# User Sessions
# ==============================================================================

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'


# ==============================================================================
# Static Files
# ==============================================================================

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


# ==============================================================================
# Caching
# ==============================================================================

REDIS_URL = 'redis://127.0.0.1:6379/1'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 5,
            "SOCKET_TIMEOUT": 60,
        },
    },
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": REDIS_URL,
            # Remove channels from groups after 3 hours
            # This matches websocket_timeout in Daphne
            "group_expiry": 10800,
        },
    },
}


# ==============================================================================
# Postgres
# ==============================================================================

# Parse database configuration from $DATABASE_URL
DATABASES = {
    'default': dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default='postgresql://postgres:postgres@localhost:5432/tabbycat',
        conn_max_age=600
    )
}
