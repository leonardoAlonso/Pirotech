from api.models import bc
from api.Users.models import User

def autenticate(user, password):
    ''' Authenticate a user

        Parameters:
            user (str): email of user
            password (str): the password of user

        Returns:
            object(Client)
    '''
    client = User.query.filter_by(email=user).first()
    try:
        if client and bc.check_password_hash(client.password, password):
            return client
        return False
    except:
        return False
