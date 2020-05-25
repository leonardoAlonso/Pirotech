from api.models import db, ma, BaseModel
from marshmallow import fields
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BOOLEAN

class Market(BaseModel, db.Model):
    """ Table Markets"""
    __tablename__ = 'markets'
    name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float(), nullable=False)
    longitude = db.Column(db.Float(), nullable=False)
    is_active = db.Column(BOOLEAN, default=False)

class MarketSchema(ma.Schema):
    """ Serializer from Markets table """
    id = fields.String(required=True)
    name = fields.String(required=True)
    latitude = fields.Float()
    longitude = fields.Float()