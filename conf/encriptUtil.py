import os
import random
import string

def generate_readable_key_iv(length=16):
    """
    Gera key e IV com caracteres legíveis (A-Z, a-z, 0-9), com o tamanho correto para AES.
    """
    chars = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    key = ''.join(random.choices(chars, k=length)).encode('utf-8')
    iv = ''.join(random.choices(chars, k=length)).encode('utf-8')
    return key, iv


key, iv = generate_readable_key_iv()

print(key)
print(iv)