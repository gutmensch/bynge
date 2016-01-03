from flask import Flask
from bynge.models import IncomingFile

app = Flask(__name__)

# init indices on ES
IncomingFile.init()

import bynge.views