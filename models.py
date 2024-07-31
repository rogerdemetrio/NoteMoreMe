from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///banconmm.db"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Tabela Produto
class Notas(Base):
    __tablename__ = "tbnota"
    id = Column(Integer, primary_key=True)
    titulo_texto = Column(VARCHAR)
    texto = Column(VARCHAR)

Base.metadata.create_all(engine)
