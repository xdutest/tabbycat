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
# Static Files
# ==============================================================================

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


# ==============================================================================
# Caching
# ==============================================================================

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://tc-redis:10000",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 5,
            "SOCKET_TIMEOUT": 60,
            "IGNORE_EXCEPTIONS": True, # Don't crash on say ConnectionError due to limits
        },
    },
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis://tc-redis", 10000)],
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
