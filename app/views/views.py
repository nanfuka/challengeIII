from flask import Flask, jsonify, request, json
from app.controllers.user_controllers import User_controller
from app.validators import Validators
import jwt
import datetime


app = Flask(__name__)
validators = Validators()
user_controller = User_controller()


@app.route('/')
def index():
    """index url"""
    return jsonify({"status": 201, "message": "hi welcome to the ireporter"})


@app.route('/api/v1/auth/signup', methods=['POST'])
def signup():
    """A user can signup by entering all the required data"""
    data = request.get_json()
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    othernames = data.get('othernames')
    email = data.get('email')
    phoneNumber = data.get('phoneNumber')
    username = data.get('username')
    isAdmin = data.get('isAdmin')
    password = data.get('password')
    user = User_controller()

    invalid_user_input = validators.validate_strings(
        firstname, lastname, othernames, username, data)
    if invalid_user_input:
        return jsonify({"status": 400, 'error': invalid_user_input}), 400
    invalid_email = validators.validate_email(email)
    if invalid_email:
        return jsonify({"status": 400, 'error': invalid_email}), 400
    invalid_type = validators.validat_numbers(phoneNumber)
    if invalid_type:
        return jsonify({"status": 400, 'error': invalid_type}), 400
    validate_boolean = validators.validate_boolean(isAdmin)
    if validate_boolean:
        return jsonify({"status": 400, 'error': validate_boolean}), 400
    validate_password = validators.validate_password(password)
    if validate_password:
        return jsonify({"status": 400, 'error': validate_password}), 400

    invalid_detail = user_controller.check_repitition(
        username, email, password)
    if invalid_detail:
        return jsonify({"status": 400, 'error': invalid_detail}), 400

    else:
        newuserinput = user.signup(
            data['firstname'],
            data['lastname'],
            data['othernames'],
            data['email'],
            data['phoneNumber'],
            data['username'],
            data['isAdmin'],
            data['password'])
        loggedin_admin = user_controller.adminlogin(username, password)
        if loggedin_admin:
            admin_token = jwt.encode({'username': data['username'],
                                      'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(minutes=30)}, 'hodulop')
            return jsonify({"status": 201, "data": [
                {"token": admin_token.decode('utf-8'),
                 "user": newuserinput,
                 "message": "you have successfully logged in as a adminstrator"
                 }]})

        else:
            token = jwt.encode({'username': data['username'],
                                'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(minutes=30)}, 'amauser')
            return jsonify(
                {"status": 201,
                 "data": [{"token": token.decode('utf-8'),
                           "user": newuserinput,
                           "message":
                           "You have signedup with ireporter as a user"}]})


@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    """A user can login by entering all the right username and password"""    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    logged_in = user_controller.login(username, password)
    if logged_in:
        loggedin_admin = user_controller.adminlogin(username, password)
        if loggedin_admin:
            admin_token = jwt.encode({'username': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'hodulop')
            return jsonify({"status": 201, "data": [
                {"token": admin_token.decode('utf-8'),
                 "user": 'newuserinput',
                 "message": "you have successfully logged in as a adminstrator"
                 }]})

        else:
            token = jwt.encode({'username': data['username'],
                                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'amauser')
            return jsonify(
                {"status": 201,
                 "data": [{"token": token.decode('utf-8'),
                           "user": newuserinput,
                           "message":
                           "You have signedup with ireporter as a user"}]})

@app.route('/api/v1/login', methods=['POST'])
def logins():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    logged_in = user_controller.login(username, password)
    if logged_in:
        loggedin_admin = user_controller.adminlogin(username, password)
        if loggedin_admin:
            admin_token = jwt.encode({'username': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'hodulop')
            return jsonify({"status":200, "data":[{"user":user_controller.loginss(username, password), "token":admin_token.decode('utf-8'), "message":"you have successfully logged in as an administrator"}]})

        else:
            token = jwt.encode({"username": data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'amauser')
            # admin_token = jwt.encode({'username': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'hodulop')
            return jsonify({"status":200, "data":[{"user":user_controller.loginss(username, password), "token":token.decode('utf-8'), "message":"you have successfully logged in as a user"}]})
    else:
        return jsonify({"status":403, "error":"Invalid username and password"})