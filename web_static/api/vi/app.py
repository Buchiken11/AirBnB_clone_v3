#!/usr/bin/python3

"""
create a handler for 404 errors that returns a JSON-formatted 404
status code response
"""
from flask import jsonify
from flask import Flask
from models import storage
from os import getenv
from api.vi.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_engine(Exception):
    """return a message before running"""
    storage.close()

    @app.error(404)
    def error_page(error):
        """Return the error message response "Not found" if url doesn't exist"""
        reply = {"error": "Not found"}
        return jsonify(reply), 404

    if __name__ == '__main':
        HOST = getenv('HBNB_API_HOST', '0.0.0.')
        PORT = int(getenv('HBNB_API_PORT', 5000))
        app.run(debug=True, host=HOST, port=PORT, threaded=True)