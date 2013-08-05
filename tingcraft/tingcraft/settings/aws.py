from base import *

DEBUG = False
ALLOWED_HOSTS = ['.liyiting.net']

AWS_ACCESS_KEY_ID = 'AKIAIS4JPQBNHQAHBWIA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_S3_SECURE_URLS = False
AWS_S3_CUSTOM_DOMAIN = 's3-singapore.liyiting.net'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 's3-singapore.liyiting.net'

AWS_STATIC_S3_CUSTOM_DOMAIN = 'assets.liyiting.net'
AWS_STATIC_STORAGE_BUCKET_NAME = 'assets.liyiting.net'
AWS_STATIC_PATH = 'assets'

STATIC_URL = 'http://%s/%s/' % (AWS_STATIC_S3_CUSTOM_DOMAIN, AWS_STATIC_PATH)
DEFAULT_AVATAR_LOCATION = STATIC_URL + 'img/avatar/'

STATICFILES_STORAGE = 'core.s3storage.S3PipelineStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # To create one in MySQL: CREATE DATABASE tingcraft CHARACTER SET utf8 COLLATE utf8_unicode_ci;
        'NAME': 'mysite',                    # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'yitingvvv',
        'HOST': 'mysql.cvqkihah2kll.ap-southeast-1.rds.amazonaws.com',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    }
}
