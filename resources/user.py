import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True)
    parser.add_argument("password", type=str, required=True)

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data["username"]):
            return {"Message": "A User with that username already exist"}, 400

        user = UserModel(data["username"], data["password"])
        UserModel.save_to_db(user)
        return {"Message": "User created successfully."}, 201
