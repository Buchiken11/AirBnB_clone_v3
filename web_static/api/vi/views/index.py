#!/usr/bin/python3

"""
an endpoint that retrieves the number of each objects by type
"""
from models import storage
from flask import jsonify
from api.vi.views import app_views

@app_veiws.route('/status')
def api_status_code():
    """
    Return a json response for Restful api
    """
    reply = {'status': "OK"}
    return jsonify(reply)

@app_views.route('stats')
def get_stats():
    """
    Gets the status code of url with flask api
    """
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('Cities'),
        'places': storage.count('Place'),
        'reveiws': storage.count('Reveiws'),
        'states': storage.count('States'),
        'users': storage.count('Users'),
    }
    return jsonify(stats)