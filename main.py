from app.app import create_app

from setting import DevConfig

app = create_app(DevConfig)

app.run(port=8080, debug=True)
