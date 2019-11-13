from resources.models import db

from flask_restful import Resource
from .models import Clientes, ClienteSchema

clients_schema = ClienteSchema(many=True)
client_schema = ClienteSchema()

class ClienteView(Resource):
    def get(self):
        clients = Clientes.query.all()
        clients = clients_schema.dump(clients)
        return {'status': 'success', 'data': clients}, 200
    
    def post(self):
        return {"message": "Hello, World!"}