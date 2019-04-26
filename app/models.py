from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db
from app import login

# defines user within db
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True)
    password_hash = db.Column(db.String(128))
    # links user to Posts
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    # login related
    # is_authenticated = db.Column(db.Boolean)
    # is_active = db.Column(db.Boolean)
    # is_anonymous = db.Column(db.Boolean)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # def get_id(self):
    #     return self.id

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

# defines listings within db
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    body = db.Column(db.String(256))
    # allows us to list posts chronologically
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # allows us to attach users to their posts
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    uname = db.Column(db.String(64), index=True)
    contact = db.Column(db.String(128))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
