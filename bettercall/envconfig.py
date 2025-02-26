from flask import Flask

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'super_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///production.db'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'

app = Flask(__name__)

# Choose the appropriate configuration based on the environment
if app.env == 'development':
    app.config.from_object(DevelopmentConfig)
elif app.env == 'testing':
    app.config.from_object(TestingConfig)
else:
    app.config.from_object(Config)

if __name__ == '__main__':
    app.run()
