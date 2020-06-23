from flask import Blueprint, request

from datetime import timedelta
from models.user import User

from flask_jwt_extended import (
    jwt_required, create_access_token,
    jwt_refresh_token_required, get_jwt_identity,
    create_refresh_token, get_raw_jwt
)

from schema.schema_model import user_schema

api = Blueprint("auth", __name__)

ACCESS_EXPIRES = timedelta(days=1)
REFRESH_EXPIRES = timedelta(days=90)


@api.route('login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", None)
    password = data.get("password", None)
    if not username or not password:
        return {"message": "Please enter username and password"}

    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
        access_token = create_access_token(identity=user.id, expires_delta=ACCESS_EXPIRES)
        refresh_token = create_refresh_token(identity=user.id, expires_delta=REFRESH_EXPIRES)
        return {"access_token": access_token, "refresh_token": refresh_token, "user": user_schema.dump(user)}
    else:
        return {"message": "Wrong username or password"}


@api.route('logout', methods=['POST'])
@jwt_required
def logout():
    pass


@api.route('refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    pass
