import logging
from flask import Flask
from flask_cors import CORS, cross_origin
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from flask import make_response
from flask import request 
from flask import jsonify

from routes import declare_api_routes
from services.data_provider_service import DbConnectService
from services.data_provider_service import session_scope 
from dao.middleware import load_initial_data

# Enable logging to troubleshoot CORS issue
logging.getLogger('flask_cors').level = logging.DEBUG

# engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

app = Flask(__name__)
CORS(app, resources=r'/api/*', supports_credentials=True)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/test/task', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        print('Abort')
    print(request['title'])
    return '1'

declare_api_routes(app)
DbConnectService()

# initialize database
load_initial_data()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
