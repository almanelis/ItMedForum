import os
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4bxol@3=_1gmtp#*1+!lzm1&p+gj=j*$@%9&wy!pxsc-_6ckij'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # css фреймворки
    'tailwind',
    'tailwind_css',
    'django_bootstrap5',    
    # дебагер 
    "debug_toolbar",
    # автоматическое обновление страницы при изменении в шаблоне
    'django_browser_reload',
    # приложения
    'users.apps.UsersConfig',
    'feed.apps.FeedConfig',
    'frontend.apps.FrontendConfig',
    # редактор статей
    'froala_editor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Дебагер
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # Обновление страниц
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'med_it_forum.urls'

TEMPLATES_DIR = BASE_DIR / 'templates'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Настройки tailwind
TAILWIND_APP_NAME = 'tailwind_css'
from shutil import which
NPM_BIN_PATH = which("npm")

WSGI_APPLICATION = 'med_it_forum.wsgi.application'

# Директория для хранения картинок
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Подключаем бэкенд filebased.EmailBackend:
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# Указываем директорию, в которую будут сохраняться файлы писем:
EMAIL_FILE_PATH = BASE_DIR / 'sent_emails' 

AUTH_USER_MODEL = 'users.User'

LOGOUT_REDIRECT_URL = 'feed:list'
# После аутентификации пользователь направляется на главную страницу
LOGIN_REDIRECT_URL = 'feed:list'
LOGIN_URL = 'login' 

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'RU-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
    ]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
INTERNAL_IPS = [
    '127.0.0.1',
]

# froala settiтgs
FROALA_EDITOR_THEME='gray'
FROALA_EDITOR_OPTIONS={
    # 'toolbarInline': True,
    'language': 'ru'
}
FROALA_EDITOR_PLUGINS = ('align', 'char_counter', 'code_beautifier' , 'colors', 'draggable', 'emoticons',
        'entities', 'file', 'font_family', 'font_size', 'image_manager', 'image', 'inline_style',
        'line_breaker', 'link', 'lists', 'paragraph_format', 'paragraph_style', 'quick_insert', 'quote', 'save', 'table',
        'url')
FRAOLA_EDITOR_THIRD_PARTY = ('image_aviary', 'spell_checker')
