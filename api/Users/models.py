from api.models import db, ma, BaseModel
from marshmallow import fields
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT

class User(BaseModel, db.Model):
    """ Table Users """
    __tablename__ = 'users'
    name = db.Column(db.String(100), nullable=False)
    client = relationship('Cliente', uselist=False, back_populates='user')
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_active = db.Column(TINYINT(1), default=1 )


class UserSchema(ma.Schema):
    """ Serializer from Users table """
    name = fields.String(required=True)
    email = fields.String(required=True)