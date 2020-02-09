from api.models import db, ma, BaseModel
from marshmallow import fields
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import TINYINT


class Market(BaseModel, db.Model):
    """ Table Clientes """
    __tablename__ = 'tianguis'
    latitude = db.Column(db.Numeric(), nullable=False)
    longitude = db.Column(db.Numeric(), nullable=False)
    name = db.Column(db.String(75), nullable=False)
    seller = relationship('Seller', back_populates='market')
    is_active = db.Column(TINYINT(1), default=1)


class MarketSchema(ma.Schema):
    """ Serializer from Clientes table """
    id = fields.String()
    latitude = fields.String(required=True)
    longitude = fields.String(required=True)
    name = fields.String(required=True)

