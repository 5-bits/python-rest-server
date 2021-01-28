import mysql.connector
import sys
import os
import datetime
from flask_restful import Resource, Api, reqparse
from flask import jsonify, request
class queries(Resource):
    def __init__(self):

        #os.system('sudo service mysql restart')
        self.mydb = mysql.connector.connect(
                host = "localhost",
                user = "server",
                password = "5115abcd",
                db = "test"
                )
        self.cursor = self.mydb.cursor()
        self.date = datetime.datetime.now()
        self.vitals = {}
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('ID', type = int)
        self.parser.add_argument('vitals')

    def RESTART():
        os.system('sudo service mysql restart')          
   
    def post(self):
        data = self.parser.parse_args()
        ID = data['ID']
        vitals = data['vitals']
        query = "INSERT INTO vitals (id, date, vitals) VALUES (%s, %s, %s)"
        vals = (ID, self.date, vitals)
        self.cursor.execute(query, vals)
        self.mydb.commit()
        resp = jsonify(data)
        return resp

    def get(self):
        query = "SELECT * FROM vitals;"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        resp = jsonify(rows)
        return resp

    def INSERT(self, vitals, ID):
        query = "INSERT INTO vitals (is, date, vitals) VALUES (%s, %s, %s)"
        vals = (ID, self.date, vitals)
        self.cursor.execute(query, vals)
        self.mydb.commit()

            

        

