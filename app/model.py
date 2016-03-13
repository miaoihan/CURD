from app import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    author = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(400), unique=True)

    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

    def __repr__(self):
        return "title is {} author is {} content is {}".format(self.title, self.author, self.content)
