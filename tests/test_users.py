
from tests import BaseTestCase
import json

class TestUsers(BaseTestCase):

    def test_signup_with_no_firstname(self):
        """tests whether the signup function will return an expecte error\
            upon signing up without a first name
        """
        user = {"firstname": " ",
                "lastname": "kalungis",
                "othernames": "Nsubuga",
                "email": "kalungi2k6@yahooo.com",
                "PhoneNumber": 777777,
                "username": "nanfukas",
                "isAdmin": "true",
                "password": "secretsd"
                }
        response = self.test_client.post('/api/v1/signup', json=user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Enter firstname')

    def test_signup_with_Iinvalid_firstname(self):
        """tests whether the signup function will return an expecte error\
            upon signing up with an invalid first name
        """
        user = {"firstname": 4546,
                "lastname": "kalungi",
                "othernames": "Nsubuga",
                "email": "kalungi2k6@yahoo.com",
                "PhoneNumber": 777777,
                "username": "nanfuka",
                "isAdmin": "true",
                "password": "secrets"
                }
        response = self.test_client.post('/api/v1/signup', json=user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'firstname should be a string')

    def test_signup_with_no_lastname(self):
        """tests whether the signup function will return an expecte error\
            upon signing up without a lastname
        """
        user = {"firstname": "frae",
                "lastname": " ",
                "othernames": "Nsubuga",
                "email": "kalungi2k6@yahoo.com",
                "PhoneNumber": 777777,
                "username": "nanfuka",
                "isAdmin": "true",
                "password": "secrets"
                }
        response = self.test_client.post('/api/v1/signup', json=user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Enter lastname')

    def test_signup_with_invalid_email(self):
        """tests whether the signup function will return an expecte error\
            upon signing up with an ivalid email
        """
        user = {"firstname": "frae",
                "lastname": "sfdrg",
                "othernames": "Nsubuga",
                "email": "kampala",
                "PhoneNumber": 777777,
                "username": "nanfuka",
                "isAdmin": "true",
                "password": "secrets"
                }
        response = self.test_client.post('/api/v1/signup', json=user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid email, it should be in this format; kals@gma.com')

    def test_signup_with_not_email(self):
        """tests whether the signup function will return an expecte error\
            upon signing up without an email
        """
        user = {"firstname": "frae",
                "lastname": "sfdrg",
                "othernames": "Nsubuga",
               
                "PhoneNumber": 777777,
                "username": "nanfuka",
                "isAdmin": "true",
                "password": "secrets"
                }
        response = self.test_client.post('/api/v1/signup', json=user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Enter Email')

    def test_signup_with_invalid_lastname(self):
        """tests whether the signup function will return an expecte error\
            upon signing up with an invalid lastname
        """
        user = {"firstname": "4546",
                "lastname": 4564,
                "othernames": "Nsubuga",
                "email": "kalungi2k6@yahoo.com",
                "PhoneNumber": 777777,
                "username": "nanfuka",
                "isAdmin": "true",
                "password": "secrets"
                }
        response = self.test_client.post('/api/v1/signup', json=user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'lastname should be a string')

    def test_signup_with_invalid_admin_status(self):
        """tests whether the signup function will return an expecte error\
            upon signing up with an invalid admin status
        """
        user = {"firstname": "frae",
                "lastname": "sfdrg",
                "othernames": "Nsubuga",
                "email": "kampala@yahoo.com",
                "phoneNumber": 777777,
                "username": "nanfuka",
                "isAdmin": "trues",
                "password": "secrets"
                }
        response = self.test_client.post('/api/v1/signup', json=user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'IsAdmin should either be true or false')

    def test_signup_with_weak_password(self):
        """tests whether the signup function will return an expecte error\
            upon signing up with a weak password
        """
        user = {"firstname": "frae",
                "lastname": "sfdrg",
                "othernames": "Nsubuga",
                "email": "kampala@yahoo.com",
                "phoneNumber": 777777,
                "username": "nanfuka",
                "isAdmin": "true",
                "password": "dfg"
                }
        response = self.test_client.post('/api/v1/signup', json=user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Increase the strength of your password')
    
    def test_signup_with_no_password(self):
        """tests whether the signup function will return an expecte error\
            upon signing up without a password
        """
        user = {"firstname": "frae",
                "lastname": "sfdrg",
                "othernames": "Nsubuga",
                "email": "kampala@yahoo.com",
                "phoneNumber": 777777,
                "username": "nanfuka",
                "isAdmin": "true",
             
                }
        response = self.test_client.post('/api/v1/signup', json=user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Enter password')

        
