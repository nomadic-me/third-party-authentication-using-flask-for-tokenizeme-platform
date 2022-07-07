from app import login, db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    #__tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    nickname = db.Column(db.String(64), nullable=False)
    def __repr__(self, username):
        return '<User> {}'.format(self.nickname)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
