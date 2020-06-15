from .models import User


def createUser(**kwargs):
    """
        Save new User in database

        Return:
            [user object]
    """
    user = User(**kwargs)
    user.save()
    return user


def uniqueEmail(email):
    """
        Check if email does not exist

        Returns:
            [bool]
    """
    user = User.query.filter_by(email=email).first()
    if not user:
        return True
    return False


def uniqueName(name):
    """
        Check if a name exist

        Returns:
            [bool]
    """
    user = User.query.filter_by(name=name).first()
    return True if not user else False
