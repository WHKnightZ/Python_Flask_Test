# from extensions import db
#
#
# class Group(db.Model):
#     __tablename__ = 'groups'
#
#     id = db.Column(db.String(50), primary_key=True)
#     name = db.Column(db.ForeignKey('users.id'), nullable=False, index=True)
#     content = db.Column(db.String(200), nullable=False)
#
#     @staticmethod
#     def get_all():
#         return Post.query.all()
#
#     @staticmethod
#     def get_by_id(_id):
#         return Post.query.get(_id)
