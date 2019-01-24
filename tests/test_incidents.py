from app.views.views import app
from app.db import DatabaseConnection
from tests.get_token import Token
import unittest
import json


class TestIncidents(unittest.TestCase):
    def setUp(self):
      
        # app.testing = True
        self.test_client = app.test_client()
        self.database = DatabaseConnection()
        self.database.create_users_table()
        self.database.create_incident_tables()
      

        self.report = {"createdby": 1,

                       "location": "22.98 33.25",
                       "status": "draft",
                       "images": "imagelocation",
                       "videos": "videolocation",
                       "comment": "this is over recurring",
                       "incident_type": "redflag"
                       }



    def tearDown(self):
        self.database.cursor.execute("DROP TABLE incidents")
        self.database.cursor.execute("DROP TABLE users")
        self.tester = None

    def test_index(self):
        """Method for testing the index route"""
        response = self.test_client.get('/')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "hi welcome to the ireporter")
        self.assertEqual(data['status'], 200)

    def test_create_incident(self):
        """tests if an intervention can be created """
        response = self.test_client.post('/api/v1/auth/intervention', data=self.report)
        self.assertEqual(200, response.status_code)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['data'][0]['id'], 1)
        self.assertEqual(data['data'][0]['message'], “Created an intervention record”)

    def test_get_intervention(self):
        response = self.test_client.post('/api/v1/auth/intervention)
        self.assertEqual(200, response.status_code)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['data'][0]['id'], 1)
        self.assertEqual(data['data'][0]['message'], “Created an intervention record”)








        

if __name__ == ('__main__'):
    unittest.main()




