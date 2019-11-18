import os
import unittest
import flask

from api.models import db
from api.Clientes.views import ClientesView
from ...run import app

TEST_DB = "test.db"

class Base(unittest.TestCase):
   """ Class base to unittesting """ 

   
    
    def __init__(self):
        self.setUp()
