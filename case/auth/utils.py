from database import obter_sessao
from models.user import User

def load_user(user_id):
    session = obter_sessao()
    user = session.get(User, int(user_id))  # forma moderna (SQLAlchemy 2.0+)
    session.close()
    return user