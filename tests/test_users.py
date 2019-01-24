# import unittest
# from app.views.views import app
# from app.controllers.user_controllers import User_controller
# import json
# from app.db import DatabaseConnection
# cont = User_controller()


# class TestUsers(unittest.TestCase):
#     def setUp(self):
#         self.test_client = app.test_client()
#         # db = DatabaseConnection()
#         cont.drop_table('incidents')
#         cont.drop_table('users')
#         # # db.create_users_table
#         # # db.create_incident_tables
#         self.db = DatabaseConnection()

#     def test_user_register(self):
#         user = {"firstname": "fhgfghfh",
#                 "lastname": "fried",
#                 "othernames": "dorotyh",
#                 "email": "kalvf@fvkfgfgg.com",
#                 "phoneNumber": 1111111111,
#                 "username": "subbcfdhfgfvdfhcvccsfess",
#                 "isAdmin": "false",
#                 "password": "sghfrhuvfbbfgdfbccsdcess"
#                 }

#         response = self.test_client.post(
#             'api/v1/auth/signup',
#             content_type='application/json',
#             data=json.dumps(user)
#         )

#         data = json.loads(response.data.decode())
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(data['status'], 201)
#         token = (data['data'][0]['token'])
#         self.assertEqual(data['data'][0]['message'],
#                          'You have signedup with ireporter as a user')
#         self.assertEqual(data['data'][0]['token'], token)

#     def test_user_register_with_out_firstname(self):
#         user = {"firstname": "",
#                 "lastname": "fried",
#                 "othernames": "dorotyh",
#                 "email": "kalvf@fvkfgfgg.com",
#                 "phoneNumber": 1111111111,
#                 "username": "subbcfdhfgfvdfhcvccsfess",
#                 "isAdmin": "false",
#                 "password": "sghfrhuvfbbfgdfbccsdcess"
#                 }

#         response = self.test_client.post(
#             'api/v1/auth/signup',
#             content_type='application/json',
#             data=json.dumps(user)
#         )

#         data = json.loads(response.data.decode())
#         self.assertEqual(response.status_code, 400)

#         self.assertEqual(data['status'], 400)
#         self.assertEqual(data['error'], "Enter firstname")

#     def test_user_register_with_out_firstname(self):
#         user = {"firstname": "debd",
#                 "lastname": "",
#                 "othernames": "dorotyh",
#                 "email": "kalvf@fvkfgfgg.com",
#                 "phoneNumber": 1111111111,
#                 "username": "subbcfdhfgfvdfhcvccsfess",
#                 "isAdmin": "false",
#                 "password": "sghfrhuvfbbfgdfbccsdcess"
#                 }

#         response = self.test_client.post(
#             'api/v1/auth/signup',
#             content_type='application/json',
#             data=json.dumps(user)
#         )

#         data = json.loads(response.data.decode())
#         self.assertEqual(response.status_code, 400)

#         self.assertEqual(data['status'], 400)
#         self.assertEqual(data['error'], 'Enter lastname')

#     def test_user_register_with_out_invalid_email(self):
#         user = {"firstname": "debd",
#                 "lastname": "lorin",
#                 "othernames": "dorotyh",
#                 "email": "kalvffvkfgfgg.com",
#                 "phoneNumber": 1111111111,
#                 "username": "subbcfdhfgfvdfhcvccsfess",
#                 "isAdmin": "false",
#                 "password": "sghfrhuvfbbfgdfbccsdcess"
#                 }

#         response = self.test_client.post(
#             'api/v1/auth/signup',
#             content_type='application/json',
#             data=json.dumps(user)
#         )

#         data = json.loads(response.data.decode())
#         self.assertEqual(response.status_code, 400)

#         self.assertEqual(data['status'], 400)
#         self.assertEqual(
#             data['error'],
#             'Invalid email, it should be in this format; kals@gma.com')

#     def test_user_register_with_out__email(self):
#         user = {"firstname": "debd",
#                 "lastname": "lorin",
#                 "othernames": "dorotyh",
#                 "email": "",
#                 "phoneNumber": 1111111111,
#                 "username": "subbcfdhfgfvdfhcvccsfess",
#                 "isAdmin": "false",
#                 "password": "sghfrhuvfbbfgdfbccsdcess"
#                 }

#         response = self.test_client.post(
#             'api/v1/auth/signup',
#             content_type='application/json',
#             data=json.dumps(user)
#         )

#         data = json.loads(response.data.decode())
#         self.assertEqual(response.status_code, 400)

#         self.assertEqual(data['status'], 400)
#         self.assertEqual(data['error'], 'Enter Email')

#     def test_user_register_with_invalid_phonenumber(self):
#         user = {"firstname": "debd",
#                 "lastname": "lorin",
#                 "othernames": "dorotyh",
#                 "email": "kalumgi@gmail.com",
#                 "phoneNumber": "grace",
#                 "username": "subbcfdhfgfvdfhcvccsfess",
#                 "isAdmin": "false",
#                 "password": "sghfrhuvfbbfgdfbccsdcess"
#                 }

#         response = self.test_client.post(
#             'api/v1/auth/signup',
#             content_type='application/json',
#             data=json.dumps(user)
#         )

#         data = json.loads(response.data.decode())
#         self.assertEqual(response.status_code, 400)

#         self.assertEqual(data['status'], 400)
#         self.assertEqual(
#             data['error'],
#             'phoneNumber should be made up of numbers')

#     def test_user_register_with_out_phonenumber(self):
#         user = {"firstname": "debd",
#                 "lastname": "lorin",
#                 "othernames": "dorotyh",
#                 "email": "kalumgi@gmail.com",

#                 "username": "subbcfdhfgfvdfhcvccsfess",
#                 "isAdmin": "false",
#                 "password": "sghfrhuvfbbfgdfbccsdcess"
#                 }

#         response = self.test_client.post(
#             'api/v1/auth/signup',
#             content_type='application/json',
#             data=json.dumps(user)
#         )

#         data = json.loads(response.data.decode())
#         self.assertEqual(response.status_code, 400)

#         self.assertEqual(data['status'], 400)
#         self.assertEqual(data['error'], 'Enter phone number')

#     def test_user_register_with_invalid_isAdmin(self):
#         user = {"firstname": "debd",
#                 "lastname": "lorin",
#                 "othernames": "dorotyh",
#                 "email": "kalumgi@gmail.com",
#                 "phoneNumber": 4582,
#                 "username": "subbcfdhfgfvdfhcvccsfess",
#                 "isAdmin": "falses",
#                 "password": "sghfrhuvfbbfgdfbccsdcess"
#                 }

#         response = self.test_client.post(
#             'api/v1/auth/signup',
#             content_type='application/json',
#             data=json.dumps(user)
#         )

#         data = json.loads(response.data.decode())
#         self.assertEqual(response.status_code, 400)

#         self.assertEqual(data['status'], 400)
#         self.assertEqual(data['error'], 'IsAdmin should either be  or False')

#     def test_user_register_without_password(self):
#         user = {"firstname": "debd",
#                 "lastname": "lorin",
#                 "othernames": "dorotyh",
#                 "email": "kalumgi@gmail.com",
#                 "phoneNumber": 4582,
#                 "username": "subbcfdhfgfvdfhcvccsfess",
#                 "isAdmin": "false",

#                 }

#         response = self.test_client.post(
#             'api/v1/auth/signup',
#             content_type='application/json',
#             data=json.dumps(user)
#         )

#         data = json.loads(response.data.decode())
#         self.assertEqual(response.status_code, 400)

#         self.assertEqual(data['status'], 400)
#         self.assertEqual(data['error'], 'Enter password')

#     def test_user_register_without_password(self):
#         user = {"firstname": "debd",
#                 "lastname": "lorin",
#                 "othernames": "dorotyh",
#                 "email": "kalumgi@gmail.com",
#                 "phoneNumber": 4582,
#                 "username": "subbcfdhfgfvdfhcvccsfess",
#                 "isAdmin": "false",

#                 }

#         response = self.test_client.post(
#             'api/v1/auth/signup',
#             content_type='application/json',
#             data=json.dumps(user)
#         )

#         data = json.loads(response.data.decode())
#         self.assertEqual(response.status_code, 400)

#         self.assertEqual(data['status'], 400)
#         self.assertEqual(data['error'], 'Enter password')
