from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from BookProject.config import Config



bcrypt = Bcrypt()
login = LoginManager()
db = SQLAlchemy()
login.login_view="user.login"

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)
    bcrypt.init_app(app)
    login.init_app(app)
    db.init_app(app)

    from BookProject.main.routes import main
    from BookProject.errors.handlers import error
    from BookProject.book.routes import books
    from BookProject.user.routes import user
    from BookProject.api.routes import apis

    app.register_blueprint(main)
    app.register_blueprint(error)
    app.register_blueprint(books)
    app.register_blueprint(user)
    app.register_blueprint(apis)

    return app