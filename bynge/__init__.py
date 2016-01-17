from flask import Flask
import os
import logging
from logging.handlers import RotatingFileHandler
from bynge.models import IncomingFile, AudioFile, ApiUser

app = Flask(__name__)


# configuration
try:
    app.config.from_object('bynge.default_settings')
except RuntimeError:
    app.logger.error('could not load default configuration')

if os.environ.get('BYNGE_SETTINGS') is not None:
    app.config.from_envvar('BYNGE_SETTINGS')


# logging
logfile_handler = RotatingFileHandler("{0}/{1}.log".format(app.config['LOG_DIR'], app.name), maxBytes=100000, backupCount=1)
logfile_handler.setLevel(eval("logging.{0}".format(app.config['LOG_LEVEL'])))
logfile_handler.setFormatter(logging.Formatter(app.config['LOG_FORMAT']))
app.logger.addHandler(logfile_handler)


# init ES index and needed models
IncomingFile.init()
AudioFile.init()
ApiUser.init()


import bynge.views