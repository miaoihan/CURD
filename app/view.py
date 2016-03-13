#!/usr/bin/python
# coding=utf-8
from app import app, db
from flask import render_template, request, url_for, redirect, session
from model import Article
from datetime import datetime


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
    created_time = datetime.now()
    article = Article(title=title, author=author, content=content, created_time=created_time)
    db.session.add(article)
    db.session.commit()
    return redirect(url_for('show_article'))


@app.route('/update_article', methods=['POST'])
def update_article():
    form = request.form
    title = form['title']
    author = form['author']
    content = form['content']
    created_time = datetime.now()
    article_id = form['article_id']
    article = Article(id=article_id, title=title, author=author, content=content, created_time=created_time)
    db.session.merge(article)
    db.session.commit()
    return redirect(url_for('show_article'))


@app.route('/articles')
def show_article():
    articles = Article.query.filter_by(del_status=1)
    return render_template('show_article.html', articles=articles)


@app.route('/edit_article/<int:article_id>')
def edit_article(article_id):
    article = Article.query.get_or_404(article_id)
    # 刷新session
    session['article_id'] = article.id
    session['title'] = article.title
    session['author'] = article.author
    session['content'] = article.content
    return render_template('edit_article.html')


@app.route('/del_article/<int:article_id>')
def del_article(article_id):
    # print article_id
    article = Article.query.get_or_404(article_id)
    article.del_status = 0
    db.session.commit()
    return redirect(url_for('show_article'))
