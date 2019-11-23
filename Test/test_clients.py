import unittest
from api import create_app
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
        self.test_client = self.app.test_client()

    def tearDown(self):
        pass

    def getClientsList(self):
        return self.test_client.get(base_url)

    def createClientSuccess(self):
        sent = {'email': fake.email(), 'name': fake.name(), 'password': "12345678"}
        with self.test_client as client:
            return client.post(base_url, data=sent)

    def createClientErrorEmail(self):
        sent = {'email': "sbishop@lopez.org",
                'name': "Leonardo Alonso", 'password': "12345678"}
        with self.test_client as client:
            return client.post(base_url, data=sent)

    def createClientErrorName(self):
        sent = {'email': "leonardoalonsososa@gmail.com",
                'name': "Yesenia Davis", 'password': "12345678"}
        with self.test_client as client:
            return client.post(base_url, data=sent)

    def createClientErrorPassword(self):
        sent = {"email": "leonardoalonsososa@gmail.com",
                "name": "Leonardo Alonso", "password": "1234567"}
        with self.test_client as client:
            return client.post(base_url, data=sent)

    def testList(self):
        response = self.getClientsList()
        self.assertEqual(response.status_code, 200)

    def testAdd(self):
        response = self.createClientSuccess()
        self.assertEqual(response.status_code, 201)

    def testAddFailEmail(self):
        response = self.createClientErrorEmail()
        self.assertEqual(response.status_code, 400)

    def testAddFailName(self):
        response = self.createClientErrorName()
        self.assertEqual(response.status_code, 400)
    
    def testAddFailPassword(self):
        response = self.createClientErrorPassword()
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
