from app.app import create_app

from setting import DevConfig

app = create_app(DevConfig)

app.run(port=5012, debug=True)
#
# '''
#     Class.query.filter(condition) ex: Class.attr > 0
#     Class.query.filter_by(attr=value)
#     Class.query.get(id)
#     Class.query.order_by(Class.attr)
#     Class.query.all()
# '''
# from sqlalchemy import inspect
#
#
# def object_as_dict(obj):
#     return {c.key: getattr(obj, c.key)
#             for c in inspect(obj).mapper.column_attrs}
#
# object_as_dict()

# class A:
#     x=1
#
# a=A()
# b=A()
# c=A()
#
# A.x=10
# A.x+=1
#
# print(a.x)
# print(b.x)
# print(c.x)
#
# a.x+=1
# c.x=20
# A.x=100
#
# print(a.x)
# print(b.x)
# print(c.x)