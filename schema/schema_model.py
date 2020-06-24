from extensions import ma
from models import User, Post


#
# class UserSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'username', 'password')

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post


post_schema = PostSchema()
posts_schema = PostSchema(many=True)
