from api.models import db, bc
from flask_restful import Resource, reqparse
from .models import Cliente, ClienteSchema
from .controller import uniqueEmail, uniqueName

clients_schema = ClienteSchema(many=True)
client_schema = ClienteSchema()

parcer = reqparse.RequestParser()
parcer.add_argument("name", type=str, required=True,
                    help="name is a required parameter")
parcer.add_argument("email", type=str, required=True,
                    help="email is a required parameter")
parcer.add_argument("password", type=str, required=True,
                    help="password is a required parameter")


class ClientesView(Resource):
    """ 
        Clientes view
        Create new client
        Get a list of clients
    """
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
        if len(args['password']) < 8:
            return {'status': 'error', 'data': 'Password len error'}, 400
        args['password'] = bc.generate_password_hash(args['password'])
        email = args['email']
        name = args['name']
        if uniqueEmail(args['email']) and uniqueName(args['name']):
            client = Cliente(**args)
            try:
                db.session.add(client)
                db.session.commit()
                result = client_schema.dump(client).data
                return {'status':'success', 'data':result}, 201
            except Exception as e:
                return {'status':'error', 'data':str(e)}, 400
        else:
            return {'status': 'error', 'data': 'Not unique'}, 400