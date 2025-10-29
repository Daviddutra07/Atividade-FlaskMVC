from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///banco.db')
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False) #Cria seções temporárias para fazer alterações, para cada usuário  

def obter_sessao():
    return SessionLocal()