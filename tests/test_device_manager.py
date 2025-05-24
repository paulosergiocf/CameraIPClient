import pytest
from src.models.manager.device_manager import DeviceManager
from src.models.devices import Device

def test_get_string_connection():
    # Arrange
    device = Device(
        host="192.168.1.1",
        port=554,
        username="admin",
        password="password"
    )
    device_manager = DeviceManager(device)

    # Act
    string_connection = device_manager._DeviceManager__get_string_connection()

    # Assert
    expected_connection = "rtsp://192.168.1.1:554/user=admin&password=password&channel=1&stream=0"
    assert string_connection == expected_connection
