#!/usr/bin/python
# -*- coding: UTF-8 -*-
from app import app, db
from app.model import Article
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

manage = Manager(app)
migrate = Migrate(app, db)


@manage.command
def query_all():
    # users = User.query_all()
    articles = Article.query.all()
    for a in articles:
        print (a)


@manage.command
def make_shell_context():
    return dict(app=app, db=db, Article=Article)

manage.add_command("shell", Shell(make_context=make_shell_context))
manage.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manage.run()




