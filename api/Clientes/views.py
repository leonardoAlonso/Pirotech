from api.models import db, bc
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import Cliente, ClienteSchema
from .controllers import createClient
from api.Users.controllers import *

clients_schema = ClienteSchema(many=True)
client_schema = ClienteSchema()


parcer = reqparse.RequestParser()
parcer.add_argument("name", type=str, required=True,
                    help="name is a required parameter")
parcer.add_argument("email", type=str, required=True,
                    help="email is a required parameter")
parcer.add_argument("password", type=str, required=True,
                    help="password is a required parameter")

parcer_update = reqparse.RequestParser()
parcer_update.add_argument("profile_picture", type=str)
parcer_update.add_argument("name", type=str)
parcer_update.add_argument("password", type=str)


class ClientesView(Resource):
    """
        Clientes view
        Create new client
        Get a list of clients
    """
    @classmethod
    def get(cls):
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
        if uniqueEmail(args['email']) and uniqueName(args['name']):
            try:
                user_args = {
                    'name': args['name'],
                    'email': args['email'],
                    'password': args['password']
                }
                user = createUser(**user_args)
            except Exception as e:
                print(str(e))
                return {'status': 'error', 'data': str(e)}, 400
            try:
                client_args = {
                    'user_id': user.id,
                }
                client = createClient(**client_args)
                client_result = client_schema.dump(client).data
            except Exception as e:
                return {'status': 'error', 'data': str(e)}, 400
            return {
                'status': 'success',
                'data': {
                    'client': client_result
                }
            }, 201
        else:
            return {'status': 'error', 'data': 'Not unique'}, 400


class ClienteView(Resource):
    '''
        Get, Update and Delete a client
    '''
    @classmethod
    @jwt_required
    def get(cls, client_id):
        '''
            Get client by id
        '''
        identity = get_jwt_identity()
        if identity != client_id:
            return {'status': 'error', 'data': 'Identity error'}, 400
        client = Cliente.query.filter_by(id=identity).first()
        user = client.user
        if client:
            client_result = client_schema.dump(client).data
            return {
                'status': 'success',
                'data': {
                    'client': client_result
                }}, 200
        else:
            return {'status': 'error', 'data': 'Client does not exist'}, 404

    @classmethod
    @jwt_required
    def put(cls, client_id):
        '''
            Update client by id
        '''
        args = parcer_update.parse_args()
        identity = get_jwt_identity()
        if identity != client_id:
            return {'status': 'error', 'data': 'Identity error'}, 400
        client = Cliente.query.filter_by(id=identity).first()
        if client:
            if not args:
                return {'status': 'error', 'data': 'Args empty'}, 400
            if args['name']:
                if uniqueName(args['name']):
                    client.user.name = args['name']
                else:
                    return {'status': 'error', 'data': 'Username invalid'}
            if args['password']:
                if len(args['password']) > 8:
                    args['password'] = bc.generate_password_hash(
                        args['password'])
                    client.user.password = args['password']
                else:
                    return {'status': 'error', 'data': 'Password is not valid'}, 400
            db.session.commit()
            client_result = client_schema.dump(client).data
            return {
                'status': 'success',
                'data': {
                    'client': client_result
                }
            }, 200
