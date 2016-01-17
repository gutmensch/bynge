import os
from datetime import datetime
from uuid import uuid4

import gevent
from flask import Blueprint
from flask import request, render_template, copy_current_request_context
from werkzeug.utils import secure_filename

from bynge.lib.processor.audio import AudioFileProcessor
from bynge.models import IncomingFile
from bynge import app


blueprint = Blueprint(__name__, __name__)
uuid = str(uuid4())


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


def incoming_filename(filename):
    file = "%s_%s" % (uuid, secure_filename(filename))
    return os.path.join(app.config['UPLOAD_DIRECTORY'], file)


@blueprint.route('', methods=['PUT'])
def store_file():
    os.makedirs(app.config['UPLOAD_DIRECTORY'], exist_ok=True)
    file = request.files['file']
    if file and allowed_file(file.filename):
        file_dest_path = incoming_filename(file.filename)
        file.save(file_dest_path)
        incoming_file = IncomingFile(processed='false', file_path=file_dest_path, uuid=uuid, store_date=datetime.now())
        incoming_file.save()
        # processing file in a background thread
        @copy_current_request_context
        def process_file():
            uploaded_file = AudioFileProcessor(uuid)
            uploaded_file.process()
        gevent.spawn(process_file)
        return render_template('storage.html'), 200
    return render_template('error.html'), 406
