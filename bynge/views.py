from bynge import app
from bynge.blueprints import storage, stream, edit

# Attach blueprints.
app.register_blueprint(storage.blueprint, url_prefix='/v1/storage')
app.register_blueprint(stream.blueprint, url_prefix='/v1/stream')
app.register_blueprint(edit.blueprint, url_prefix='/v1/edit')