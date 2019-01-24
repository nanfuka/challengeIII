from app.views.views import app
import json



class Token:

    @staticmethod
    def get_user_token():
        user = {"firstname": "fhgfghfh",
                "lastname": "fried",
                "othernames": "dorotyh",
                "email": "kalvf@fvkfgfgg.com",
                "phoneNumber": 1111111111,
                "username": "subbcfdhfgfvdfhcvccsfess",
                "isAdmin": "false",
                "password": "sghfrhuvfbbfgdfbccsdcess"
                }
        response = app.test_client().post('/api/v1/auth/signup', data=user)
        response = app.test_client().post('/api/v1/auth/login', data=user)
        token = json.loads(response.data)['token']
        return token

    @staticmethod
    def get_admin_token():
        user = {
            'username': 'admin',
            'password': 'mynameisadmin'
            }
        response = app.test_client().post('/api/v1/auth/login', data=user)
        token = json.loads(response.data)['token']
        return token