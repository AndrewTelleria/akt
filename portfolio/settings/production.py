from .base import *
from decouple import config
import os

DEBUG = False

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['35.160.36.100', 'aktelleria.com', 'www.aktelleria.com']

try:
    from .local import *
except ImportError:
    pass
