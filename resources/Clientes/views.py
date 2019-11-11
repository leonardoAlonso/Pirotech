from flask_restful import Resource
from .model import Cliente, ClienteSchema

clients_schema = ClienteSchema(many=True)
client_schema = ClienteSchema()

class Cliente(Resource):
    def get(self):
        clients = Cliente.query.all()
        clients = clients_schema.dump(clients)
        return {'status': 'success', 'data': clients}, 200
    
    def post(self):
        return {"message": "Hello, World!"}