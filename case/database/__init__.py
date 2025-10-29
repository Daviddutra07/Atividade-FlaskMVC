from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///banco.db')
SessionLocal = sessionmaker(bind=engine) #Cria seções temporárias para fazer alterações, para cada usuário  

def obter_sessao():
    return SessionLocal()