from resources.models import db, ma
from marshmallow import fields
from sqlalchemy.dialects.mysql import TINYINT
import uuid


class Cliente(db.Model):
    __tablename__ = 'Clientes'
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_facebook = db.Column(TINYINT(1), default=0)
    is_twitter = db.Column(TINYINT(1), default=0)
    is_google = db.Column(TINYINT(1), default=0)
    profile_picture = db.Column(db.String(255), nullable=True)
    creation_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, **kwargs):
        self.id = uuid.uuid1()
        for key, value in kwargs.items():
            setattr(self, key, value)


class ClienteSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    email = fields.String(required=True)
    profile_picture = fields.String(required=True)

