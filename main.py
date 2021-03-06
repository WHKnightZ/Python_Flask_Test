from app.app import create_app

from setting import DevConfig
from flask_cors import CORS

# from migrate.default import create_db

app = create_app(DevConfig)
CORS(app)

# @app.before_first_request
# def db_init():
#     create_db()


if __name__ == "__main__":
    app.run(port=5012)

'''
    Class.query.filter(condition) ex: Class.attr > 0
    Class.query.filter_by(attr=value)
    Class.query.get(id)
    Class.query.order_by(Class.attr)
    Class.query.all()
'''
