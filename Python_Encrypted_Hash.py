# # # # -*- coding: utf-8 -*-
# Reference: http://security.stackexchange.com/questions/18290/is-sha-1-hash-always-the-same
# Hash functions are deterministic: same input yields the same output.
# Any implementation of a given hash function, regardless of the language it is implemented in, must act the same.
# However, note that hash functions take sequences of bits as input.
# When we "hash a string", we actually convert a sequence of characters into a sequence of bits, and then hash it.

# http://www.laurentluce.com/posts/python-and-cryptography-with-pycrypto/
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):
    """
    A classical AES Cipher. Can use any size of data and any size of password thanks to padding.
    Also ensure the coherence and the type of the data with a unicode to byte converter.
    """
    def __init__(self, key):
        self.bs = 32 # Block_size is setup to 32
        self.key = hashlib.sha256(AESCipher.str_to_bytes(key)).digest()

    @staticmethod
    def str_to_bytes(data):
        u_type = type(b''.decode('utf8'))
        if isinstance(data, u_type):
            return data.encode('utf8')
        return data

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * AESCipher.str_to_bytes(chr(self.bs - len(s) % self.bs))

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    def encrypt(self, raw):
        raw = self._pad(AESCipher.str_to_bytes(raw))
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw)).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

if __name__ == '__main__':

    cipher = AESCipher(key='mykey') # key can be string with any length
    text = 'test'
    encrypted = cipher.encrypt("Hello World")
    print(encrypted)
    decrypted = cipher.decrypt(encrypted)
    print(decrypted)