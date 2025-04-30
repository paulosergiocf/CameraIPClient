import sqlalchemy as sa
from datetime import datetime
from src.models.model_base import ModelBase

class Device(ModelBase):
    __tablename__: str = 'devices'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    creation_date: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    name_devide: str = sa.Column(sa.String(45), unique=True, nullable=False)
    host: str = sa.Column(sa.String(45), unique=False, nullable=False)
    port: int = sa.Column(sa.Integer, unique=False, nullable=False)
    username: str = sa.Column(sa.String(45), unique=False, nullable=False)
    password: str = sa.Column(sa.String(250), unique=False, nullable=False)

    def __repr__(self):
        return f"<Device: {self.nome}>"
