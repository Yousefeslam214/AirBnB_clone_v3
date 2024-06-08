#!/usr/bin/python3
""" This module uses blueprint to generate views
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route("/status", strict_slashes=False)
def status():
    """Return the status of the application"""
    text = {"status": "OK"}
    return jsonify(text)
