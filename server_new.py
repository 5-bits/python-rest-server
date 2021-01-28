from flask import Flask as flask 
from flask_restful import Resource, Api
from server_class import queries

app = flask(__name__)
api = Api(app)
#during deployment secret key is needed
#app.secret_key = 'key'

api.add_resource(queries, '/')
    

if __name__ == '__main__':
    app.run(debug = True, host = "localhost", port = 5000)
    

