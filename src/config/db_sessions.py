import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine
from src.models.model_base import ModelBase
import os

__engine: Optional[Engine] = None

def create_engine(sqlite: bool = False) -> Engine:
    """
        Cria Engine de conexão com a base de dados.
    """
    global __engine

    if __engine:
        return
    
    if sqlite:
        arquivo_db = 'data/database.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)

        conn_str = f'sqlite:///{arquivo_db}'
        __engine = sa.create_engine(url=conn_str, echo=False, connect_args={"check_same_thread":False})
        if not Path(arquivo_db).exists():
            create_tables()
    
    else:
        conn_str = f'postgresql://{os.environ["USERPG"]}:{os.environ["PASSPG"]}@{os.environ["HOST"]}:{os.environ["PORT"]}/{os.environ["DATABASE"]}'

        __engine = sa.create_engine(url=conn_str, echo=False)

def create_session() -> Session:
    """
        Cria session de conexão com a base de dados.
    """
    
    global __engine

    if not __engine:
        create_engine(sqlite=True)
        
    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session: Session = __session()

    return session



def create_tables() -> None:
    """
    Criar tabelas.
    """

    global __engine

    if not __engine:
        create_engine(sqlite=True)

    from src.models import __all__models
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)
