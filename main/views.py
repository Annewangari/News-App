from flask import render_template
from app import app
@app.route('/')
def index():

    return render_template('index.html')

@app.route('/news-article')
def index():
@app.route('/newsArticle')
def newsArticle():

    return render_template('news-article.html')
    return render_template('newsArticle.html')

@app.route('/news-source')
def index():
@app.route('/newsSource')
def newsSource():

    return render_template('news-source.html')
    return render_template('newsSource.html')
