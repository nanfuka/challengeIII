from app.views.views import app
from app.db import DatabaseConnection
# from tests.get_token import Token
import unittest
import json


class TestIncidents(unittest.TestCase):
    def setUp(self):
      
        # app.testing = True
        self.test_client = app.test_client()
        self.database = DatabaseConnection()
        self.database.create_users_table()
        self.database.create_incident_tables()
      

        self.user = {"firstname": "grace",
                "lastname": "bantariza",
                "othernames": "bright",
                "email": "grachcfe@gdmail.com",
                "phoneNumber": 1111111111,
                "username": "grvrachce",
                "isAdmin": "true",
                "password": "greatsong"
                }


    def tearDown(self):
        self.database.cursor.execute("DROP TABLE incidents")
        self.database.cursor.execute("DROP TABLE users")
             
        self.database.create_users_table()
        self.database.create_incident_tables()
        


    def test_signup(self):
        response = self.test_client.post('/api/v1/auth/signup', json=self.user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(
        #     data[1]['message'], "you have successfully logged in as a adminstrator")
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['data'][0]['message'], "you have successfully logged in as a adminstrator")
        # token = self.assertEqual(data['data'][0]['token'])

    def test_token(self):
        response = self.test_client.post('/api/v1/auth/signup', json=self.user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(
        #     data[1]['message'], "you have successfully logged in as a adminstrator")
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['data'][0]['message'], "you have successfully logged in as a adminstrator")
        # token = self.assertEqual(data['data'][0]['token'])
        # token = json.loads(data['data'][0]['token'])
      
        # return token

    def get_token(self, username="grvrachce", password="marie"):
        """
        Returns a user token
        """
        response = self.login_user(email, password)
        return json.loads(response.data.decode())['token']

        # self.assertEqual(data['data']['othernames'], "mercy")
        # self.assertEqual(data['data']['username'], "jhku")
        # self.assertEqual(data['data']['phoneNumber'], 1111111111)


    # def test_signup_with_no_firstname(self):
    #     user = {"firstname": " ",
    #             "lastname": "kalungi",
    #             "othernames": "Nsubuga",
    #             "email": "kalungi2k6@yahoo.com",
    #             "PhoneNumber": 777777,
    #             "username": "nanfuka",
    #             "isAdmin": "true",
    #             "password": "secrets"
    #             }
    #     response = self.test_client.post('/api/v1/auth/signup', json=user)
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(data['error'], 'Enter firstname')

    # def test_signup_with_Iinvalid_firstname(self):
    #     user = {"firstname": 4546,
    #             "lastname": "kalungi",
    #             "othernames": "Nsubuga",
    #             "email": "kalungi2k6@yahoo.com",
    #             "PhoneNumber": 777777,
    #             "username": "nanfuka",
    #             "isAdmin": "true",
    #             "password": "secrets"
    #             }
    #     response = self.test_client.post('/api/v1/auth/signup', json=user)
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(data['error'], 'firstname should be a string')

    # def test_signup_with_no_lastname(self):
    #     user = {"firstname": "frae",
    #             "lastname": " ",
    #             "othernames": "Nsubuga",
    #             "email": "kalungi2k6@yahoo.com",
    #             "PhoneNumber": 777777,
    #             "username": "nanfuka",
    #             "isAdmin": "true",
    #             "password": "secrets"
    #             }
    #     response = self.test_client.post('/api/v1/auth/signup', json=user)
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(data['error'], 'Enter lastname')

    # def test_login_with_no_invalid_phonenumber(self):
    #     user = {"firstname": "frae",
    #             "lastname": "fgfdhfg",
    #             "othernames": "Nsubuga",
    #             "email": "kalungi2k6@yahoo.com",
    #             "phoneNumber": "dfgf",
    #             "username": "nanfuka",
    #             "isAdmin": "true",
    #             "password": "secrets"
    #             }
    #     response = self.test_client.post('/api/v1/auth/signup', json=user)
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(data['error'], 'phoneNumber should be made up of numbers')

    # def test_login_with_no_phonenumber(self):
    #     user = {"firstname": "frae",
    #             "lastname": "fgfdhfg",
    #             "othernames": "Nsubuga",
    #             "email": "kalungi2k6@yahoo.com",
                
    #             "username": "nanfuka",
    #             "isAdmin": "true",
    #             "password": "secrets"
    #             }
    #     response = self.test_client.post('/api/v1/auth/signup', json=user)
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(data['error'], 'Enter phone number')

    # def test_signup_with_no_email(self):
    #     user = {"firstname": "frae",
    #             "lastname": "sfdrg",
    #             "othernames": "Nsubuga",
    #             "email": "kampala",
    #             "PhoneNumber": 777777,
    #             "username": "nanfuka",
    #             "isAdmin": "true",
    #             "password": "secrets"
    #             }
    #     response = self.test_client.post('/api/v1/auth/signup', json=user)
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(data['error'], 'Invalid email, it should be in this format; kals@gma.com')

    # def test_signup_with_not_email(self):
    #     user = {"firstname": "frae",
    #             "lastname": "sfdrg",
    #             "othernames": "Nsubuga",
               
    #             "PhoneNumber": 777777,
    #             "username": "nanfuka",
    #             "isAdmin": "true",
    #             "password": "secrets"
    #             }
    #     response = self.test_client.post('/api/v1/auth/signup', json=user)
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(data['error'], 'Enter Email')
    # def test_signup_with_invalid_lastname(self):
    #     user = {"firstname": "4546",
    #             "lastname": 4564,
    #             "othernames": "Nsubuga",
    #             "email": "kalungi2k6@yahoo.com",
    #             "PhoneNumber": 777777,
    #             "username": "nanfuka",
    #             "isAdmin": "true",
    #             "password": "secrets"
    #             }
    #     response = self.test_client.post('/api/v1/auth/signup', json=user)
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(data['error'], 'lastname should be a string')

    # def test_signup_with_invalid_admin_status(self):
    #     user = {"firstname": "frae",
    #             "lastname": "sfdrg",
    #             "othernames": "Nsubuga",
    #             "email": "kampala@yahoo.com",
    #             "phoneNumber": 777777,
    #             "username": "nanfuka",
    #             "isAdmin": "trues",
    #             "password": "secrets"
    #             }
    #     response = self.test_client.post('/api/v1/auth/signup', json=user)
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(data['error'], 'IsAdmin should either be  or False')

    # def test_signup_with_weak_password(self):
    #     user = {"firstname": "frae",
    #             "lastname": "sfdrg",
    #             "othernames": "Nsubuga",
    #             "email": "kampala@yahoo.com",
    #             "phoneNumber": 777777,
    #             "username": "nanfuka",
    #             "isAdmin": "true",
    #             "password": "dfg"
    #             }
    #     response = self.test_client.post('/api/v1/auth/signup', json=user)
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(data['error'], 'Increase the strength of your password')

    # def test_signup_with_no_password(self):
    #     user = {"firstname": "frae",
    #             "lastname": "sfdrg",
    #             "othernames": "Nsubuga",
    #             "email": "kampala@yahoo.com",
    #             "phoneNumber": 777777,
    #             "username": "nanfuka",
    #             "isAdmin": "true",
             
    #             }
    #     response = self.test_client.post('/api/v1/auth/signup', json=user)
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(data['error'], 'Enter password')

    # def test_login(self):
    #     """method for testing the login"""
    #     user = {"firstname": "4546",
    #             "lastname": "4564",
    #             "othernames": "Nsubuga",
    #             "email": "kalungi2k6@yahoo.com",
    #             "PhoneNumber": 777777,
    #             "username": "nanfuka",
    #             "isAdmin": "true",
    #             "password": "secrets"
    #             }
    #     response = self.test_client.post('/api/v1/auth/signup', json=user)
    #     login = {"username": "nanfuka",
    #              "password": "secrets"}
    #     response = self.test_client.post('/api/v1/auth/login', json=login)
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(
    #         data{'message': 'you have logged in successfully',
    #                   'status': 201})

    #     logins = {"username": "nanfuks",
    #               "password": "secres"}
    #     response = self.test_client.post('/api/v1/auth/login', json=logins)
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(
    #         data, {"error": "user with such credentials does not exist",
    #                'status': 404})