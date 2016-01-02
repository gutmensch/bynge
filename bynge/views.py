from bynge import app
from bynge.blueprints import store, play, edit

# Attach blueprints.
app.register_blueprint(store.blueprint, url_prefix='/v1/store')
app.register_blueprint(play.blueprint, url_prefix='/v1/play')
app.register_blueprint(edit.blueprint, url_prefix='/v1/edit')