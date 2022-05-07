from flask import Flask, request, json, jsonify
from werkzeug.exceptions import HTTPException
from urllib.parse import urlparse
import requests
from . import errors, parser

def create_app() -> Flask:
    app = Flask(__name__)

    @app.route('/reviews', methods=['POST'])
    def get_reviews():
        """ Get review data from business url """
        try:
            url = request.form.get('url')
        except requests.exceptions.RequestException:
            raise errors.URLError('Missing required url parameter in request')

        reviews = parser.ReviewTrackerParser.parse_url(url)

        response = jsonify(reviews)
        response.content_type = 'application/json'
        return response

    @app.errorhandler(HTTPException)
    def handle_exception(error: HTTPException):
        """ Handle app errors and return JSON """
        if isinstance(error, HTTPException):
            response = error.get_response()
            response.data = json.dumps({
                'code': error.code,
                'name': error.name,
                'description': error.description,
            })
            response.content_type = 'application/json'
            return response
        else:
            response = jsonify({
                'code': 500,
                'name': error.__class__.__name__,
                'description': str(error)
            })
            response.status_code = 500
            response.content_type = 'application/json'
            return response
    
    return app
