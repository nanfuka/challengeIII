from flask import Flask, jsonify, request, json
import re
from ..db import DatabaseConnection
from app.model.users import User
import jwt
from functools import wraps
from app.controllers.token import get_current_identity


userkey = 'amauser'
adminkey = 'amanadmin'

db = DatabaseConnection()


class User_controller():

    def signup(self, *args):
        """This method innitialises all the attributes that will be used in \
        the creation of a user"""
        self.firstname = args[0]
        self.lastname = args[1]
        self.othernames = args[2]
        self.email = args[3]
        self.phoneNumber = args[4]
        self.username = args[5]
        self.isAdmin = args[6]
        self.password = args[7]

    def create_user(self, firstname,
                    lastname,
                    othernames,
                    email,
                    phoneNumber,
                    username,
                    isAdmin,
                    password):
        query = """ INSERT INTO users (firstname, lastname, othernames, email, \
                phoneNumber, username, isAdmin, password) \
                VALUES ('{}', '{}', '{}','{}', '{}', '{}','{}', '{}') 
                RETURNING userid, firstname, lastname, othernames, email, 
                phoneNumber, username, isAdmin;"""\
                .format(firstname,
                        lastname,
                        othernames,
                        email,
                        phoneNumber,
                        username,
                        isAdmin,
                        password)
        db.cursor.execute(query)
        return db.cursor.fetchone()

    def check_repitition(self, username, email, password):
        """This method checks through the list \
           for values to prevent a user 
           from regestering twice
        """
        if self.check_email_exists(email):
            return "Email already exists, choose another one"
        elif self.check_username_exists(username):
            return "Username already exists, choose another one"

        elif len(password) < 4:
            return "password strength is too weak"

    def check_username_exists(self, username):
        """This method checks through the list for values to avoid a user 
            from regestering twice with the same username
        """
        query = "SELECT * from users where username = '{}';".format(username)
        db.cursor.execute(query)
        user_details = db.cursor.fetchall()
        if user_details:
            return user_details

    def check_email_exists(self, email):
        """This method checks through the list for values to avoid a user 
            from regestering twice
        """
        query = "SELECT * from users where email = '{}';".format(email)
        db.cursor.execute(query)
        user_details = db.cursor.fetchall()
        if user_details:
            return user_details

    def check_password_exists(self, password):
        """This method checks through the list for values to avoid a user 
            from regestering twice
        """
        query = "SELECT * from users where password = '{}';".format(password)
        db.cursor.execute(query)
        user_details = db.cursor.fetchall()
        if user_details:
            return user_details

    def drop_table(self, table_name):
        drop = f"DROP TABLE {table_name};"
        db.cursor.execute(drop)

    def user_token(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({'message': 'Token is missing'}), 404
            try:
                jwt.decode(token, userkey)
            except:
                return jsonify({'message': 'Token is invalid'}), 404
            return f(*args, **kwargs)
        return decorated

    def admin_token(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({'message': 'Token is missing'}), 404
            try:
                jwt.decode(token, adminkey)
            except:
                return jsonify({'message': 'Token is invalid'}), 404
            return f(*args, **kwargs)
        return decorated

    def adminlogin(self, isAdmin):
        """method for logging in the adminstrator"""

        if isAdmin is True:
            return True

    
    def get_admin(self):
        query = "SELECT * from users where isAdmin = 'true'"
        db.cursor.execute(query)
        admin_data = db.cursor.fetchone()
        return admin_data


    def get_user(self):
        query = "SELECT * from users where isAdmin = False"
        db.cursor.execute(query)
        admin_data = db.cursor.fetchone()
        return True


    def login(self, username, password):
        """method for logging in the registered none admin-user"""

        query = f"""SELECT * FROM users WHERE username =\
         '{username}' AND password = '{password}'"""
        db.cursor.execute(query)
        user_details = db.cursor.fetchall()
        return user_details


    def logins(self, username, password):
        query = "SELECT * FROM users WHERE username='{}';".format(username)
        db.cursor.execute(query)
        user_details = db.cursor.fetchone()
        if user_details:

            if user_details['password'] == password:
                return user_details
            return {"error": "wrong email credentials"}
        return jsonify({"status": 403,
                        "error": "Invalid username and password"})

    def loginss(self, username, password):
        query = f"""SELECT * FROM users WHERE username = '{username}' \
        AND password = '{password}'"""
        db.cursor.execute(query)
        user_details = db.cursor.fetchone()
        return user_details
        # if user_details:
        #     return user_details

        # return jsonify({"error": "enter the right username and password"})

    def get_all_users(self, username):
        query = "SELECT * FROM users WHERE username='{}';".format(username)
        db.cursor.execute(query)
        user_details = db.cursor.fetchone()
        return user_details

    def adminlogin(self, username, password):
        """method for logging in the adminstrator"""
        query = "SELECT * FROM users WHERE username='{}' and password='{}';".format(username, password)
        db.cursor.execute(query)
        user_details = db.cursor.fetchone()
        if user_details['isadmin']== "true":
            return user_details

    def userlogin(self, username, password):
        """method for logging in the adminstrator"""
        query = "SELECT * FROM users WHERE username='{}' and password='{}';".format(username, password)
        db.cursor.execute(query)
        user_details = db.cursor.fetchone()
        if user_details['isadmin']== "false":
            return user_details


    def get_all_users(self, username):
        query = "SELECT * FROM users WHERE username='{}';".format(username)
        db.cursor.execute(query)
        user_details = db.cursor.fetchone()
        return user_details

    def get_all_specific_(self, username):
        query = "SELECT * FROM users WHERE username='{}';".format(username)
        db.cursor.execute(query)
        user_details = db.cursor.fetchone()
        return user_details


    def admins_login(self, isAdmin):
        if isAdmin == "true":
            return True

    def user_token(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({'message': 'Token is missing'}), 404
            try:
                jwt.decode(token, userkey)
            except:
                return jsonify({'message': 'Token is invalid'}), 404
            return f(*args, **kwargs)
        return decorated

    def admin_token(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({'message': 'Token is missing'}), 404
            try:
                jwt.decode(token, adminkey)
            except:
                return jsonify({'message': 'Token is invalid'}), 404
            return f(*args, **kwargs)
        return decorated

       
