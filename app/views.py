from app import app
from flask import render_template
from newsapi import NewsApiClient
from .config import Config

@app.route('/')
def home():

    newsapi = NewsApiClient(api_key= Config.API_KEY)

    top_headlines = newsapi.get_top_headlines(sources= 'techcrunch, the-verge, gizmodo, the-next-web, techradar, recode, ars-technica')

    all_articles = top_headlines['articles']

    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []

    for i in range(len(all_articles)):
        main_article = all_articles[i]

        title.append(main_article['title'])
        desc.append(main_article['description'])
        author.append(main_article['author'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])

        contents = zip(title, desc, author, img, p_date, url)

    return  render_template('home.html', content = contents)