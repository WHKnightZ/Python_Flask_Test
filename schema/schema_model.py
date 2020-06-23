from extensions import ma
from models.user import User
#
# class UserSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'username', 'password')

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

user_schema = UserSchema()
users_schema = UserSchema(many=True)
