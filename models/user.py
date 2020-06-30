from extensions import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    # id_group = db.relationship('Group', primaryjoin='User.user_id == User.id', backref='posts')

    @staticmethod
    def get_all():
        return User.query.order_by(User.username).all()

    @staticmethod
    def get_by_id(_id):
        return User.query.get(_id)
