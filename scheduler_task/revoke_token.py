from models import TokenBlacklist
from extensions import db


def remove_token_expiry():
    with db.app.app_context():
        TokenBlacklist.prune_database()
