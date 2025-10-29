
from flask import Flask
from config import Config
from extensions import init_extensions, login_manager
from auth.routes import auth_bp
from controllers.user_controller import user_bp
from controllers.produtos_controller import produto_bp
from models import Base
from database import engine

app = Flask(__name__, template_folder='views')


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    init_extensions(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(produto_bp)

    from auth.utils import load_user
    login_manager.user_loader(load_user) 
    
    with app.app_context():
        Base.metadata.create_all(bind=engine)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)