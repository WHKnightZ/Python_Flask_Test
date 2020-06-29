import json
from app.app import create_app
from extensions import db
from models import User, Post

from setting import ProdConfig


class MigrateDatabase:
    def __init__(self):
        app = create_app(config_object=ProdConfig)
        app_context = app.app_context()
        app_context.push()
        db.drop_all()  # drop all tables
        db.create_all()  # create a new schema
        with open('migrate/default.json') as file:
            self.default_data = json.load(file)

    def create_default_users(self):
        users = self.default_data.get('users', {})
        for item in users:
            instance = User()
            for key in item.keys():
                instance.__setattr__(key, item[key])
            db.session.add(instance)

        db.session.commit()

    def create_default_posts(self):
        posts = self.default_data.get('posts', {})
        for item in posts:
            instance = Post()
            for key in item.keys():
                instance.__setattr__(key, item[key])
            db.session.add(instance)

        db.session.commit()

def create_db():
    worker = MigrateDatabase()
    worker.create_default_users()
    worker.create_default_posts()
