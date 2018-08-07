from .base import *
import os

SECRET_KEY = os.getenv('SECRET_KEY', 'SECRET_KEY')

ALLOWED_HOSTS = ['portfolio-env.6sduwvv6gr.us-west-2.elasticbeanstalk.com']

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
