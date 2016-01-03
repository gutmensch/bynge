import os
from bynge.models import IncomingFile
from uuid import uuid4
from flask import Blueprint
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from datetime import datetime

UPLOAD_DIRECTORY = '/Users/jazz/playground/incoming'
ALLOWED_EXTENSIONS = { 'mp3', 'm4a', 'flac' }

app = Flask(__name__)
app.config['UPLOAD_DIRECTORY'] = UPLOAD_DIRECTORY

blueprint = Blueprint(__name__, __name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def incoming_filename(filename):
    file = "%s_%s" % (uuid4(), secure_filename(filename))
    return os.path.join(app.config['UPLOAD_DIRECTORY'], file)


@blueprint.route('', methods=['PUT'])
def store_file():
    os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)
    file = request.files['file']
    if file and allowed_file(file.filename):
        file.save(incoming_filename(file.filename))
        #IncomingFile.init()
        incoming_file = IncomingFile(meta={'id': 1}, file_path='Hello world!', uuid='1', store_date=datetime.now())
        incoming_file.save()
        return render_template('storage.html'), 200
    return render_template('error.html'), 406
