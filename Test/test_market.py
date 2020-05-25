import unittest
from api import create_app
from api.config import TestingConfig
from api.models import db
from faker import Faker

fake = Faker()

base_url = '/api/v1/markets'

class MarketsTest(unittest.TestCase):
    """
        Test cases from Markets views
    """
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
    
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
    
    def createMarketSuccess(self):
        data = {'name': fake.name(), 'latitude': float(fake.latitude()), 'longitude': float(fake.longitude())}
        with self.client as client:
            return client.post(base_url, data=data)

    def testAdd(self):
        response = self.createMarketSuccess()
        self.assertEqual(response.status_code, 201)
