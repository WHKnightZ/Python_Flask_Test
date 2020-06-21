from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, "Khanh", "123456"),
    User(2, "Chan", "123")
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identify(payload):
    user_id = payload["identify"]
    return userid_mapping.get(user_id, None)
