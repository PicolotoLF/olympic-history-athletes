from .base import *


SECRET_KEY = "development"

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'mydb.db'),
    }
}
#
# # TODO
# os.environ.setdefault()
# os.environ.setdefault()