import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_jwt_extended import JWTManager

from resources.user import User
from resources.user_login import UserLogin
from resources.user_register import UserRegister
from resources.current_user import CurrentUser

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL_NEW', 'sqlite:///data.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL_NEW')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'my key'
api = Api(app)

#
# @app.before_first_request
# def create_tables():
#     db.create_all()


# jwt = JWT(app, authenticate, identity)
jwt = JWTManager(app)


api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(CurrentUser, '/user')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)  # important to mention debug=True
