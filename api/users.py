import uuid

from flask import Blueprint, request

from extensions import db
from models.user import User
from schema.schema_model import user_schema, users_schema

from flask_jwt_extended import (
    jwt_required, create_access_token,
    jwt_refresh_token_required, get_jwt_identity,
    create_refresh_token, get_raw_jwt
)

api = Blueprint("users", __name__)


@api.route('', methods=['GET'])
@jwt_required
def get_all_users():
    user = User.get_all()
    user = users_schema.dump(user)
    return {"users": user}


@api.route('/<_id>', methods=['GET'])
@jwt_required
def get_user_by_id(_id):
    user = User.get_by_id(_id)
    if not user:
        return {"message": "User not found"}
    user = user_schema.dump(user)
    return {"user": user}


@api.route('', methods=['POST'])
@jwt_required
def create_user():
    data = request.get_json()
    username = data.get("username", None)
    password = data.get("password", None)
    if not username or not password:
        return {"message": "Please enter username and password"}

    user = User.query.filter_by(username=username).first()

    if user:
        return {"message": "Username is existed"}
    else:
        _id = uuid.uuid1()
        user = User(id=_id, username=username, password=password)
        db.session.add(user)
        db.session.commit()
        user = user_schema.dump(user)
        return {"message": "Success", "user": user}


@api.route('/<_id>', methods=['PUT'])
@jwt_required
def update_user(_id):
    user = User.get_by_id(_id)
    if not user:
        return {"message": "User not found"}
    data = request.get_json()

    password = data.get("password", None)
    user.password = password

    db.session.commit()
    user = user_schema.dump(user)
    return {"message": "Success", "user": user}


@api.route('/<_id>', methods=['DELETE'])
@jwt_required
def delete_user(_id):
    user = User.get_by_id(_id)
    if not user:
        return {"message": "User not found"}

    db.session.delete(user)
    db.session.commit()
    user = user_schema.dump(user)
    return {"message": "Success", "user": user}
