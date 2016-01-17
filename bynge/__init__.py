from flask import Flask
import os
import logging
from logging.handlers import RotatingFileHandler
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl.index import Index
from bynge.models import IncomingFile, AudioFile, ApiUser
from sys import exit


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


# init ES index and document type mappings
try:
    connections.create_connection(hosts=[app.config['ELASTIC_URL']])
    #Index(name='bynge').delete()
    if not Index(name='bynge').exists():
        Index(name='bynge').settings(number_of_shards=1, number_of_replicas=0).create()
    IncomingFile.init()
    AudioFile.init()
    ApiUser.init()
except:
    app.logger.error("could not initialize elasticsearch, aborting")
    exit(1)


import bynge.views