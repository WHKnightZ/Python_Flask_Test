from flask import Flask

import api

from extensions import db, jwt, ma

from setting import DevConfig


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)


def register_blueprints(app):
    app.register_blueprint(api.auth.api, url_prefix="/api/auth")
    app.register_blueprint(api.users.api, url_prefix="/api/users")
    app.register_blueprint(api.posts.api, url_prefix="/api/posts")
    app.register_blueprint(api.utils.api, url_prefix="/api/utils")
