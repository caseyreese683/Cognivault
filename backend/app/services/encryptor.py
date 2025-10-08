from Crypto.Cipher import AES
import base64, os

class Encryptor:
    def __init__(self, key: bytes):
        self.key = key

    def encrypt(self, data: str) -> str:
        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data.encode())
        return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

    def decrypt(self, encrypted: str) -> str:
        raw = base64.b64decode(encrypted)
        nonce, tag, ciphertext = raw[:16], raw[16:32], raw[32:]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce)
        return cipher.decrypt_and_verify(ciphertext, tag).decode()
