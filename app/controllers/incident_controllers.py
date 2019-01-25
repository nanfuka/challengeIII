# from app.models.incident import Incident, incidents
from flask import Flask, jsonify, request, json
from flask import Flask, jsonify, request, json
import re
from ..db import DatabaseConnection
from app.model.users import User
import jwt
from functools import wraps
from app.controllers.token import get_current_identity


userkey = 'amauser'
adminkey = 'hodulop'

db = DatabaseConnection()


class Incidence:
    def create_incidences(self, createdby,
                          incident_type,
                          location,
                          images,
                          videos,
                          comment):
        query = """ INSERT INTO incidents \
        (createdby, incident_type, location, images, videos, comment) VALUES ('{}', '{}', '{}','{}', '{}', '{}') RETURNING incident_id, createdby, incident_type, location, status,images, videos, comment;"""\
                .format(createdby,
                        incident_type,
                        location,
                        images,
                        videos,
                        comment
                        )
        db.cursor.execute(query)
        return db.cursor.fetchall()

    def get_one_incident(self, incident_type, incident_id):
        """Function that returns a single incidence"""

        query = "SELECT * FROM incidents WHERE incident_type = '{}' AND incident_id = {};".format(
            incident_type, incident_id)
        db.cursor.execute(query)
        return db.cursor.fetchall()
    
    def get_all_incidents(self, incident_type):
        """Function that returns all incidents of a particular type"""
        query = "SELECT * FROM incidents WHERE incident_type = '{}';".format(incident_type)
        db.cursor.execute(query)
        return db.cursor.fetchall()


    def edits_incident(self, incident_id, incident_type, location):
        query = "UPDATE incidents SET location = '{}' WHERE incident_id = '{}'\
         AND incident_type = '{}' RETURNING * ;".format(
            location, incident_id, incident_type)
        db.cursor.execute(query)
        return db.cursor.fetchone()

    def edits_comment(self, incident_id, incident_type, comment):
        query = "UPDATE incidents SET comment = '{}' WHERE incident_id = '{}' \
        AND incident_type = '{}' RETURNING * ;".format(
            comment, incident_id, incident_type)
        db.cursor.execute(query)
        return db.cursor.fetchall()

    def delete_record(self, incident_id, incident_type):
        """method for deleting a particular intervention"""
        
        query = "DELETE FROM incidents WHERE u USING incidents WHERE incident_id = {} AND \
            incident_type ='{}'".format(incident_id, incident_type)

   
    def check_incidents(self, incident_id, incident_type):
        """method for checking if there are any interventions in the system"""
        query = "SELECT * FROM incidents WHERE incident_id = {} and \
            incident_type ='{}'".format(incident_id, incident_type)
        db.cursor.execute(query)
        return db.cursor.fetchall()

    def verify_createdby_value(self, createdby, incident_type):
        """method for checking if there are any interventions in the system"""
        query = "SELECT * FROM users WHERE userid = {} \
            ".format(createdby, incident_type)
        db.cursor.execute(query)
        return db.cursor.fetchall()

    def modify_status(self, incident_type, incident_id):
        "Method for modifying the status of a particular incident"
        update = db.cursor.execute(
            "UPDATE  incidents SET status = '{}' WHERE incident_id = '{}'\
             and incident_type ='{}'".format(incident_id, incident_type))
