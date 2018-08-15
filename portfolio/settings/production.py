from .base import *
from .dev import SECRET_KEY
import os

SECRET_KEY = SECRET_KEY

ALLOWED_HOSTS = ['']

DEBUG = False

try:
    from .local import *
except ImportError:
    pass