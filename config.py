import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '4q&{qYHLX5<yy?'
    LANGUAGES = ['en', 'nl']
