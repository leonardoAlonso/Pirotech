import uuid
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
ma = Marshmallow()
bc = Bcrypt()

class BaseModel(object):
    id = db.Column(db.String(36), primary_key=True)
    creation_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        db.session.add(self)
        db.session.commit()