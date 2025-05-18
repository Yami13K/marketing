import os
from datetime import timedelta
from decouple import config, Csv
from pathlib import Path


# ========================
# Base Project Directory
# ========================
# Set the BASE_DIR to the parent directory of the current file.
BASE_DIR = Path(__file__).resolve().parent.parent

# ========================
# Environment Configuration
# ========================
# Use the `PHASE` environment variable to differentiate between environments like dev, staging, or production.
PHASE = config("PHASE", default="dev")

# ========================
# Static Files Configuration
# ========================
# Define the URL and root for static files (e.g., CSS, JavaScript, images).
STATIC_URL = "/marketing/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")

# ========================
# Secret Key Configuration
# ========================
# WARNING: Keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# ========================
# Security Settings
# ========================
# Trust the X-Forwarded-Host header (usually used when deploying behind proxies or load balancers).
USE_X_FORWARDED_HOST = True

# Append a slash to URLs if not provided by default.
APPEND_SLASH = True

# Debugging should be turned off in production for security and performance reasons.
DEBUG = config("DEBUG", default=False, cast=bool)

# ========================
# Installed Apps
# ========================
# List of all installed Django apps and third-party libraries that provide additional functionality.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django_extensions",  # Django extensions like shell-plus
    "rest_framework",  # REST API support
    "rest_framework.authtoken",  # Token-based authentication for DRF
    "rest_framework_simplejwt",  # JWT support
    "rest_framework_simplejwt.token_blacklist",  # For token blacklisting
    "corsheaders",  # For enabling Cross-Origin Resource Sharing (CORS)
    "drf_spectacular",  # Automatic API documentation generation
]

# ========================
# CORS Configuration
# ========================
# Define allowed origins for Cross-Origin Resource Sharing (CORS).
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
]

# Allow credentials (cookies, HTTP authentication) to be sent with cross-origin requests.
CORS_ALLOW_CREDENTIALS = True

# ========================
# Spectacular API Settings (for DRF Spectacular)
# ========================
# Configure the OpenAPI schema settings for API documentation generation.
SPECTACULAR_SETTINGS = {
    "COMPONENT_SPLIT_REQUEST": True,
    "TITLE": "marketing",
}

# ========================
# REST Framework Settings
# ========================
# Customize the default behavior of the Django REST Framework (DRF).
REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ],
    "DATE_INPUT_FORMATS": ["%d-%m-%Y", "%d,%B,%Y"],
    "DATE_FORMAT": "%d,%B,%Y",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "ALLOWED_VERSIONS": ["1.0.0", "1.0.1"],
    "DEFAULT_VERSION": "1.0.0",
    "VERSION_PARAM": "version",
}

# ========================
# JWT (JSON Web Token) Authentication
# ========================
# Configure JWT authentication settings.
SIMPLE_JWT = {
    "SIGNING_KEY": config("SECRET_KEY"),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=14),
    "SLIDING_TOKEN_LIFETIME": timedelta(days=14),
    "SLIDING_TOKEN_REFRESH_LIFETIME_GRACE_PERIOD": timedelta(seconds=1),
    "ID_TOKEN_ALLOW_REUSE": False,
    "BLACKLIST_AFTER_ROTATION": True,
}

# ========================
# Middleware Configuration
# ========================
# List of middleware components to handle various aspects of the request/response lifecycle.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ========================
# URL Configuration
# ========================
# Set the root URL configuration for the project.
ROOT_URLCONF = 'marketing.urls'

# ========================
# Container Name for Deployment (e.g., Docker)
# ========================
# Define the container name used in deployments (e.g., for Docker).
CONTAINER_NAME = "marketing"

# ========================
# Allowed Hosts Configuration
# ========================
# Define allowed hostnames or IPs that can access this Django application.
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="localhost", cast=Csv()) + [CONTAINER_NAME]

# ========================
# CSRF Configuration
# ========================
# Define trusted origins for CSRF (Cross-Site Request Forgery) protection.
CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]
for host in ALLOWED_HOSTS:
    CSRF_TRUSTED_ORIGINS.extend([f"http://{host}:81", f"https://{host}:81"])

# ========================
# Template Settings
# ========================
# Configure templates for rendering HTML responses.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ========================
# WSGI Application Configuration
# ========================
# Specify the WSGI application for serving the project.
WSGI_APPLICATION = 'marketing.wsgi.application'

# ========================
# Database Configuration
# ========================
# Define database connection settings for PostgreSQL.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": config("DB_HOST"),
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASS"),
    }
}

# ========================
# Password Validation
# ========================
# Enable password validation to improve security.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ========================
# Internationalization (I18N) and Timezone (TZ) Settings
# ========================
# Set the language and timezone for the application.
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True  # Enable internationalization support
USE_TZ = True  # Enable timezone-aware datetimes

# ========================
# Media and Static Files Configuration
# ========================
# Media files (uploaded by users)
HOST = config("HOST", default="localhost")
PORT = config("PORT", default=80)
MEDIA_URL = f"http://{HOST}:{PORT}/"

# Static files (CSS, JavaScript, images)
STATIC_URL = 'static/'

# ========================
# Default Auto Field Setting
# ========================
# Automatically use BigAutoField for primary keys on models.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ========================
# Celery Configuration
# ========================
# Configure Celery to use Redis as the broker and result backend.
CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = "redis://redis:6379/0"
