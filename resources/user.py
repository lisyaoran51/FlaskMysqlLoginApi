import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import jwt_required




class User(Resource):

    @classmethod
    @jwt_required
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        return user.json()


    @classmethod
    @jwt_required
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        user.delete_from_db()
        return {'message': 'User deleted'}, 200
