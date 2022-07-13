from app import app
from flask import render_template
from .request import get_news_source, publishedArticles, randomArticles, topHeadlines


@app.route('/')
def home():
    articles = publishedArticles()

    return render_template('home.html', articles=articles)


@app.route('/headlines')
def headlines():
    headlines = topHeadlines()

    return render_template('headlines.html', headlines=headlines)


@app.route('/articles')
def articles():
    random = randomArticles()

    return render_template('articles.html', random=random)


@app.route('/sources')
def sources():
    newsSource = get_news_source()

    return render_template('sources.html', newsSource=newsSource)


@app.route('/category/business')
def business():
    sources = topHeadlines('business')

    return render_template('business.html', sources=sources)


@app.route('/category/tech')
def tech():
    sources = topHeadlines('tech')

    return render_template('tech.html', sources=sources)


@app.route('/category/entertainment')
def entertainment():
    sources = topHeadlines('entertainment')

    return render_template('entertainment.html', sources=sources)


@app.route('/category/science')
def science():
    sources = topHeadlines('science')

    return render_template('science.html', sources=sources)


@app.route('/category/sports')
def sports():
    sources = topHeadlines('sport')

    return render_template('sport.html', sources=sources)


@app.route('/category/health')
def health():
    sources = topHeadlines('health')

    return render_template('health.html', sources=sources)
