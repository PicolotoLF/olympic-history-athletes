import dj_database_url

from .base import *


SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

DATABASES = {'default': dj_database_url.config(conn_max_age=600)}