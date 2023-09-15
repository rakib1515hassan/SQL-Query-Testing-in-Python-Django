import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/




# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-(t+=9d^lc)=w!!e*fkg@c+q$&g94(m(^86=2r+@ua-*(kpw+al'
SECRET_KEY = config('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = config('DEBUG', default=False, cast=bool)





ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Basic_Query',
    'Query_Time',




    'django.contrib.humanize', # For Show Time and Date field in HTML template

    # 'tinymce',           ## For Tiny Text Editor
    'ckeditor',            ## For CKEditor Text Editor
    'ckeditor_uploader',   ## For CKEditor Text Editor
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'Core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "testsqldb",      # Database name
        # "USER": "rakib",        # Username
        "USER": "root",           # Username
        # "PASSWORD": "123456ra", # user Password
        "PASSWORD": "",           # user Password
        # "HOST": "127.0.0.1",
        "HOST": "localhost",
        "PORT": "3306",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/



# STATIC_URL = 'static/'
# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [STATIC_DIR, ]

# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")



STATIC_URL = 'static/'
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')


MEDIA_URL = '/Ck_Items/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/Ck_Items')




# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


## NOTE For CKEditor----------------------------------------------------------------

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        # 'height': 300,
        # 'width': 300,

        'removePlugins':'exportpdf',  # এই Proparty ব্যবহার করে, আপনি কিছু Plagin বন্ধ করতে পারেন যা সম্পাদনা সংক্রান্ত 
                                      # স্পেসিফিক ফিচার যোগ করে। "exportpdf" নামের Plagin বন্ধ করার ফলে, ব্যবহারকারীরা
                                      #  ক্রমান্বয়ে PDF ডকুমেন্ট তৈরি করতে পারবেন না এবং এই Plagin এর সম্পর্কিত কোনো বিশেষ
                                      #  সম্প্রদায়ের সমর্থন থাকবে না।

        
        'extraPlugins': ','.join(
            [
                'codesnippet',    ## For Code snippet added with your CkEditors
                'widget',

                'html5video',     ## For HTML5 video added with your CkEditors
                'youtube',        ## For YouTube video added with your CkEditors     
                
            ]
        ),       
    },
}
