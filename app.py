from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from resources.Clientes.views import ClienteView


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(ClienteView, '/cliente')
