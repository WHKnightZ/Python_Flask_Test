from app.app import create_app

from setting import DevConfig

app = create_app(DevConfig)

app.run(port=5012, debug=True)

'''
    Class.query.filter(condition) ex: Class.attr > 0
    Class.query.filter_by(attr=value)
    Class.query.get(id)
    Class.query.order_by(Class.attr)
    Class.query.all()
'''