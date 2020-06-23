class DevConfig:
    ENV = 'development'
    DEBUG = True
    DEBUG_TB_ENABLED = True  # Disable Debug toolbar
    HOST = '0.0.0.0'
    TEMPLATES_AUTO_RELOAD = True
    # JWT Config
    JWT_SECRET_KEY = 'Khanh'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    # mysql
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SCHEDULER_API_ENABLED = False
