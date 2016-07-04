from flask.ext.sqlalchemy import SQLAlchemy
from flaskapp import app,db

# Association table for User-Group
user_group = db.Table('user_group',
        db.Column('user_id',db.Integer,db.ForeignKey('user.user_id')),
        db.Column('group_id',db.Integer,db.ForeignKey('group.group_id'))
        )

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    profile_url = db.Column(db.String())
    fcm_token = db.Column(db.String())
    user_group = db.relationship('Group',
            secondary=user_group,
            backref=db.backref('users', lazy='dynamic'))

    def __init__(self, user_id,first_name,last_name,profile_url,fcm_token):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.profile_url = profile_url
        self.fcm_token = fcm_token

    def __repr__(self):
        return '<User %r>' % self.first_name

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Group(db.Model):
    group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String())
    count = db.Column(db.Integer)

    def __init__(self,name,count):
        self.group_name = name
        self.count = count

    def __repr__(self):
        return '<Group %r>' % self.group_name

    def as_dict(self):
        return {c.name: getattr(self,c.name) for c in self.__table__.columns}
