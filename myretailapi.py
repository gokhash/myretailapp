import traceback,logging
from mongoengine import DoesNotExist
from flask_restx import Api

api = Api(version='1.0', title='MyRetail API',
          description='A Flask RestX powered API for MyRetail Products')
log = logging.getLogger(__name__)

@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    print(message)
    return {'message': message}, 500

#@api.errorhandler(DoesNotExist)
#def database_not_found_error_handler(e):
#    """No results found in database"""
#    print(traceback.format_exc())
#    return {'message': 'A database result was required but none was found.'}, 404

