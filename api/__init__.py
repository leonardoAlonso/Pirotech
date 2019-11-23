from flask import Flask
from flask import Blueprint
from flask_restful import Api
from api.models import db
from api.Clientes.views import ClientesView

api_bp = Blueprint('api', __name__)

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app

api = Api(api_bp)

# Route
api.add_resource(ClientesView, '/clientes')
