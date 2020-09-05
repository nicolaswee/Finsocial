import os, sys, json
from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)

db = SQLAlchemy(app)

CORS(app)

class UsersModel(db.Model):
    __tablename__ = "users_table"

    name = db.Column(db.String(), primary_key=True)
    password = db.Column(db.String())

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return f"<Users {self.name}>"

@app.route('/test',methods=['GET'])
def test():
    return jsonify({'status':True, "message":"Successful"}), 200

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")