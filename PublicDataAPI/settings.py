from pathlib import Path
from datetime import timedelta
from decouple import config
import dj_database_url
import os
from corsheaders.defaults import default_headers

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config('SECRET_KEY')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEBUG = config('DEBUG', default=False, cast=bool)

# Get the database URL from environment variable
DATABASE_URL = config('DATABASE_URL')  # Ensure DATABASE_URL is set in .env or environment

DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600, ssl_require=True)
}

#ALLOWED_HOSTS = ['rockae.com', '.rockae.com']
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',  # Required for Swagger
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'apps.contract',
    'apps.public_api',
    'apps.utility',
    'apps.health',
    'drf_spectacular',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'PublicDataAPI.middleware.APIKeyMiddleware',  # Add API Key middleware
]


CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'PublicDataAPI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PublicDataAPI.wsgi.application'

# Add API Key settings
API_KEY_HEADER = 'X-API-KEY'
API_KEY = config('API_KEY', default='your-default-api-key-here').strip('"\'')

# REST framework configuration for API Key authentication
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'EXCEPTION_HANDLER': 'PublicDataAPI.utils.custom_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'message',
}

PRODUCTION_URL = config('PRODUCTION_URL', default='https://default-url.app')
SPECTACULAR_SETTINGS = {
    'TITLE': 'Admin Dashboard API',
    'DESCRIPTION': '''
API documentation for the Admin Dashboard.

Authentication:
- All endpoints require an API key
- Add the API key in the X-API-KEY header
- Example: X-API-KEY: your-api-key-here
''',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'SWAGGER_UI_SETTINGS': {
        'persistAuthorization': True,
        'displayOperationId': True,
    },
    'SERVERS': [
        {'url': PRODUCTION_URL, 'description': 'Production'},
        {'url': 'http://127.0.0.1:8000', 'description': 'Local Development'},
    ],
    'SECURITY': [{"ApiKeyAuth": []}],
    'SECURITY_DEFINITIONS': {
        'ApiKeyAuth': {
            'type': 'apiKey',
            'in': 'header',
            'name': API_KEY_HEADER,
            'description': f'API key must be provided in the {API_KEY_HEADER} header for all requests'
        }
    },
    'SERVE_AUTHENTICATION_CLASSES': [],
    'SERVE_PERMISSIONS_CLASSES': [],
    'SCHEMA_PATH_PREFIX': '/api/'
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




FTP_ALLOW_OVERWRITE = True

CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-API-KEY',
]



# auto-update 2024-10-14T18:00:00
# auto-update 2024-10-14T18:20:00
# auto-update 2024-10-14T18:40:00
# auto-update 2024-10-14T19:00:00
# auto-update 2024-10-14T19:20:00
# auto-update 2024-10-14T19:40:00
# auto-update 2024-10-14T20:00:00
# auto-update 2024-10-14T20:20:00
# auto-update 2024-10-14T20:40:00
# auto-update 2024-10-14T21:00:00
# auto-update 2024-10-14T21:20:00
# auto-update 2024-10-14T21:40:00
# auto-update 2024-10-15T18:00:00
# auto-update 2024-10-15T18:21:49
# auto-update 2024-10-15T18:43:38
# auto-update 2024-10-15T19:05:27
# auto-update 2024-10-15T19:27:16
# auto-update 2024-10-15T19:49:05
# auto-update 2024-10-15T20:10:54
# auto-update 2024-10-15T20:32:43
# auto-update 2024-10-15T20:54:32
# auto-update 2024-10-15T21:16:21
# auto-update 2024-10-15T21:38:10
# auto-update 2024-10-16T18:00:00
# auto-update 2024-10-16T18:34:17
# auto-update 2024-10-16T19:08:34
# auto-update 2024-10-16T19:42:51
# auto-update 2024-10-16T20:17:08
# auto-update 2024-10-16T20:51:25
# auto-update 2024-10-16T21:25:42
# auto-update 2024-10-17T18:00:00
# auto-update 2024-10-17T18:24:00
# auto-update 2024-10-17T18:48:00
# auto-update 2024-10-17T19:12:00
# auto-update 2024-10-17T19:36:00
# auto-update 2024-10-17T20:00:00
# auto-update 2024-10-17T20:24:00
# auto-update 2024-10-17T20:48:00
# auto-update 2024-10-17T21:12:00
# auto-update 2024-10-17T21:36:00
# auto-update 2024-10-22T18:00:00
# auto-update 2024-10-22T18:24:00
# auto-update 2024-10-22T18:48:00
# auto-update 2024-10-22T19:12:00
# auto-update 2024-10-22T19:36:00
# auto-update 2024-10-22T20:00:00
# auto-update 2024-10-22T20:24:00
# auto-update 2024-10-22T20:48:00
# auto-update 2024-10-22T21:12:00
# auto-update 2024-10-22T21:36:00
# auto-update 2024-10-26T09:00:00
# auto-update 2024-10-26T11:00:00
# auto-update 2024-10-26T13:00:00
# auto-update 2024-10-26T15:00:00
# auto-update 2024-10-26T17:00:00
# auto-update 2024-10-26T19:00:00
# auto-update 2024-10-29T18:00:00
# auto-update 2024-10-29T18:34:17
# auto-update 2024-10-29T19:08:34
# auto-update 2024-10-29T19:42:51
# auto-update 2024-10-29T20:17:08
# auto-update 2024-10-29T20:51:25
# auto-update 2024-10-29T21:25:42
# auto-update 2024-11-01T18:00:00
# auto-update 2024-11-01T18:21:49
# auto-update 2024-11-01T18:43:38
# auto-update 2024-11-01T19:05:27
# auto-update 2024-11-01T19:27:16
# auto-update 2024-11-01T19:49:05
# auto-update 2024-11-01T20:10:54
# auto-update 2024-11-01T20:32:43
# auto-update 2024-11-01T20:54:32
# auto-update 2024-11-01T21:16:21
# auto-update 2024-11-01T21:38:10
# auto-update 2024-11-05T18:00:00
# auto-update 2024-11-05T18:21:49
# auto-update 2024-11-05T18:43:38
# auto-update 2024-11-05T19:05:27
# auto-update 2024-11-05T19:27:16
# auto-update 2024-11-05T19:49:05
# auto-update 2024-11-05T20:10:54
# auto-update 2024-11-05T20:32:43
# auto-update 2024-11-05T20:54:32
# auto-update 2024-11-05T21:16:21
# auto-update 2024-11-05T21:38:10
# auto-update 2024-11-08T18:00:00
# auto-update 2024-11-08T18:24:00
# auto-update 2024-11-08T18:48:00
# auto-update 2024-11-08T19:12:00
# auto-update 2024-11-08T19:36:00
# auto-update 2024-11-08T20:00:00
# auto-update 2024-11-08T20:24:00
# auto-update 2024-11-08T20:48:00
# auto-update 2024-11-08T21:12:00
# auto-update 2024-11-08T21:36:00
# auto-update 2024-11-09T09:00:00
# auto-update 2024-11-09T11:00:00
# auto-update 2024-11-09T13:00:00
# auto-update 2024-11-09T15:00:00
# auto-update 2024-11-09T17:00:00
# auto-update 2024-11-09T19:00:00
# auto-update 2024-11-12T18:00:00
# auto-update 2024-11-12T18:20:00
# auto-update 2024-11-12T18:40:00
# auto-update 2024-11-12T19:00:00
# auto-update 2024-11-12T19:20:00
# auto-update 2024-11-12T19:40:00
# auto-update 2024-11-12T20:00:00
# auto-update 2024-11-12T20:20:00
# auto-update 2024-11-12T20:40:00
# auto-update 2024-11-12T21:00:00
# auto-update 2024-11-12T21:20:00
# auto-update 2024-11-12T21:40:00
# auto-update 2024-11-13T18:00:00
# auto-update 2024-11-13T18:34:17
# auto-update 2024-11-13T19:08:34
# auto-update 2024-11-13T19:42:51
# auto-update 2024-11-13T20:17:08
# auto-update 2024-11-13T20:51:25
# auto-update 2024-11-13T21:25:42
# auto-update 2024-11-14T18:00:00
# auto-update 2024-11-14T18:24:00
# auto-update 2024-11-14T18:48:00
# auto-update 2024-11-14T19:12:00
# auto-update 2024-11-14T19:36:00
# auto-update 2024-11-14T20:00:00
# auto-update 2024-11-14T20:24:00
# auto-update 2024-11-14T20:48:00
# auto-update 2024-11-14T21:12:00
# auto-update 2024-11-14T21:36:00
# auto-update 2024-11-20T18:00:00
# auto-update 2024-11-20T18:17:08
# auto-update 2024-11-20T18:34:16
# auto-update 2024-11-20T18:51:24
# auto-update 2024-11-20T19:08:32
# auto-update 2024-11-20T19:25:40
# auto-update 2024-11-20T19:42:48
# auto-update 2024-11-20T19:59:56
# auto-update 2024-11-20T20:17:04
# auto-update 2024-11-20T20:34:12
# auto-update 2024-11-20T20:51:20
# auto-update 2024-11-20T21:08:28
# auto-update 2024-11-20T21:25:36
# auto-update 2024-11-20T21:42:44
# auto-update 2024-11-23T09:00:00
# auto-update 2024-11-23T11:24:00
# auto-update 2024-11-23T13:48:00
# auto-update 2024-11-23T16:12:00
# auto-update 2024-11-23T18:36:00
# auto-update 2024-11-27T18:00:00
# auto-update 2024-11-27T18:17:08
# auto-update 2024-11-27T18:34:16
# auto-update 2024-11-27T18:51:24
# auto-update 2024-11-27T19:08:32
# auto-update 2024-11-27T19:25:40
# auto-update 2024-11-27T19:42:48
# auto-update 2024-11-27T19:59:56
# auto-update 2024-11-27T20:17:04
# auto-update 2024-11-27T20:34:12
# auto-update 2024-11-27T20:51:20
# auto-update 2024-11-27T21:08:28
# auto-update 2024-11-27T21:25:36
# auto-update 2024-11-27T21:42:44
# auto-update 2024-11-30T09:00:00
# auto-update 2024-11-30T09:55:23
# auto-update 2024-11-30T10:50:46
# auto-update 2024-11-30T11:46:09
# auto-update 2024-11-30T12:41:32
# auto-update 2024-11-30T13:36:55
# auto-update 2024-11-30T14:32:18
# auto-update 2024-11-30T15:27:41
# auto-update 2024-11-30T16:23:04
# auto-update 2024-11-30T17:18:27
# auto-update 2024-11-30T18:13:50
# auto-update 2024-11-30T19:09:13
# auto-update 2024-11-30T20:04:36
# auto-update 2024-12-01T09:00:00
# auto-update 2024-12-01T10:05:27
# auto-update 2024-12-01T11:10:54
# auto-update 2024-12-01T12:16:21
# auto-update 2024-12-01T13:21:48
# auto-update 2024-12-01T14:27:15
# auto-update 2024-12-01T15:32:42
# auto-update 2024-12-01T16:38:09
# auto-update 2024-12-01T17:43:36
# auto-update 2024-12-01T18:49:03
# auto-update 2024-12-01T19:54:30
# auto-update 2024-12-04T18:00:00
# auto-update 2024-12-04T18:34:17
# auto-update 2024-12-04T19:08:34
# auto-update 2024-12-04T19:42:51
# auto-update 2024-12-04T20:17:08
# auto-update 2024-12-04T20:51:25
# auto-update 2024-12-04T21:25:42
# auto-update 2024-12-05T18:00:00
# auto-update 2024-12-05T18:34:17
# auto-update 2024-12-05T19:08:34
# auto-update 2024-12-05T19:42:51
# auto-update 2024-12-05T20:17:08
# auto-update 2024-12-05T20:51:25
# auto-update 2024-12-05T21:25:42
# auto-update 2024-12-09T18:00:00
# auto-update 2024-12-09T18:18:27
# auto-update 2024-12-09T18:36:54
# auto-update 2024-12-09T18:55:21
# auto-update 2024-12-09T19:13:48
# auto-update 2024-12-09T19:32:15
# auto-update 2024-12-09T19:50:42
# auto-update 2024-12-09T20:09:09
# auto-update 2024-12-09T20:27:36
# auto-update 2024-12-09T20:46:03
# auto-update 2024-12-09T21:04:30
# auto-update 2024-12-09T21:22:57
# auto-update 2024-12-09T21:41:24
# auto-update 2024-12-10T18:00:00
# auto-update 2024-12-10T18:24:00
# auto-update 2024-12-10T18:48:00
# auto-update 2024-12-10T19:12:00
# auto-update 2024-12-10T19:36:00
# auto-update 2024-12-10T20:00:00
# auto-update 2024-12-10T20:24:00
# auto-update 2024-12-10T20:48:00
# auto-update 2024-12-10T21:12:00
# auto-update 2024-12-10T21:36:00
# auto-update 2024-12-11T18:00:00
# auto-update 2024-12-11T18:26:40
# auto-update 2024-12-11T18:53:20
# auto-update 2024-12-11T19:20:00
# auto-update 2024-12-11T19:46:40
# auto-update 2024-12-11T20:13:20
# auto-update 2024-12-11T20:40:00
# auto-update 2024-12-11T21:06:40
# auto-update 2024-12-11T21:33:20
# auto-update 2024-12-12T18:00:00
# auto-update 2024-12-12T18:24:00
# auto-update 2024-12-12T18:48:00
# auto-update 2024-12-12T19:12:00
# auto-update 2024-12-12T19:36:00
# auto-update 2024-12-12T20:00:00
# auto-update 2024-12-12T20:24:00
# auto-update 2024-12-12T20:48:00
# auto-update 2024-12-12T21:12:00
# auto-update 2024-12-12T21:36:00
# auto-update 2024-12-13T18:00:00
# auto-update 2024-12-13T18:26:40
# auto-update 2024-12-13T18:53:20
# auto-update 2024-12-13T19:20:00
# auto-update 2024-12-13T19:46:40
# auto-update 2024-12-13T20:13:20
# auto-update 2024-12-13T20:40:00
# auto-update 2024-12-13T21:06:40
# auto-update 2024-12-13T21:33:20
# auto-update 2024-12-16T18:00:00
# auto-update 2024-12-16T18:40:00
# auto-update 2024-12-16T19:20:00
# auto-update 2024-12-16T20:00:00
# auto-update 2024-12-16T20:40:00
# auto-update 2024-12-16T21:20:00
# auto-update 2024-12-19T18:00:00
# auto-update 2024-12-19T18:34:17
# auto-update 2024-12-19T19:08:34
# auto-update 2024-12-19T19:42:51
# auto-update 2024-12-19T20:17:08
# auto-update 2024-12-19T20:51:25
# auto-update 2024-12-19T21:25:42
# auto-update 2024-12-20T18:00:00
# auto-update 2024-12-20T18:30:00
# auto-update 2024-12-20T19:00:00
# auto-update 2024-12-20T19:30:00
# auto-update 2024-12-20T20:00:00
# auto-update 2024-12-20T20:30:00
# auto-update 2024-12-20T21:00:00
# auto-update 2024-12-20T21:30:00
# auto-update 2024-12-23T18:00:00
# auto-update 2024-12-23T18:24:00
# auto-update 2024-12-23T18:48:00
# auto-update 2024-12-23T19:12:00
# auto-update 2024-12-23T19:36:00
# auto-update 2024-12-23T20:00:00
# auto-update 2024-12-23T20:24:00
# auto-update 2024-12-23T20:48:00
# auto-update 2024-12-23T21:12:00
# auto-update 2024-12-23T21:36:00
# auto-update 2024-12-25T18:00:00
# auto-update 2024-12-25T18:17:08
# auto-update 2024-12-25T18:34:16
# auto-update 2024-12-25T18:51:24
# auto-update 2024-12-25T19:08:32
# auto-update 2024-12-25T19:25:40
# auto-update 2024-12-25T19:42:48
# auto-update 2024-12-25T19:59:56
# auto-update 2024-12-25T20:17:04
# auto-update 2024-12-25T20:34:12
# auto-update 2024-12-25T20:51:20
# auto-update 2024-12-25T21:08:28
# auto-update 2024-12-25T21:25:36
# auto-update 2024-12-25T21:42:44
# auto-update 2024-12-26T18:00:00
# auto-update 2024-12-26T18:20:00
# auto-update 2024-12-26T18:40:00
# auto-update 2024-12-26T19:00:00
# auto-update 2024-12-26T19:20:00
# auto-update 2024-12-26T19:40:00
# auto-update 2024-12-26T20:00:00
# auto-update 2024-12-26T20:20:00
# auto-update 2024-12-26T20:40:00
# auto-update 2024-12-26T21:00:00
# auto-update 2024-12-26T21:20:00
# auto-update 2024-12-26T21:40:00
# auto-update 2024-12-29T09:00:00
# auto-update 2024-12-29T11:24:00
# auto-update 2024-12-29T13:48:00
# auto-update 2024-12-29T16:12:00
# auto-update 2024-12-29T18:36:00
# auto-update 2024-12-30T18:00:00
# auto-update 2024-12-30T18:40:00
# auto-update 2024-12-30T19:20:00
# auto-update 2024-12-30T20:00:00
# auto-update 2024-12-30T20:40:00
# auto-update 2024-12-30T21:20:00
# auto-update 2025-01-02T18:00:00
# auto-update 2025-01-02T18:30:00
# auto-update 2025-01-02T19:00:00
# auto-update 2025-01-02T19:30:00
# auto-update 2025-01-02T20:00:00
# auto-update 2025-01-02T20:30:00
# auto-update 2025-01-02T21:00:00
# auto-update 2025-01-02T21:30:00
# auto-update 2025-01-10T18:00:00
# auto-update 2025-01-10T18:26:40
# auto-update 2025-01-10T18:53:20
# auto-update 2025-01-10T19:20:00
# auto-update 2025-01-10T19:46:40
# auto-update 2025-01-10T20:13:20
# auto-update 2025-01-10T20:40:00
# auto-update 2025-01-10T21:06:40
# auto-update 2025-01-10T21:33:20
# auto-update 2025-01-11T09:00:00
# auto-update 2025-01-11T09:55:23
# auto-update 2025-01-11T10:50:46
# auto-update 2025-01-11T11:46:09
# auto-update 2025-01-11T12:41:32
# auto-update 2025-01-11T13:36:55
# auto-update 2025-01-11T14:32:18
# auto-update 2025-01-11T15:27:41
# auto-update 2025-01-11T16:23:04
# auto-update 2025-01-11T17:18:27
# auto-update 2025-01-11T18:13:50
# auto-update 2025-01-11T19:09:13
# auto-update 2025-01-11T20:04:36
# auto-update 2025-01-12T09:00:00
# auto-update 2025-01-12T10:00:00
# auto-update 2025-01-12T11:00:00
# auto-update 2025-01-12T12:00:00
# auto-update 2025-01-12T13:00:00
# auto-update 2025-01-12T14:00:00
# auto-update 2025-01-12T15:00:00
# auto-update 2025-01-12T16:00:00
# auto-update 2025-01-12T17:00:00
# auto-update 2025-01-12T18:00:00
# auto-update 2025-01-12T19:00:00
# auto-update 2025-01-12T20:00:00
# auto-update 2025-01-13T18:00:00
# auto-update 2025-01-13T18:48:00
# auto-update 2025-01-13T19:36:00
# auto-update 2025-01-13T20:24:00
# auto-update 2025-01-13T21:12:00
# auto-update 2025-01-14T18:00:00
# auto-update 2025-01-14T18:18:27
# auto-update 2025-01-14T18:36:54
# auto-update 2025-01-14T18:55:21
# auto-update 2025-01-14T19:13:48
# auto-update 2025-01-14T19:32:15
# auto-update 2025-01-14T19:50:42
# auto-update 2025-01-14T20:09:09
# auto-update 2025-01-14T20:27:36
# auto-update 2025-01-14T20:46:03
# auto-update 2025-01-14T21:04:30
# auto-update 2025-01-14T21:22:57
# auto-update 2025-01-14T21:41:24
# auto-update 2025-01-15T18:00:00
# auto-update 2025-01-15T18:20:00
# auto-update 2025-01-15T18:40:00
# auto-update 2025-01-15T19:00:00
# auto-update 2025-01-15T19:20:00
# auto-update 2025-01-15T19:40:00
# auto-update 2025-01-15T20:00:00
# auto-update 2025-01-15T20:20:00
# auto-update 2025-01-15T20:40:00
# auto-update 2025-01-15T21:00:00
# auto-update 2025-01-15T21:20:00
# auto-update 2025-01-15T21:40:00
# auto-update 2025-01-16T18:00:00
# auto-update 2025-01-16T18:48:00
# auto-update 2025-01-16T19:36:00
# auto-update 2025-01-16T20:24:00
# auto-update 2025-01-16T21:12:00
# auto-update 2025-01-19T09:00:00
# auto-update 2025-01-19T11:24:00
# auto-update 2025-01-19T13:48:00
# auto-update 2025-01-19T16:12:00
# auto-update 2025-01-19T18:36:00
# auto-update 2025-01-20T18:00:00
# auto-update 2025-01-20T18:24:00
# auto-update 2025-01-20T18:48:00
# auto-update 2025-01-20T19:12:00
# auto-update 2025-01-20T19:36:00
# auto-update 2025-01-20T20:00:00
# auto-update 2025-01-20T20:24:00
# auto-update 2025-01-20T20:48:00
# auto-update 2025-01-20T21:12:00
# auto-update 2025-01-20T21:36:00
# auto-update 2025-01-22T18:00:00
# auto-update 2025-01-22T18:30:00
# auto-update 2025-01-22T19:00:00
# auto-update 2025-01-22T19:30:00
# auto-update 2025-01-22T20:00:00
# auto-update 2025-01-22T20:30:00
# auto-update 2025-01-22T21:00:00
# auto-update 2025-01-22T21:30:00
# auto-update 2025-01-23T18:00:00
# auto-update 2025-01-23T18:26:40
# auto-update 2025-01-23T18:53:20
# auto-update 2025-01-23T19:20:00
# auto-update 2025-01-23T19:46:40
# auto-update 2025-01-23T20:13:20
# auto-update 2025-01-23T20:40:00
# auto-update 2025-01-23T21:06:40
# auto-update 2025-01-23T21:33:20
# auto-update 2025-01-28T18:00:00
# auto-update 2025-01-28T18:18:27
# auto-update 2025-01-28T18:36:54
# auto-update 2025-01-28T18:55:21
# auto-update 2025-01-28T19:13:48
# auto-update 2025-01-28T19:32:15
# auto-update 2025-01-28T19:50:42
# auto-update 2025-01-28T20:09:09
# auto-update 2025-01-28T20:27:36
# auto-update 2025-01-28T20:46:03
# auto-update 2025-01-28T21:04:30
# auto-update 2025-01-28T21:22:57
# auto-update 2025-01-28T21:41:24
# auto-update 2025-01-30T18:00:00
# auto-update 2025-01-30T18:17:08
# auto-update 2025-01-30T18:34:16
# auto-update 2025-01-30T18:51:24
# auto-update 2025-01-30T19:08:32
# auto-update 2025-01-30T19:25:40
# auto-update 2025-01-30T19:42:48
# auto-update 2025-01-30T19:59:56
# auto-update 2025-01-30T20:17:04
# auto-update 2025-01-30T20:34:12
# auto-update 2025-01-30T20:51:20
# auto-update 2025-01-30T21:08:28
# auto-update 2025-01-30T21:25:36
# auto-update 2025-01-30T21:42:44
# auto-update 2025-02-01T09:00:00
# auto-update 2025-02-01T11:24:00
# auto-update 2025-02-01T13:48:00
# auto-update 2025-02-01T16:12:00
# auto-update 2025-02-01T18:36:00
# auto-update 2025-02-02T09:00:00
# auto-update 2025-02-02T09:55:23
# auto-update 2025-02-02T10:50:46
# auto-update 2025-02-02T11:46:09
# auto-update 2025-02-02T12:41:32
# auto-update 2025-02-02T13:36:55
# auto-update 2025-02-02T14:32:18
# auto-update 2025-02-02T15:27:41
# auto-update 2025-02-02T16:23:04
# auto-update 2025-02-02T17:18:27
# auto-update 2025-02-02T18:13:50
# auto-update 2025-02-02T19:09:13
# auto-update 2025-02-02T20:04:36
# auto-update 2025-02-04T18:00:00
# auto-update 2025-02-04T18:26:40
# auto-update 2025-02-04T18:53:20
# auto-update 2025-02-04T19:20:00
# auto-update 2025-02-04T19:46:40
# auto-update 2025-02-04T20:13:20
# auto-update 2025-02-04T20:40:00
# auto-update 2025-02-04T21:06:40
# auto-update 2025-02-04T21:33:20
# auto-update 2025-02-05T18:00:00
# auto-update 2025-02-05T18:40:00
# auto-update 2025-02-05T19:20:00
# auto-update 2025-02-05T20:00:00
# auto-update 2025-02-05T20:40:00
# auto-update 2025-02-05T21:20:00
# auto-update 2025-02-07T18:00:00
# auto-update 2025-02-07T18:18:27
# auto-update 2025-02-07T18:36:54
# auto-update 2025-02-07T18:55:21
# auto-update 2025-02-07T19:13:48
# auto-update 2025-02-07T19:32:15
# auto-update 2025-02-07T19:50:42
# auto-update 2025-02-07T20:09:09
# auto-update 2025-02-07T20:27:36
# auto-update 2025-02-07T20:46:03
# auto-update 2025-02-07T21:04:30
# auto-update 2025-02-07T21:22:57
# auto-update 2025-02-07T21:41:24
# auto-update 2025-02-08T09:00:00
# auto-update 2025-02-08T11:24:00
# auto-update 2025-02-08T13:48:00
# auto-update 2025-02-08T16:12:00
# auto-update 2025-02-08T18:36:00
# auto-update 2025-02-09T09:00:00
# auto-update 2025-02-09T10:05:27
# auto-update 2025-02-09T11:10:54
# auto-update 2025-02-09T12:16:21
# auto-update 2025-02-09T13:21:48
# auto-update 2025-02-09T14:27:15
# auto-update 2025-02-09T15:32:42
# auto-update 2025-02-09T16:38:09
# auto-update 2025-02-09T17:43:36
# auto-update 2025-02-09T18:49:03
# auto-update 2025-02-09T19:54:30
# auto-update 2025-02-11T18:00:00
# auto-update 2025-02-11T18:21:49
# auto-update 2025-02-11T18:43:38
# auto-update 2025-02-11T19:05:27
# auto-update 2025-02-11T19:27:16
# auto-update 2025-02-11T19:49:05
# auto-update 2025-02-11T20:10:54
# auto-update 2025-02-11T20:32:43
# auto-update 2025-02-11T20:54:32
# auto-update 2025-02-11T21:16:21
# auto-update 2025-02-11T21:38:10
# auto-update 2025-02-12T18:00:00
# auto-update 2025-02-12T18:34:17
# auto-update 2025-02-12T19:08:34
# auto-update 2025-02-12T19:42:51
# auto-update 2025-02-12T20:17:08
# auto-update 2025-02-12T20:51:25
# auto-update 2025-02-12T21:25:42
# auto-update 2025-02-13T18:00:00
# auto-update 2025-02-13T18:20:00
# auto-update 2025-02-13T18:40:00
# auto-update 2025-02-13T19:00:00
# auto-update 2025-02-13T19:20:00
# auto-update 2025-02-13T19:40:00
# auto-update 2025-02-13T20:00:00
# auto-update 2025-02-13T20:20:00
# auto-update 2025-02-13T20:40:00
# auto-update 2025-02-13T21:00:00
# auto-update 2025-02-13T21:20:00
# auto-update 2025-02-13T21:40:00
# auto-update 2025-02-17T18:00:00
# auto-update 2025-02-17T18:17:08
# auto-update 2025-02-17T18:34:16
# auto-update 2025-02-17T18:51:24
# auto-update 2025-02-17T19:08:32
# auto-update 2025-02-17T19:25:40
# auto-update 2025-02-17T19:42:48
# auto-update 2025-02-17T19:59:56
# auto-update 2025-02-17T20:17:04
# auto-update 2025-02-17T20:34:12
# auto-update 2025-02-17T20:51:20
# auto-update 2025-02-17T21:08:28
# auto-update 2025-02-17T21:25:36
# auto-update 2025-02-17T21:42:44
# auto-update 2025-02-21T18:00:00
# auto-update 2025-02-21T18:24:00
# auto-update 2025-02-21T18:48:00
# auto-update 2025-02-21T19:12:00
# auto-update 2025-02-21T19:36:00
# auto-update 2025-02-21T20:00:00
# auto-update 2025-02-21T20:24:00
# auto-update 2025-02-21T20:48:00
# auto-update 2025-02-21T21:12:00
# auto-update 2025-02-21T21:36:00
# auto-update 2025-02-22T09:00:00
# auto-update 2025-02-22T09:55:23
# auto-update 2025-02-22T10:50:46
# auto-update 2025-02-22T11:46:09
# auto-update 2025-02-22T12:41:32
# auto-update 2025-02-22T13:36:55
# auto-update 2025-02-22T14:32:18
# auto-update 2025-02-22T15:27:41
# auto-update 2025-02-22T16:23:04
# auto-update 2025-02-22T17:18:27
# auto-update 2025-02-22T18:13:50
# auto-update 2025-02-22T19:09:13
# auto-update 2025-02-22T20:04:36
# auto-update 2025-02-23T09:00:00
# auto-update 2025-02-23T09:55:23
# auto-update 2025-02-23T10:50:46
# auto-update 2025-02-23T11:46:09
# auto-update 2025-02-23T12:41:32
# auto-update 2025-02-23T13:36:55
# auto-update 2025-02-23T14:32:18
# auto-update 2025-02-23T15:27:41
# auto-update 2025-02-23T16:23:04
# auto-update 2025-02-23T17:18:27
# auto-update 2025-02-23T18:13:50
# auto-update 2025-02-23T19:09:13
# auto-update 2025-02-23T20:04:36
# auto-update 2025-02-24T18:00:00
# auto-update 2025-02-24T18:24:00
# auto-update 2025-02-24T18:48:00
# auto-update 2025-02-24T19:12:00
# auto-update 2025-02-24T19:36:00
# auto-update 2025-02-24T20:00:00
# auto-update 2025-02-24T20:24:00
# auto-update 2025-02-24T20:48:00
# auto-update 2025-02-24T21:12:00
# auto-update 2025-02-24T21:36:00
# auto-update 2025-02-25T18:00:00
# auto-update 2025-02-25T18:26:40
# auto-update 2025-02-25T18:53:20
# auto-update 2025-02-25T19:20:00
# auto-update 2025-02-25T19:46:40
# auto-update 2025-02-25T20:13:20
# auto-update 2025-02-25T20:40:00
# auto-update 2025-02-25T21:06:40
# auto-update 2025-02-25T21:33:20
# auto-update 2025-02-27T18:00:00
# auto-update 2025-02-27T18:17:08
# auto-update 2025-02-27T18:34:16
# auto-update 2025-02-27T18:51:24
# auto-update 2025-02-27T19:08:32
# auto-update 2025-02-27T19:25:40
# auto-update 2025-02-27T19:42:48
# auto-update 2025-02-27T19:59:56
# auto-update 2025-02-27T20:17:04
# auto-update 2025-02-27T20:34:12
# auto-update 2025-02-27T20:51:20
# auto-update 2025-02-27T21:08:28
# auto-update 2025-02-27T21:25:36
# auto-update 2025-02-27T21:42:44
# auto-update 2025-02-28T18:00:00
# auto-update 2025-02-28T18:20:00
# auto-update 2025-02-28T18:40:00
# auto-update 2025-02-28T19:00:00
# auto-update 2025-02-28T19:20:00
# auto-update 2025-02-28T19:40:00
# auto-update 2025-02-28T20:00:00
# auto-update 2025-02-28T20:20:00
# auto-update 2025-02-28T20:40:00
# auto-update 2025-02-28T21:00:00
# auto-update 2025-02-28T21:20:00
# auto-update 2025-02-28T21:40:00
# auto-update 2025-03-03T18:00:00
# auto-update 2025-03-03T18:17:08
# auto-update 2025-03-03T18:34:16
# auto-update 2025-03-03T18:51:24
# auto-update 2025-03-03T19:08:32
# auto-update 2025-03-03T19:25:40
# auto-update 2025-03-03T19:42:48
# auto-update 2025-03-03T19:59:56
# auto-update 2025-03-03T20:17:04
# auto-update 2025-03-03T20:34:12
# auto-update 2025-03-03T20:51:20
# auto-update 2025-03-03T21:08:28
# auto-update 2025-03-03T21:25:36
# auto-update 2025-03-03T21:42:44
# auto-update 2025-03-06T18:00:00
# auto-update 2025-03-06T18:17:08
# auto-update 2025-03-06T18:34:16
# auto-update 2025-03-06T18:51:24
# auto-update 2025-03-06T19:08:32
# auto-update 2025-03-06T19:25:40
# auto-update 2025-03-06T19:42:48
# auto-update 2025-03-06T19:59:56
# auto-update 2025-03-06T20:17:04
