import os

class Config:
    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?category={}&language=en&apiKey=525ae38a499a41b78c74314ee571668b'

    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&language=en&apiKey=525ae38a499a41b78c74314ee571668b'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

    SECRET_KEY = os.environ.get('SECRET_KEY')




class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
