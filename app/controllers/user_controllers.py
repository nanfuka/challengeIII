from flask import Flask, jsonify, request, json
import re
from ..db import DatabaseConnection
from app.model.users import User 

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
                VALUES ('{}', '{}', '{}','{}', '{}', '{}','{}', '{}');".format(self.firstname, self.lastname, self.othernames, self.email, self.phoneNumber, self.username, self.isAdmin, self.password)
        db.cursor.execute(query)
        user = User(*args)
        newuser = user.get_dictionary()
        return newuser


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

    def check_email_exists(self, email):
        """This method checks through the list for values to avoid a user 
            from regestering twice
        """
        query = "SELECT * from users where password = '{}';".format(password)
        db.cursor.execute(query)
        user_details = db.cursor.fetchall()
        if user_details:
            return user_details



    


    
