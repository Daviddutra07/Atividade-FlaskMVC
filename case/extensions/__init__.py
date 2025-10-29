from flask_login import LoginManager
from auth.utils import load_user  

login_manager = LoginManager()
login_manager.login_view = "auth.login"


login_manager.user_loader(load_user)

def init_extensions(app):
    """
    Inicializa as extensões do Flask (no caso, apenas o Flask-Login).
    """
    login_manager.init_app(app)