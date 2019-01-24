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
        (createdby, incident_type, location, images, videos, comment) VALUES ('{}', '{}', '{}','{}', '{}', '{}') RETURNING id, createdby, incident_type, location, status,images, videos, comment;"""\
                .format(createdby,
                        incident_type,
                        location,
                        images,
                        videos,
                        comment
                        )
        db.cursor.execute(query)
        return db.cursor.fetchall()

    def get_one_incident(self, incident_type, intervention_id):
        """Function that returns a single incidence"""
        db.cursor.execute(
            "select * from incidents where incident_type = '{}' and id = '{}'"
            .format(incident_type, intervention_id))
        incident = db.cursor.fetchone()

        if incident is None:
            return jsonify({
                "status": 200,
                "message": "There is curretly no required data in the system"
            }), 200

        return jsonify({
            "status": 200,
            "data": incident
        }), 200
    
    def get_all_incidents(self, incident_type):
        """Function that returns all incidents of a particular type"""
        # db.cursor.execute(
        #     "select * from incidents where incident_type = '{}'"
        #     .format(incident_type))
        # incident = db.cursor.fetchall()
        # return incident
        query = "SELECT * FROM incidents WHERE incident_type = '{}';".format(incident_type)
        db.cursor.execute(query)
        return db.cursor.fetchall()


    def edits_incident(self, incident_id, incident_type, location):
        query = "UPDATE incidents SET location = '{}' WHERE id = '{}'\
         AND incident_type = '{}' RETURNING * ;".format(
            location, incident_id, incident_type)
        db.cursor.execute(query)
        return db.cursor.fetchall()

    def edits_comment(self, incident_id, incident_type, comment):
        query = "UPDATE incidents SET comment = '{}' WHERE id = '{}' \
        AND incident_type = '{}' RETURNING * ;".format(
            comment, incident_id, incident_type)
        db.cursor.execute(query)
        return db.cursor.fetchall()

    def delete_record(self, incident_id, incident_type):
        """method for deleting a particular intervention"""
        query = "DELETE FROM incidents WHERE id = {} and \
            incident_type ='{}'".format(incident_id, incident_type)

        db.cursor.execute(query)
        return db.cursor.fetchall()
        update = db.cursor.execute()
        return "deleted"

    def check_incidents(self, incident_id, incident_type):
        """method for checking if there are any interventions in the system"""
        query = "SELECT * FROM incidents WHERE id = {} and \
            incident_type ='{}'".format(incident_id, incident_type)
        db.cursor.execute(query)
        return db.cursor.fetchall()



        # if update:
        #     return jsonify({"data":[{"message": "intervention record has been deleted", "id": redflag_id}]})
        # else:
        #     return False
        #     return jsonify(
        #         {"status": 200, 
        #          "data": [{"id": redflag_id, 
        #                    "message": "red-flag record has been deleted"}]})
        # return jsonify({"status": 200, "message": "no redflag to delete"}), 200

    def modify_status(self, incident_type, incident_id):
        "Method for modifying the status of a particular incident"
        update = db.cursor.execute(
            "UPDATE  incidents SET status = '{}' WHERE incident_id = '{}'\
             and incident_type ='{}'".format(incident_id, incident_type))
