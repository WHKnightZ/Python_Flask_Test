# from apscheduler.triggers import interval
from flask import Flask

import api

from extensions import db, jwt, ma, scheduler
# from scheduler_task.revoke_token import remove_token_expiry
from models import User, Post

from setting import DevConfig


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app, config_object)
    register_blueprints(app)
    return app


def register_extensions(app, config_object):
    db.app = app
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    print(User.query.join(Post).all())

    # if config_object.ENV != 'test':
    #     trigger = interval.IntervalTrigger(seconds=5)
    #     scheduler.add_job(remove_token_expiry, trigger=trigger, id='remove_token_expiry', replace_existing=True)
    #     scheduler.start()


def register_blueprints(app):
    app.register_blueprint(api.auth.api, url_prefix="/api/auth")
    app.register_blueprint(api.users.api, url_prefix="/api/users")
    app.register_blueprint(api.posts.api, url_prefix="/api/posts")
    app.register_blueprint(api.utils.api, url_prefix="/api/utils")
