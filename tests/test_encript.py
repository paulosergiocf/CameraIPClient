import pytest
from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.hazmat.primitives import padding
from src.util.encript import Encript

def test_encrypt_decrypt_AES_CBC_valid_input(): 
    data = "Test data"

    ciphertext = Encript.encrypt_AES_CBC(data)
    decrypted_data = Encript.decrypt_AES_CBC(ciphertext)

    assert decrypted_data == data



def test_encrypt_AES_CBC_padding():
    data = "Test"

    ciphertext = Encript.encrypt_AES_CBC(data)

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data.encode('utf-8')) + padder.finalize()

    assert len(ciphertext) == len(padded_data)