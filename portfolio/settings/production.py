from .base import *
import os

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['portfolio-env.pam4nmw3wm.us-west-2.elasticbeanstalk.com']

DEBUG = False

try:
    from .local import *
except ImportError:
    pass





[program:akt]
command = /home/ubuntu/gunicorn_start.bash
user = ubuntu
stdout_logfile = /home/ubuntu/logs/gunicorn_supervisor.log
redirect_stderr = true
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8