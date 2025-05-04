import pytest
from datetime import datetime
from src.models.devices import Device
from src.models.model_base import ModelBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados para os testes
@pytest.fixture(scope="module")
def engine():
    return create_engine('sqlite:///:memory:')

@pytest.fixture(scope="module")
def setup_database(engine):
    ModelBase.metadata.create_all(engine)
    yield
    ModelBase.metadata.drop_all(engine)

@pytest.fixture
def session(engine, setup_database):
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
    session.close()

def test_device_creation(session):
    # Teste para criar uma instância de Device
    device = Device(
        name_device="Camera1",
        host="192.168.1.100",
        port=8080,
        username="admin",
        password="password123"
    )
    session.add(device)
    session.commit()

    # Consulta ao banco de dados para verificar se o dispositivo foi adicionado
    retrieved_device = session.query(Device).filter_by(name_device="Camera1").first()
    assert retrieved_device is not None
    assert retrieved_device.name_device == "Camera1"
    assert retrieved_device.host == "192.168.1.100"
    assert retrieved_device.port == 8080
    assert retrieved_device.username == "admin"
    assert retrieved_device.password == "password123"

def test_device_repr():
    # Teste do método __repr__
    device = Device(
        name_device="Camera2",
        host="192.168.1.101",
        port=9090,
        username="user",
        password="pass456"
    )
    assert repr(device) == "<Device: Camera2>"

def test_unique_name_device(session):
    # Teste para garantir que name_device seja único
    device1 = Device(
        name_device="Camera3",
        host="192.168.1.102",
        port=7070,
        username="admin",
        password="password789"
    )
    device2 = Device(
        name_device="Camera3",  # Nome duplicado
        host="192.168.1.103",
        port=6060,
        username="user",
        password="pass123"
    )
    session.add(device1)
    session.commit()

    session.add(device2)
    with pytest.raises(Exception):
        session.commit()
