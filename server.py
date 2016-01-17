from gevent.wsgi import WSGIServer
from bynge import app

if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
