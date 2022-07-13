import json
import urllib.request

from newsapi.newsapi_client import NewsApiClient

from .config import Config
from .models import Articles
from .models import Sources

api_key = None
base_url = None
base_url_for_everything = None
base_url_top_headlines = None
base_source_list = None


def zip_content(articles):
    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []

    for article in articles:
        source.append(article['source'])
        title.append(article['title'])
        desc.append(article['description'])
        author.append(article['author'])
        img.append(article['urlToImage'])
        p_date.append(article['publishedAt'])
        url.append(article['url'])

    return zip(source, title, desc, author, img, p_date, url)


def publishedArticles():
    newsapi = NewsApiClient(api_key=Config.API_KEY)

    get_articles = newsapi.get_everything(
        sources='cnn, reuters, cnbc, the-verge, gizmodo, the-next-web, techradar, recode, ars-technica')

    all_articles = get_articles['articles']

    return zip_content(all_articles)


def topHeadlines(tag=None):
    newsapi = NewsApiClient(api_key=Config.API_KEY)

    if tag:
        top_headlines = newsapi.get_top_headlines(category=tag)
    else:
        top_headlines = newsapi.get_top_headlines(
            sources='cnn, reuters, cnbc, techcrunch, the-verge, gizmodo, the-next-web, techradar, recode, ars-technica')

    all_headlines = top_headlines['articles']
    return zip_content(all_headlines)



def randomArticles():
    newsapi = NewsApiClient(api_key=Config.API_KEY)

    random_articles = newsapi.get_everything(sources='the-verge, gizmodo, the-next-web, recode, ars-technica')

    all_articles = random_articles['articles']

    return zip_content(all_articles)


def get_news_source():
    '''
    Function that gets the json response to our url request
    '''
    get_news_source_url = 'https://newsapi.org/v2/sources?apiKey=' + Config.API_KEY
    with urllib.request.urlopen(get_news_source_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)

        news_source_results = None

        if get_news_source_response['sources']:
            news_source_results_list = get_news_source_response['sources']
            news_source_results = process_sources(news_source_results_list)

    return news_source_results


def process_sources(source_list):
    '''
    function that process the news articles and transform them to a list of objects
    '''
    news_source_result = []
    for news_source_item in source_list:
        name = news_source_item.get('name')
        description = news_source_item.get('description')
        url = news_source_item.get('url')

        if name:
            news_source_object = Sources(name, description, url)
            news_source_result.append(news_source_object)
    return news_source_result
