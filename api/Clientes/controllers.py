from .models import Cliente

def createClient(**kwargs):
    """
        Add new client
    """
    client = Cliente(**kwargs)
    client.save()
    return client
