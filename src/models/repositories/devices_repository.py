from src.config.db_sessions import create_session
from src.models.devices import Device

class DeviceRepository:

    @staticmethod
    def get_by_id( device_id: int) -> Device:
        with create_session() as session:
            return session.query(Device).where(Device.id == device_id).one_or_none()

    @staticmethod
    def get_all() -> list[Device]:
        with create_session() as session:
            return session.query(Device).all()
    
    @staticmethod
    def create_device(name_device: str, host: str, port: int, username: str, password: str) -> Device:
        device: Device = Device(name_device=name_device, host=host, port=port, username=username, password=password)
        with create_session() as session:
            session.add(device)
            session.commit()
        
        return device
    
    @staticmethod
    def update_device(device_id: int, name_device: str, host: str, port: int, username: str, password: str) -> Device:

        with create_session() as session:
            device: Device = session.query(Device).where(Device.id == device_id).first()
            if device:                    
                device.name_device = name_device
                device.host = host
                device.port = port
                device.username = username
                device.password = password
                session.commit()

    @staticmethod
    def delete_device(device_id: int):
        with create_session() as session:
            device: Device = session.query(Device).where(Device.id == device_id).first()
            if device:
                session.delete(device)
                session.commit()
