from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity
from flask_restful import Resource, reqparse
from .controllers import autenticate
from datetime import timedelta

parcer = reqparse.RequestParser()
parcer.add_argument("email", type=str, required=True,
                    help="email is a required parameter")
parcer.add_argument("password", type=str, required=True,
                    help="password is a required parameter")


class ClientAuth(Resource):
    '''
        Auth methods
    '''
    @classmethod
    def post(cls):
        '''
            Login method
        '''
        args = parcer.parse_args()
        user = autenticate(args['email'], args['password'])
        if user.client:
            access_token = create_access_token(
                identity=user.client.id, fresh=True, expires_delta=timedelta(hours=1))
            refresh_token = create_refresh_token(user.client.id)

            return {
                'status': 'success',
                'data': {
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
            }, 200
        return {'status': 'error', 'data': 'Invalid credentials'}, 400


class TokenRefresh(Resource):
    '''
        Refresh JWT token method
    '''
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(
            identity=current_user, fresh=True, expires_delta=timedelta(hours=1))
        refresh_token = create_refresh_token(current_user)
        return {
            'status': 'success',
            'data': {
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        }, 200
