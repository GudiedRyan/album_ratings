from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from album_ratings.config import DevelopmentConfig

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    from album_ratings.main.routes import main
    app.register_blueprint(main)

    from album_ratings.albums.routes import albums
    app.register_blueprint(albums)

    return app