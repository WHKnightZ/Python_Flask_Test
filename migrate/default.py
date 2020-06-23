import json
from app.app import create_app
from extensions import db
from models import User

from setting import DevConfig

class MigrateDatabase:
    def __init__(self):
        app = create_app(config_object=DevConfig)
        app_context = app.app_context()
        app_context.push()
        db.drop_all()  # drop all tables
        db.create_all()  # create a new schema
        with open('default.json') as file:
            self.default_data = json.load(file)

    def create_default_users(self):
        users = self.default_data.get('users', {})
        for item in users:
            instance = User()
            for key in item.keys():
                instance.__setattr__(key, item[key])
            db.session.add(instance)

        db.session.commit()


if __name__ == '__main__':
    worker = MigrateDatabase()
    worker.create_default_users()