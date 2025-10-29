from . import Base
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Column, Integer, String, Table
from case.database import obter_sessao
from werkzeug.security import generate_password_hash

class User(Base, UserMixin):
    __tablename__ = 'tb_usuarios'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(200), nullable=False)
    produtos: Mapped[list["Pro  duto"]] = relationship(back_populates='user', cascade='all, delete-orphan') # type: ignore


    def __repr__(self):
        return f'<Usuario {self.email}>'

    @classmethod
    def all(cls):
        session = obter_sessao()
        usuarios = session.query(cls).all()
        session.close()
        return usuarios
    
    def save(self): 
        session = obter_sessao()
    
def save(self):
    session = obter_sessao()

    existente = session.query(User).filter_by(email=self.email).first()
    if existente:
        session.close()
        return None  # Já existe

    # Cria novo usuário
    session.add(self)
    session.commit()
    session.close()
    return True