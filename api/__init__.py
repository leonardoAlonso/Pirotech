from flask import Flask
from flask import Blueprint
from flask_restful import Api
from flask_jwt_extended import JWTManager
from api.models import db
from api.Clientes.views import ClientesView, ClienteView
from api.Auth.views import ClientAuth, TokenRefresh

api_bp = Blueprint('api', __name__)

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    jwt = JWTManager(app)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app

api = Api(api_bp)

# Route
api.add_resource(ClientAuth, '/clientes/auth')
api.add_resource(TokenRefresh, '/clientes/refresh')
api.add_resource(ClientesView, '/clientes')
api.add_resource(ClienteView, '/clientes/<client_id>')