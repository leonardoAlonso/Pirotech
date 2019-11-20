from api.models import db
from .models import Cliente, ClienteSchema

def uniqueEmail(email):
    client = Cliente.query.filter_by(email=email).first()
    if not client:
        return True
    return False
def uniqueName(name):
    client = Cliente.query.filter_by(name=name).first()
    if not client:
        return True
    return False