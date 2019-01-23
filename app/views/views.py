from flask import Flask, jsonify, request, json
from app.controllers.user_controllers import User_controller
from app.controllers.incident_controllers import Incidence
from app.validators import Validators
import jwt
import datetime


app = Flask(__name__)
validators = Validators()
user_controller = User_controller()
incidence = Incidence()


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
        new = user_controller.create_user(
            firstname,
            lastname,
            othernames,
            email,
            phoneNumber,
            username,
            isAdmin,
            password)
        loggedin_admin = user_controller.adminlogin(username, password)
        if loggedin_admin:
            admin_token = jwt.encode({'username': data['username'],
                                      'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(minutes=30)}, 'hodulop')
            return jsonify(
                {"status": 201, "data": [
                 {"token": admin_token.decode('utf-8'),
                  "user": new,
                  "message":
                  "you have successfully logged in as a adminstrator"
                  }]})

        else:
            token = jwt.encode({'username': data['username'],
                                'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(minutes=30)}, 'amauser')
            return jsonify(
                {"status": 201,
                    "data": [{"token": token.decode('utf-8'),
                              "user": new,
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
            admin_token = jwt.encode({'username': data['username'],
                                      'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(minutes=30)}, 'hodulop')
            return jsonify(
                {"status": 200, "data":
                 [{"user": user_controller.loginss(
                                username, password),
                   "token": admin_token.decode('utf-8'),
                   "message":
                   "you have successfully logged in as an administrator"}]})

        else:
            token = jwt.encode({"username": data['username'],
                                'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(minutes=30)}, 'amauser')
            return jsonify({"status": 200, "data": [
                {"user": user_controller.loginss(username, password),
                 "token": token.decode('utf-8'),
                 "message": "you have successfully logged in as a user"}]})
    else:
        return jsonify({"status": 403,
                        "error": "Invalid username and password"})


@app.route('/api/v1/auth/intervention', methods=['POST'])
# @users.customer_token
def create_intervetion():
    """A user can create a redflag by entering all the required data"""
    data = request.get_json()
    if not data:
        return jsonify({"status": 400, "message": "enter all fields"})
    createdby = data.get('createdby')
    location = data.get('location')
    comment = data.get('comment')
    incident_type = data.get('incident_type')
    status = "draft"
    images = data.get('images')
    videos = data.get('videos')
    if len(data) < 3:
        return jsonify({"status": 400, "message": "enter all fields"})

    error_message = validators.validate_input(
        createdby, incident_type, status, images, data)
    wrong_location = validators.validate_location(location)
    validate_comment = validators.validate_coment(comment)
    if wrong_location:
        return jsonify({"status": 400, 'error': wrong_location}), 400
    elif error_message:
        return jsonify({"status": 400, 'error': error_message}), 400

    new_incident = incidence.create_incidences(
        data['createdby'],
        data['incident_type'],
        data['location'],
        data['images'],
        data['videos'],
        data['comment'])
    return jsonify({"status": 201, "user": new_incident})


@app.route('/api/v1/interventions')
# @users.admin_token
def get_all_interventions():
    """ A user can retrieve all intervention records\
    only after including the bearer token in the header
    """
    return incidence.get_all_incidents('intervention')


@app.route('/api/v1/interventions/<int:intervention_id>', methods=['DELETE'])
# @users.admin_token
def get_intervention():
    incidence.delete_record(intervention_id, 'intervention')


@app.route('/api/v1/interventions/<int:intervention_id>')
# @users.admin_token
def get_one_intervention(intervention_id):
    return incidence.get_one_incident('intervention', intervention_id)


@app.route(
    '/api/v1/intervention/<int:intervention_id>/location', methods=['PATCH'])
# @jwt_required
def edit_location(intervention_id):
    """from this route, the user can edit the location and an intervation"""
    data = request.get_json()
    location = data.get('location')

    wrong_location = validators.validate_location(location)
    if wrong_location:
        return jsonify({"status": 400, 'error': wrong_location}), 400
    elif incidence.edits_incident(intervention_id, 'intervention', location):
        return jsonify({"status": 200, "data":
                        [{"id": intervention_id,
                            "message": "successfully edited a location"}]})
    return jsonify({"status": 200,
                    "message": "intervation id is not available"})


@app.route(
    '/api/v1/interventions/<intervention_id>/comment', methods=['PATCH'])
# @jwt_required
def edit_comment(intervention_id):
    """
    using this route a user can modify the location of a single redflag
    """
    data = request.get_json()
    comment = data.get('comment')

    invalid_comment = validators.validate_coment(comment)
    if invalid_comment:
        return jsonify({"status": 400, 'error': invalid_comment}), 400
    elif incidence.edits_comment(intervention_id, 'intervention', comment):
        return jsonify({"status": 200, "data":
                        [{"id": intervention_id,
                          "message": "successfully edited a comment"}]})
    return jsonify(
        {"status": 200, "message": "intervation id is not available"})
