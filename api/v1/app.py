#!/usr/bin/python3
""" This module prepare flask blueprint
"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def shutdown_session(exception=None):
    """ fun """
    storage.close()



if __name__ == "__main__":
    host = getenv("HBNB_API_HOST")
    port = getenv("HBNB_API_PORT")
    if host is None:
        host = "0.0.0.0"
    if port is None:
        port = 5000
    app.run(host=host, port=port, threaded=True)
