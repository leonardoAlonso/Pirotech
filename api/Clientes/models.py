from api.models import db, ma, BaseModel
from marshmallow import fields
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import TINYINT

from api.Users.models import UserSchema


class Cliente(BaseModel, db.Model):
    """ Table Clientes """
    __tablename__ = 'clientes'
    user_id = db.Column(db.String(36), ForeignKey('users.id'))
    user = relationship('User', back_populates='client')
    profile_picture = db.Column(db.String(255), nullable=True)
    is_facebook = db.Column(TINYINT(1), default=0)
    is_twitter = db.Column(TINYINT(1), default=0)
    is_google = db.Column(TINYINT(1), default=0)


class ClienteSchema(ma.Schema):
    """ Serializer from Clientes table """
    id = fields.String()
    profile_picture = fields.String(required=True)
    user = fields.Nested(UserSchema)

