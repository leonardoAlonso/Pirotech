import unittest
from api import create_app
from api.config import TestingConfig

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
    
    def testList(self):
        response = self.getClientsList()
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()