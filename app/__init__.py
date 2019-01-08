from flask import Flask, request
from flask_babel import Babel, lazy_gettext as _l
from config import Config


app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.config.from_object(Config)

from app import routes
