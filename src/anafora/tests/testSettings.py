import sys, os
#Django settings for web project.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True
#TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': '',                      # Or path to database file if using sqlite3.
#        'USER': '',                      # Not used with sqlite3.
#        'PASSWORD': '',                  # Not used with sqlite3.
#        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#    }
#}
DATABASES = {'default': {'ENGINE': ''}}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Denver'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URLthat handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
# e.g.  STATIC_ROOT = '/data/home/verbs/student/wech5560/Research/anaforaDevelop/src/main/static'
#STATIC_ROOT = '/data/home/verbs/student/wech5560/Research/anaforaDevelop/src/static'
STATIC_ROOT = ''
#STATIC_ROOT = '/data/home/verbs/student/wech5560/Research/TemporalPreAnnotation/main/StaticFiles'
# e.g.  STATIC_URL = '/static/'
ROOT_URL = ''
STATIC_URL = ROOT_URL + '/static/'

#e.g. ROOT_URL = '/~wech5560/anafora'
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/data/home/verbs/student/wech5560/Research/anaforaDevelop/src/static',
	'/data/home/verbs/student/wech5560/Research/anaforaFileDevelop/testData',
	'/data/home/verbs/student/wech5560/Research/anaforaFileDevelop/anaforaProjectFile',
    )
#    /data/home/verbs/student/wech5560/Research/anaforaDevelop/src/main/static',
#    '/data/home/verbs/student/wech5560/Research/anaforaDevelop/src/main/static/css',
#    '/data/home/verbs/student/wech5560/Research/anaforaDevelop/src/main/static/js',
#    '/data/home/verbs/student/wech5560/Research/anaforaDevelop/src/main/static/image',
#)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '@#FDJVJ(@#sj823R'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': False,
		#'DIRS': [os.path.join(BASE_DIR, 'Templates'), ],
		'DIRS': ["/data/home/verbs/student/wech5560/Research/anaforaDevelop/src/Templates",],
    },
]
# List of callables that know how to import templates from various sources.
"""
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
"""

"""
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)
"""

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Uncomment the next line for Anafora digest auth
#    'anafora.anaforaAuthMiddleware.AnaforaAuthMiddleware',
    'anafora.anaforaAuthMiddleware.AnaforaAuthMiddleware',
    'anafora.tests.testAnaforaAuthMiddleware.TestAnaforaAuthMiddleware',
)

ROOT_URLCONF = 'web.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'web.wsgi.application'

"""
TEMPLATE_DIRS = (
    "/data/home/verbs/student/wech5560/Research/anaforaDevelop/src/Templates",
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
"""

INSTALLED_APPS = (
#    'django.contrib.auth',
#    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.sites',
#    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    #'markFalsePositive',
    #'django_qunit',
    'anafora',
	'anaforaTest',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEST_RUNNER = 'anafora.tests.databaselessTest.DatabaselessTestRunner'

# Assign the anafora project file directory path
# e.g.  ANAFORA_PROJECT_FILE_ROOT = "/data/home/verbs/student/wech5560/Research/KnowtatorProcessing/data/anaforaProjectFile/"
ANAFORA_PROJECT_FILE_ROOT = ""

ANAFORA_AUTH_LDAP = True

# Assign the Digest auth group file location
# e.g.  GROUP_FILE = '/data/anafora-event/site/anafora-event.group'
GROUP_FILE = ''

# Assign the group name for the admin
# e.g.  ADMIN_GROUPNAME = 'anaforaadmin'
ADMIN_GROUPNAME = 'anaforaadmin'

# Assign the setting file in the project directory
# e.g. ANAFORA_PROJECT_SETTING_FILENAME = ".setting.xml"
ANAFORA_PROJECT_SETTING_FILENAME = ".setting.xml"
