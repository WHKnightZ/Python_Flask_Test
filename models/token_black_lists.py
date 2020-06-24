from flask_jwt_extended import decode_token

from extensions import db

class TokenBlacklist(db.Model):
    __tablename__ = 'token_blacklist'

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    token_type = db.Column(db.String(10), nullable=False)
    user_identity = db.Column(db.String(50), nullable=False)
    revoked = db.Column(db.Boolean, nullable=False)
    expires = db.Column(db.Integer, nullable=False)

    @staticmethod
    def add_token_to_database(encoded_token, user_identity):
        decoded_token = decode_token(encoded_token)
        jti = decoded_token['jti']
        token_type = decoded_token['type']
        expires = decoded_token['exp']
        revoked = False

        db_token = TokenBlacklist(
            jti=jti,
            token_type=token_type,
            user_identity=user_identity,
            expires=expires,
            revoked=revoked,
        )
        db.session.add(db_token)
        db.session.commit()

    @staticmethod
    def is_token_revoked(decoded_token):
        jti = decoded_token['jti']
        try:
            token = TokenBlacklist.query.filter_by(jti=jti).one()
            return token.revoked
        except Exception:
            return True

    @staticmethod
    def revoke_token(jti):
        try:
            token = TokenBlacklist.query.filter_by(jti=jti).first()
            token.revoked = True
            db.session.commit()
        except Exception as ex:
            return {"message": "Error"}

    @staticmethod
    def revoke_all_token(users_identity):
        try:
            if type(users_identity) is not list:
                users_identity = [users_identity]
            tokens = TokenBlacklist.query.filter(TokenBlacklist.user_identity.in_(users_identity),
                                                 TokenBlacklist.revoked == False).all()
            for token in tokens:
                token.revoked = True
            db.session.commit()
        except Exception:
            return {"message": "Could not find the user"}

    @staticmethod
    def unrevoke_token(jti):
        try:
            token = TokenBlacklist.query.filter_by(jti=jti).one()
            token.revoked = False
            db.session.commit()
        except Exception:
            return {"message": "Could not find the token"}

    # @staticmethod
    # def prune_database():
    #     now_in_seconds = get_datetime_now_s()
    #     expired = TokenBlacklist.query.filter(TokenBlacklist.expires < now_in_seconds).all()
    #     for token in expired:
    #         db.session.delete(token)
    #     db.session.commit()
