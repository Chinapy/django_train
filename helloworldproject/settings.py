from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
""" BASE_DIR ：　プロジェクトにおける「基準」となる場所を示すために使われる"""
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
"""プロジェクト毎に重複しないように作成される暗号のようなもの
ユーザのパスワードのsalt(ユーザが入力したパスワードの先頭に加える文字列、
パスワード強化のために用いられる)
"""
SECRET_KEY = 'django-insecure-&d9z*0^7u#s*=)mhhvgdi0j-^8nefp^3r-zpluwci^7-&4l=4&'

# SECURITY WARNING: don't run with debug turned on in production!
""" プロジェクトが開発中か本番環境かをDjangoに示すために用いられる """
DEBUG = True
""" 外部からのアクセスを受けるサーバーを指定する際に用いられる"""
ALLOWED_HOSTS = []


# Application definition
""" インストールされているアプリを示している
※ここでのアプリとは、完成されたシステムとしてのアプリケーションWebサイトのこと
 """
INSTALLED_APPS = [
    # あらかじめDjangoが用意しているアプリ
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Django内部でrequestとresponseが受け渡される間に行われる処理機能が記載されている
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ブラウザからrequestが送られた際、最初にそのrequestを受け取るファイルを指定している
# デフォルトでは、プロジェクトのurls.pyファイルが指定されている
ROOT_URLCONF = 'helloworldproject.urls'
# htmlファイルなどのテンプレートを入れる場所を示すために用いられる
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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
# wsgi を実行させる関数が記載されている。
WSGI_APPLICATION = 'helloworldproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
"""パスワード強度を高めるための設定が書かれている
例：minimumlengthvalidatorは最小の文字数の制限をかける機能
"""
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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
