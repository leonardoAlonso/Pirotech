from app import db, ma
from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_sqlalchemy import SQLAlchemy


class Cliente(db.Model):
    pass

class ClienteSchema(ma.Schema):
    pass