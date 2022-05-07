from werkzeug.exceptions import HTTPException

class URLError(HTTPException):
    code = 400
    name = 'URLError'

class ReviewsError(HTTPException):
    code = 404
    name = 'Missing Review Error'

class ParameterError(HTTPException):
    code = 404
    name = 'Missing Parameter Error'