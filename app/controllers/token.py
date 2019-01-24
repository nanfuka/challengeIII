from app.views import app
import json


class Token:
    def get_user_token(self):
        user = {"firstname": "fhgfghfh",
                "lastname": "fried",
                "othernames": "dorotyh",
                "email": "kalvf@fvkfgfgg.com",
                "phoneNumber": 1111111111,
                "username": "mathew",
                "isAdmin": "false",
                "password": "princess"
                }
        response = app.test_client.post('/api/v1/auth/signup', data=user)
        user_login = {"username": "mathew",
                      "password": "princes"
                      }

        response = test_client.post('/api/v1/auth/login', data=user)
        data = json.loads(response.data.decode())
        # token = json.loads(response.data)['token']
        # return token
        token = (data['data'][0]['token'])
        print(token)
        return token



    "data": [
        {
            "message": "You have signedup with ireporter as a user",
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImJyb2d0dmZmaGVyIiwiaXNBZG1pbiI6ImZhbHNlIiwiZXhwIjoxNTQ4MzE0NDkzfQ.ORy4MJxDVa16aVXbIK_h0llndu7p0Jt5VyvKN-Ceog0",
            "user": [
                {
                    "email": "kafhjcgscgfdfgxFgxxssfddfdgfsdDcsdlkxgrfdu@gmail.com",
                    "firstname": "gvghcgvh",
                    "isadmin": "false",
                    "lastname": "fjkhjhk",
                    "othernames": "1234",
                    "phonenumber": 21545,
                    "userid": 9,
                    "username": "brogtvffher"
                }
            ]
        }
    ],
    "status": 201
}