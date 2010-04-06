import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
LOCAL = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Hugo Henriques Maia Vieira', 'hugomaiavieira@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'hugomaiavi'
DATABASE_USER = 'root'
DATABASE_PASSWORD = 'root'
DATABASE_HOST = ''
DATABASE_PORT = ''

TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

USE_I18N = True

try:
    from server_settings import *
except ImportError:
    pass

MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media')

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = 'xqo#aupy_)6+r&((1$!47%@fjzxrc(-m-#e+o4ojk2t=25kk^&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT_PATH, 'templates'),
)

EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = ''
EMAIL_PORT = ''

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.syndication',
    'django.contrib.comments',

    'blog',
    'tags',
)

