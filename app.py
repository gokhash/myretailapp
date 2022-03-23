import os
import logging.config
from flask import Flask
from database.db import initialize_db
from flask_restx import Api,Resource,reqparse,fields
from resources.routes import initialize_routes
from myretailapi import api

app = Flask(__name__)
#api = Api(app)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://myretail_mongodb/MY_RETAIL'
}

log.info('>>>>> Starting development server')

initialize_db(app)

initialize_routes(api)
api.init_app(app)
app.run(host='0.0.0.0',debug=True)
