import unittest
from app.views.views import app
from app.controllers.user_controllers import User_controller

import json
from app.db import DatabaseConnection 
cont = User_controller()


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        """This method sets up the tests client, \
            connects to the database and sets up the data for signing up
        """
        self.test_client = app.test_client()
        self.db = DatabaseConnection()
        self.user = {"firstname": "deb",
                "lastname":"kalun",
                "othernames":"mercy",
                "email":"ziwa@yahoo.com",
                "phoneNumber":1111111111,
                "username":"morice",
                "isAdmin":"false",
                "password":"popcorn"

                }

    def test_user_register(self):
        """This method tests wether a user can signup with all teh valid data"""
        response = self.test_client.post('/api/v1/signup', json=self.user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            data['message'], "Successfully signedup with ireporter")
        self.assertEqual(data['data']['firstname'], "deb")
        self.assertEqual(data['data']['othernames'], "mercy")
        self.assertEqual(data['data']['username'], "morice")
        self.assertEqual(data['data']['phoneNumber'], 1111111111)



    def tearDown(self):
        """method for dropping the tables \
           so that the data can be reused
        """
        cont.drop_table('users')
if __name__ == "__main__":
    unittest.main()