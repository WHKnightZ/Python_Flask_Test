import json

from flask_testing import TestCase

from app.app import create_app
from extensions import db
from models import User
from setting import TestConfig


class BaseTestCase(TestCase):

    def create_app(self):
        app = create_app(config_object=TestConfig)
        return app

    def setUp(self):
        db.drop_all()
        db.create_all()

        with open('migrate/default.json') as file:
            default_data = json.load(file)

        users = default_data.get('users', {})
        for item in users:
            instance = User()
            for key in item.keys():
                instance.__setattr__(key, item[key])
            db.session.add(instance)

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
