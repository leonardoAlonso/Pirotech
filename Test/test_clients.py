import unittest
from api import create_app
from api.models import db
from api.config import TestingConfig
from faker import Faker

fake = Faker()

base_url = "/api/v1/clientes"


class ClientsTest(unittest.TestCase):
    """
        Test cases from Clients View
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

    def getClientsList(self):
        return self.client.get(base_url)

    def createClientSuccess(self):
        sent = {'email': fake.email(), 'name': fake.name(), 'password': "12345678"}
        print(sent)
        with self.client as client:
            return client.post(base_url, data=sent)

    def createClientErrorPassword(self):
        sent = {"email": "leonardoalonsososa@gmail.com",
                "name": "Leonardo Alonso", "password": "1234567"}
        with self.client as client:
            return client.post(base_url, data=sent)

    def testList(self):
        response = self.getClientsList()
        self.assertEqual(response.status_code, 200)

    def testAdd(self):
        response = self.createClientSuccess()
        self.assertEqual(response.status_code, 201)
    
    def testAddFailPassword(self):
        response = self.createClientErrorPassword()
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
