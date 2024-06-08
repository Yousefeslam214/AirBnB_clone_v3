#!/usr/bin/python3
""" This module uses blueprint to generate views
"""


from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models import storage
from models.state import State
from models.city import City


@app_views.route("/states/<state_id>/cities", methods=["GET"], strict_slashes=False)
def get_city(state_id):
    """Retrieves the list of all City """
    state = storage.get("State", state_id)
    if not state:
        abort(404, "Not found")
    return jsonify([city.to_dict() for city in state.cities])
    # states_list = storage.all("City")
    # all_states = []
    # for obj in states_list.values():
    #     all_states.append(obj.to_dict())
    # return jsonify(all_states)


@app_views.route("/cities/<city_id>", methods=["GET"], strict_slashes=False)
def get_city_id(city_id):
    """Retrieves a City"""
    city = storage.get("City", city_id)
    if not city:
        abort(404, "Not found")
    return jsonify(city.to_dict())


@app_views.route("/cities/<city_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_city_id(city_id):
    """Deletes a City object"""
    city = storage.get("City", city_id)
    if not city:
        abort(404, "Not found")
    storage.delete(city)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route("/states/<state_id>/cities", methods=["POST"], strict_slashes=False)
def post_city():
    """Creates a City"""
    new_city = request.get_json()
    if not new_city:
        abort(400, 'Not a JSON')
    if 'name' not in new_city:
        abort(400, 'Missing name')
    city = City(**new_city)
    storage.save
    return make_response(city.to_dict(), 201)


@app_views.route("/cities/<city_id>", methods=["PUT"], strict_slashes=False)
def put_city(city_id):
    """Updates a City object"""
    city = storage.get("City", city_id)
    if not city:
        abort(404, "Not found")
    new_city = request.get_json()
    if not new_city:
        abort(400, 'Not a JSON')
    for key, value in new_city.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(city, key, value)
    storage.save()
    return make_response(jsonify(city.to_dict()), 200)

if __name__ == '__main__':
    pass
# curl -X GET http://0.0.0.0:5000/api/v1/states/421a55f4-7d82-47d9-b54c-a76916479545/cities
