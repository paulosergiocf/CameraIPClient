from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from src.util.convencions import Contants

class Encript():
    @staticmethod
    def encrypt_AES_CBC(data):
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data.encode('utf-8'))
        padded_data += padder.finalize()

        cipher = Cipher(algorithms.AES(Contants.KEY.value), modes.CBC(Contants.VETOR.value), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return ciphertext

    @staticmethod
    def decrypt_AES_CBC(ciphertext):
        decryptor = Cipher(algorithms.AES(Contants.KEY.value), modes.CBC(Contants.VETOR.value), backend=default_backend()).decryptor()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        unpadded_data = unpadder.update(decrypted_data)
        unpadded_data += unpadder.finalize()
        return unpadded_data.decode('utf-8')

