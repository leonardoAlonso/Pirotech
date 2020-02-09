from api.models import db, ma, BaseModel
from marshmallow import fields
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import TINYINT


class Seller(BaseModel, db.Model):
    """ Table Clientes """
    __tablename__ = 'vendedores'
    local_number = db.Column(db.Integer(), nullable=True)
    local_name = db.Column(db.String(100), nullable=True)
    market_id = db.Column(db.String(36), ForeignKey('users.id'))
    market = relationship('Market', back_populates='seller')


class SellerSchema(ma.Schema):
    """ Serializer from Clientes table """
    id = fields.String()
    local_number = fields.String(required=True)
    local_name = fields.String(required=True)

