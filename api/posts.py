from flask import Blueprint

from models import Post
from schema.schema_model import posts_schema

api = Blueprint("posts", __name__)


@api.route('', methods=['GET'])
def get_all_posts():
    posts = Post.get_all()
    posts = posts_schema.dump(posts)
    return {"posts": posts}
