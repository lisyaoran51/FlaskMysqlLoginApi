import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import jwt_required, get_jwt_claims, jwt_optional, get_jwt_identity
from datetime import datetime




class CurrentUser(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('birthdate', 
        type=lambda x: datetime.strptime(x,'%Y-%m-%d').date(),
        required=True,
        help="This field cannot be blank."
    )

    @jwt_optional
    def get(self, user_id):

        user_id = get_jwt_identity()
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        return user.json()


    @jwt_optional
    def delete(self, user_id):
        
        user_id = get_jwt_identity()
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        user.delete_from_db()
        return {'message': 'User deleted'}, 200
    

    @jwt_optional
    def put(self):

        user_id = get_jwt_identity()
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        data = CurrentUser.parser.parse_args()

        if not data['username']:
            return {'message': 'username could not be blank'}, 400

        if not data['birthdate']:
            return {'message': 'birthdate could not be blank'}, 400

        user.username = data['username']
        user.birthdate = data['birthdate']

        user.save_to_db()

        return user.json()