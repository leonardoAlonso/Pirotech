from api.models import bc
from api.Clientes.models import Cliente


def autenticate(user, password):
    ''' Authenticate a user

        Parameters:
            user (str): email of user
            password (str): the password of user

        Returns:
            object(Client)
    '''
    client = Cliente.query.filter_by(email=user).first()
    try:
        if client and bc.check_password_hash(client.password, password):
            return client
        return False
    except:
        return False
