from flask import Blueprint, request

from datetime import timedelta
from models import User, TokenBlacklist
from extensions import jwt

from flask_jwt_extended import (
    jwt_required, create_access_token,
    jwt_refresh_token_required, get_jwt_identity,
    create_refresh_token, get_raw_jwt, decode_token
)

from schema.schema_model import user_schema
from utils import get_datetime_now_s

api = Blueprint("auth", __name__)

ACCESS_EXPIRES = timedelta(seconds=1)
REFRESH_EXPIRES = timedelta(seconds=1)


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
        print(get_datetime_now_s())
        decoded_token = decode_token(access_token)
        print(decoded_token['exp'])
        TokenBlacklist.add_token_to_database(access_token, user.id)
        TokenBlacklist.add_token_to_database(refresh_token, user.id)
        return {"access_token": access_token, "refresh_token": refresh_token, "user": user_schema.dump(user)}
    else:
        return {"message": "Wrong username or password"}


@api.route('logout', methods=['POST'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    TokenBlacklist.revoke_token(jti)
    return {"message": "Logout success"}


@api.route('refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    user_id = get_jwt_identity()
    if not user_id:
        return {"message": "User not exists"}
    access_token = create_access_token(identity=user_id, expires_delta=ACCESS_EXPIRES)
    refresh_token = create_refresh_token(identity=user_id, expires_delta=REFRESH_EXPIRES)
    TokenBlacklist.add_token_to_database(access_token, user_id)
    TokenBlacklist.add_token_to_database(refresh_token, user_id)
    return {"access_token": access_token, "refresh_token": refresh_token}


@jwt.token_in_blacklist_loader
def check_if_token_is_revoked(decrypted_token):
    return TokenBlacklist.is_token_revoked(decrypted_token)
