from . import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float
from database import obter_sessao

class Produto(Base):
    __tablename__ = 'tb_produtos'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(80), nullable=False)
    descricao: Mapped[str] = mapped_column(String(200))
    preco: Mapped[float] = mapped_column(Float, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("tb_usuarios.id"))
    user: Mapped["User"] = relationship(back_populates="produtos") # type: ignore


    def __repr__(self):
        return f'<Produto {self.nome}, ID: {self.id}>'

    @classmethod
    def all(cls):
        session = obter_sessao()
        produtos = session.query(cls).all()
        session.close()
        return produtos
    
    def save(self):
        session = obter_sessao()
        session.add(self)
        session.commit()
        return self
    
    @classmethod
    def get(cls, id):
        session = obter_sessao()
        produto = session.get(cls, id)  
        session.close()
        return produto