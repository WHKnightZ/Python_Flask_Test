from extensions import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False, index=True)
    content = db.Column(db.String(200), nullable=False)

    user = db.relationship('User', primaryjoin='Post.user_id == User.id', backref='posts')

    @staticmethod
    def get_all():
        return Post.query.all()

    @staticmethod
    def get_by_id(_id):
        return Post.query.get(_id)
