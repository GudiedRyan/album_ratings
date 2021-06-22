from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from album_ratings.config import DevelopmentConfig

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    Bootstrap(app)

    from album_ratings.albums.routes import albums
    app.register_blueprint(albums)

    return app
