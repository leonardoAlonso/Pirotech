from api.models import db, ma, BaseModel
from marshmallow import fields
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import BOOLEAN

from api.Users.models import UserSchema


class Cliente(BaseModel, db.Model):
    """ Table Clientes """
    __tablename__ = 'clientes'
    user_id = db.Column(db.String(36), ForeignKey('users.id'))
    user = relationship('User', back_populates='client')
    profile_picture = db.Column(db.String(255), nullable=True)
    is_facebook = db.Column(BOOLEAN, default=False)
    is_twitter = db.Column(BOOLEAN, default=False)
    is_google = db.Column(BOOLEAN, default=False)


class ClienteSchema(ma.Schema):
    """ Serializer from Clientes table """
    id = fields.String()
    profile_picture = fields.String(required=True)
    user = fields.Nested(UserSchema)

