from flask import Flask

import api

from extensions import db, jwt, ma

from setting import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

jwt.init_app(app)
db.init_app(app)
ma.init_app(app)

@jwt.token_in_blacklist_loader
def check_if_token_is_revoked(decrypted_token):
    return False

app.register_blueprint(api.auth.api, url_prefix="/api/auth")
app.register_blueprint(api.users.api, url_prefix="/api/users")

app.run(port=8080)
