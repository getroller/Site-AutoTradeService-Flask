from flask import Config, Flask
from flask_mailman import Mail
from .extensions import db
from .config import Config
from .routes.user import user
from .routes.post import post
from .routes.main import main
from .routes.japan import japan
from .routes.korea import korea
from .routes.china import china
from .routes.about import about


mail = Mail()

def create_app (config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    mail.init_app(app)

    app.register_blueprint(user)
    app.register_blueprint(post)
    app.register_blueprint(main)
    app.register_blueprint(japan)
    app.register_blueprint(korea)
    app.register_blueprint(china)
    app.register_blueprint(about)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app