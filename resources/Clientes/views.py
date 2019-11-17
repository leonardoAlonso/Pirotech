from resources.models import db, bc
from flask_restful import Resource, reqparse
from .models import Cliente, ClienteSchema


clients_schema = ClienteSchema(many=True)
client_schema = ClienteSchema()

parcer = reqparse.RequestParser()
parcer.add_argument("name", type=str, required=True,
                    help="name is a required parameter")
parcer.add_argument("email", type=str, required=True,
                    help="email is a required parameter")
parcer.add_argument("password", type=str, required=True,
                    help="password is a required parameter")


class ClienteView(Resource):
    @classmethod
    def get(cls ):
        '''
        Get a list of all clientes
        '''
        clients = Cliente.query.all()
        clients = clients_schema.dump(clients).data
        return {'status': 'success', 'data': clients}, 200

    @classmethod
    def post(cls):
        '''
        Add new client to database
        '''
        args = parcer.parse_args()
        args['password'] = bc.generate_password_hash(args['password'])
        client = Cliente(**args)
        try:
            db.session.add(client)
            db.session.commit()
            result = client_schema.dump(client).data
            return {'status':'success', 'data':result}, 201
        except Exception as e:
            return {'status':'error', 'data':str(e)}, 400
