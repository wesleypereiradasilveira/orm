

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine
from pathlib import Path
from typing import Optional
from dotenv import dotenv_values
from models.model_base import ModelBase

__engine: Optional[Engine] = None
secrets = dotenv_values(".env")

def create_engine(sqlite: bool = False) -> Engine:
    global __engine

    if __engine:
        return
    
    if sqlite:
        db_file = "db/popsicles.sqlite"
        folder = Path(db_file).parent
        folder.mkdir(parents=True, exist_ok=True)

        connection_string = f"sqlite:///{db_file}"
        __engine = sa.create_engine(url=connection_string, echo=False, connect_args={"check_same_thread": False})
    else:
        db_user = str(secrets["POSTGRES_USER"])
        db_password = str(secrets["POSTGRES_PASSWORD"])
        db_port = int(secrets["POSTGRES_PORT"])
        connection_string = f"postgresql://{db_user}:{db_password}@localhost:{db_port}/popsicles"
        __engine = sa.create_engine(url=connection_string, echo=False)

    return __engine

def create_session(sqlite: bool = False) -> Session:
    global __engine

    if not __engine:
        create_engine(sqlite)

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    session: Session = __session()

    return session

def create_tables(sqlite: bool = False) -> None:
    global __engine

    if not __engine:
        create_engine(sqlite)

    import models.__all_models
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)
