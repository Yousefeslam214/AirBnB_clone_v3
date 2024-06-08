#!/usr/bin/python3
""" This module uses blueprint to generate views
"""


from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models import storage
from models.state import State


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def get_states():
    """This method gets all instances of state"""
    states_list = storage.all("State")
    all_states = []
    for obj in states_list.values():
        all_states.append(obj.to_dict())
    return jsonify(all_states)


@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def get_states_id(state_id):
    """This method gets all instances of state"""
    state = storage.get("State", state_id)
    if not state:
        abort(404, "Not found")
    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_states_id(state_id):
    """This function delete_state_by_id"""
    state = storage.get("State", state_id)
    if not state:
        abort(404, "Not found")
    storage.delete(state)
    storage.save()
    return jsonify(state.to_dict()), 200


@app_views.route("/states", methods=["POST"], strict_slashes=False)
def post_states():
    """This function creates a new state"""
    new_state = request.get_json()
    if not new_state:
        abort(400, 'Not a JSON')
    if 'name' not in new_state:
        abort(400, 'Missing name')
    state = State(**new_state)
    storage.save
    return make_response(state.to_dict(), 201)


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def put_states(state_id):
    """Updates a State object"""
    state = storage.get("State", state_id)
    if not state:
        abort(404, "Not found")
    new_state = request.get_json()
    if not new_state:
        abort(400, 'Not a JSON')
    if not request.json:
        abort(400, 'Not a JSON')
    for key, value in new_state.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
        state.save()
        storage.save()
    return jsonify(state.to_dict()), 200
