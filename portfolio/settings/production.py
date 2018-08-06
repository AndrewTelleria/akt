from .base import *
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['portfolio-env.qkwxmxpt4x.us-west-2.elasticbeanstalk.com']

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
