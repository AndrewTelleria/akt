from .base import *
from .dev import SECRET_KEY
import os

SECRET_KEY = SECRET_KEY

ALLOWED_HOSTS = ['35.160.36.100', 'aktelleria.com', 'www.aktelleria.com']
# ALLOWED_HOSTS = ['*']

DEBUG = True

try:
    from .local import *
except ImportError:
    pass
