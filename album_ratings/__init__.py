from flask import Flask
from album_ratings.config import DevelopmentConfig

def create_app():

    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    from album_ratings.main.routes import main
    app.register_blueprint(main)

    return app
