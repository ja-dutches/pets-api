from flask import Flask

from pets_api.extensions import db
from pets_api.home.views import home_app
from pets_api.pet.views import pet_app


def create_app(**config_overrides):
    """
    Create a Flask application using the app factory pattern.
    :return: Flask app
    """

    app = Flask(__name__, instance_relative_config=True)
    # Load config
    app.config.from_object('config.settings')

    # apply overrides for tests
    app.config.update(config_overrides)

    # register blueprints
    app.register_blueprint(home_app)
    app.register_blueprint(pet_app)

    # initialize extensions
    extensions(app)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).
    :param app: Flask application instance
    :return: None
    """
    db.init_app(app)

    return None
