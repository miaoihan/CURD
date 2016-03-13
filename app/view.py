#!/usr/bin/python
# coding=utf-8
from app import app, db
from flask import render_template, request, url_for, redirect
from model import Article


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/new_article', methods=['GET', 'POST'])
def new_article():
    if request.method == 'GET':
        # return render_template(url_for('new_article'))
        return render_template('new_article.html')
    # 数据库添加业务
    # 写入数据库
    form = request.form
    title = form['title']
    author = form['author']
    content = form['content']
    article = Article(title=title, author=author, content=content)
    db.session.add(article)
    db.session.commit()
    return redirect(url_for('show_article'))


@app.route('/articles')
def show_article():
    articles = Article.query.all()
    return render_template('show_article.html', articles=articles)


@app.route('/edit_article/<int:article_id>')
def edit_article(article_id):
    article = Article.query.get_or_404(article_id)
    title = article.title
    author = article.author
    content = article.content
    return redirect(url_for('new_article'))


@app.route('/del_article/<int:article_id>')
def del_article(article_id):
    # print article_id
    article = Article.query.get_or_404(article_id)
    db.session.delete(article)
    db.session.commit()
    return redirect(url_for('show_article'))

