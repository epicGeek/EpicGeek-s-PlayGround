# coding: utf-8
from app import db


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, title, author, content,create_time):
        self.title = title
        self.author = author
        self.content = content
        self.create_time = create_time

    def __repr__(self):
        return "title:%s , author: %s" % (self.title, self.author)
db.create_all()
