from db import db
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    birthdate = db.Column(db.Date)

    def __init__(self, username, password, birthdate):
        # self.id = _id
        self.username = username
        self.password = password
        self.birthdate = birthdate

    def json(self):

        today = datetime.datetime.now().date()
        

        return {
            'id': self.id,
            'username': self.username,
            'birthdate': self.birthdate,
            'age': today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first() # SELECT * FROM


    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
