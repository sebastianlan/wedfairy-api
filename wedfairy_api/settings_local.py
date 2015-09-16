LOCAL_SETTINGS = True
from settings import *

DEBUG = True

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'wedfairy_api',
    'USER': 'root',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': '3306',
}
