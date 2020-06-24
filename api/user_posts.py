from flask import Blueprint

from extensions import db
from models import Post, User
from schema.schema_model import posts_schema

api = Blueprint("user_posts", __name__)


@api.route('<user_id>/posts', methods=['GET'])
def get_all_posts_by_user(user_id):
    posts = Post.query.filter_by(user_id=user_id).all()

    user_id = "a74dd5a8-9369-11ea-afb4-00e04d380507"
    print(Post.query.filter(Post.user_id == user_id).all())
    print(Post.query.filter_by(user_id=user_id).all())

    list = db.session.query(Post).join(User).filter_by(username="Khanh").all()
    print(list)

    posts = posts_schema.dump(posts)
    return {"posts": posts}
