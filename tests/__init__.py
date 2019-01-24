# import unittest
# from app.views.views import app
# from app.controllers.user_controllers import User_controller

# import json
# from app.db import DatabaseConnection
# cont = User_controller()


# class BaseTestCase(unittest.TestCase):
#     def setUp(self):
#         """This method sets up the tests client, \
#             connects to the database and sets up the data for signing up
#         """
#         self.test_client = app.test_client()
#         self.db = DatabaseConnection()
#         self.user = {"firstname": "debras",
#                      "lastname": "kalun",
#                      "othernames": "mercy",
#                      "email": "ziwa@yahoo.com",
#                      "phoneNumber": 1111111111,
#                      "username": "morice",
#                      "isAdmin": "false",
#                      "password": "popcorn"

#                      }

#     def test_user_register(self):
#         """This method tests wether a user 
#         can signup with all teh valid data
#         """
#         response = self.test_client.post('/api/v1/signup', json=self.user)
#         data = json.loads(response.data)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(
#             data['message'][0], "You have successfully signedup with ireporter as a user")
#         # self.assertEqual(data['data']['firstname'], "deb")
#         # self.assertEqual(data['data']['othernames'], "mercy")
#         # self.assertEqual(data['data']['username'], "morice")
#         # self.assertEqual(data['data']['phoneNumber'], 1111111111)

#         token = json.loads(response.data.decode())
#         self.assertEqual(data['access_token'], token['access_token'])

#     # def tearDown(self):
#     #     """method for dropping the tables \
#     #        so that the data can be reused
#     #     """
#     #     cont.drop_table('incidents')
#     #     cont.drop_table('users')


# if __name__ == "__main__":
#     unittest.main()
