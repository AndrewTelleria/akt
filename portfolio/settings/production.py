from .base import *
import os

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['portfolio-env.6sduwvv6gr.us-west-2.elasticbeanstalk.com']

DEBUG = True

try:
    from .local import *
except ImportError:
    pass
