#!/usr/bin/python
# coding=utf-8
from app import app
from flask_script import Manager
from app.model import Article

manage = Manager(app)


@manage.command
def query_all():
    # users = User.query_all()
    articles = Article.query.all()
    for a in articles:
        print a


if __name__ == '__main__':
    app.run()




