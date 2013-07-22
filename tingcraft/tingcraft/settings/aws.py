from base import *


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
