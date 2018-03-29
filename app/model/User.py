# coding: utf-8
from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    comment = db.Column(db.String(80), nullable=False)

    def __init__(self, account, password, create_time, comment):
        self.account = account
        self.password = password
        self.create_time = create_time
        self.comment = comment

    def __repr__(self):
        return ""
db.create_all()
