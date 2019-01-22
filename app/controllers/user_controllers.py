from flask import Flask, jsonify, request, json
import re
from ..db import DatabaseConnection
from app.model.users import User
import jwt
from functools import wraps


userkey = 'amauser'
adminkey = 'hodulop'

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

        query = "INSERT INTO users (firstname, lastname, othernames, email, \
                phoneNumber, username, isAdmin, password) \
                VALUES ('{}', '{}', '{}','{}', '{}', '{}','{}', '{}');"\
                    .format(self.firstname,
                            self.lastname,
                            self.othernames,
                            self.email,
                            self.phoneNumber,
                            self.username,
                            self.isAdmin,
                            self.password)
        db.cursor.execute(query)
        user = User(*args)
        newuser = user.get_dictionary()
        return newuser

    def check_repitition(self, username, email, password):
        """This method checks through the list for values to avoid a user 
            from regestering twice
        """
        if self.check_email_exists(email):
            return "Email already exists, choose another one"
        elif self.check_username_exists(username):
            return "Username already exists, choose another one"
        elif self.check_password_exists(password):
            return "password already exists, choose another one"
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

    def adminlogin(self, username, password):
        """method for logging in the adminstrator"""

        if username == 'admin' and password == 'ohpriz':
            return True
