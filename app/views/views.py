from flask import Flask, jsonify, request, json
from app.controllers.user_controllers import User_controller
from app.controllers.incident_controllers import Incidence
from app.validators import Validators
import jwt
import datetime
from app.controllers.token import *


app = Flask(__name__)
validators = Validators()
user_controller = User_controller()
incidence = Incidence()


@app.route('/')
def index():
    """index url"""
    
    return jsonify({"status": 200, "message": "hi welcome to the ireporter"})


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

        loggedin_admin = user_controller.admins_login(data['isAdmin'])
        if loggedin_admin:
            admin_token = encode_token(new['userid'], data['isAdmin'])
            print(admin_token)

            return jsonify({"status": 201, "data": [{"token": admin_token, "user": new,"message": "you have successfully logged in as a adminstrator"}]})
        if not loggedin_admin:
            user_token = encode_token(new['userid'], data['isAdmin']) 
            return jsonify({"status": 201, "data": [{"token": user_token, "user": new,"message": "you have successfully signedup in as a user"}]})


@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    """A user can login by entering all the right username and password"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    loggedin = user_controller.loginss(username, password)
    if not loggedin:
        return jsonify({"status": 403, "error": "Invalid username and password"})
    
    adminlogin = user_controller.adminlogin(username, password)
    if adminlogin:
        print("admin", adminlogin)

        admin_token = encode_token(adminlogin['userid'], adminlogin['isadmin'])


        return jsonify({"status": 201, "data": [
            {"token": admin_token, "user":loggedin,
            # "user": new,
            "message": "you have successfully signedup in as a adminstrator"
            }]})

    userlogin = user_controller.userlogin(username, password)
    if userlogin:
        print("user", userlogin)

        user_token = encode_token(userlogin['userid'], userlogin['isadmin'])

        return jsonify(
            {"status": 201,
            "data": [{"token": user_token, "data":userlogin,
                    
                    "message":
                    "You have loggedin with ireporter as a user"}]})


@app.route('/api/v1/auth/intervention', methods=['POST'])
# @restricted
def create_intervetion():
    """A user can create a redflag by entering all the required data"""
    data = request.get_json()
    print(get_current_identity)
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

    valid_createdby = incidence.verify_createdby_value(createdby, 'intervention')
    if not valid_createdby:
        return jsonify({"error":"created_by value does not reference to any registered user."})

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


@app.route('/api/v1/auth/interventions')
def get_all_interventions():
    """ A user can retrieve all intervention records\
    only her interventions.
    """
    return jsonify({"data": incidence.get_all_incidents('intervention')})


@app.route('/api/v1/auth/interventions/<int:intervention_id>', methods=['DELETE'])
# @restricted
def get_intervention(intervention_id):
    if not incidence.check_incidents(intervention_id, 'intervention'):
        return jsonify({"status":200, "message":"intervention_id supplied is not in the system"})
    
    interventions = incidence.check_incidents(intervention_id, 'intervention')
    if not interventions:
        return jsonify({"status":200, "message":"there are currently no records to delete"})
    delete = incidence.delete_record(intervention_id, 'intervention')
    if delete:
        return jsonify({"status": 200, "data": [{"id": intervention_id, "message": "“intervention record has been deleted”"}]})
    else: return jsonify({"status": 404, "message": "intervantion_id is invalid"})

@app.route('/api/v1/auth/interventions/<int:intervention_id>')
# @restricted
def get_one_intervention(intervention_id):
    """Route from where only one intervention is returned"""
    data = incidence.get_one_incident('intervention', intervention_id)
    if not data:
        return jsonify({"status":200, "message":"There are currently no intervention records"})

    return jsonify({"data":incidence.get_one_incident('intervention', intervention_id)})


@app.route('/api/v1/intervention/<int:intervention_id>/location', methods=['PATCH'])
# @restricted
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


@app.route('/api/v1/interventions/int:<intervention_id>/comment', methods=['PATCH'])
# @restricted
def edit_comment(intervention_id, userid):
    """
    using this route a user can modify the comment of a single intervention
    """
    data = request.get_json()
    location = data.get('location')

    invalid_comment = incidence.validate_coment(comment)

    if invalid_comment:
        return jsonify()
    
    # if invalid_comment:
    #     return jsonify({"status": 400, "error": invalid comment})
    # elif incidence.edits_incident(intervention_id, 'comment', comment):
    #     return jsonify({"status": 200, "data":[{"id": intervention_id,
    # message": "successfully edited a comment"}]})
    # return jsonify({"status": 200,
    #                 "message": "intervation id is not available"})


        # Admin can change the status of a record
        #  to either under investigation, rejected
        #   (in the event of a false claim) or 
        #   resolved (in the event that the claim has
        #    been investigated and resolved).



