import base64
import Crypto.Util.Padding as padding
from Crypto.Cipher import AES
from Crypto.Protocol import KDF
from pbkdf2 import PBKDF2
from Crypto.Protocol.KDF import PBKDF2

# data = "UE0YJoHoJSiaBo6DRBqqxT0qq/LvJT9XXX7YHEN/40X3HuKHTBqMfAfE2q7/aOWpiqqIjaw+ZaIQArZ8JTRKioiNswDz4YNzi6s8wpWuX0RZOWa31hxX6+ggfAUfZZAbRkM5/yiksVmTSJz1qzIm5C4xFjxLvu3jxarmVt3Xv+N3pW4rppbne/6QkDoyJc/do/alYhivpDlrucBvB3gTFa8U5X4oLuURizCoA/I8f7kFhTbjeRh2QcUYr2R6RCYlpX/QcJXt3La9jF7gj53Ntg=="
# key = 'jahernoticelivecredentials'
# enc_txt = base64.b64decode(data)
# salt_t = ["0x49", "0x76", "0x61", "0x6e", "0x20", "0x4d", "0x65", "0x64", "0x76", "0x65", "0x64", "0x65", "0x76"]
# salt = bytes([int(x, 0) for x in salt_t])
# key_bytes = KDF.PBKDF2(key, salt, 32, 1000)
# iv = KDF.PBKDF2(key, salt, 48, 1000)[32:48]
# cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
# decryptedPadded = cipher.decrypt(enc_txt)
# decrypted = padding.unpad(decryptedPadded, 16)  # Pkcs7 unpadding
# text=decrypted.decode('utf-16')
# print(text)
 
plaintext = "Data Source=132.148.165.161,14251;Initial Catalog=jahernotice;User Id=esmsrvdb;Password=esmsys-2018;"
key = b'jahernoticelivecredentials'
# plaintext_bytes = plaintext.encode('utf-16')
# salt_t = ["0x49", "0x76", "0x61", "0x6e", "0x20", "0x4d", "0x65", "0x64", "0x76", "0x65", "0x64", "0x65", "0x76"]
# salt = bytes([int(x, 0) for x in salt_t])
# key_bytes_1 = KDF.PBKDF2(key, salt, 48, 1000)
# iv_1 = KDF.PBKDF2(key, salt, 64, 1000)[16:48]
# cipher_1 = AES.new(key_bytes_1, AES.MODE_CBC, iv_1)
# padded_text = padding.pad(plaintext.encode('utf-8'), 32)  # Pkcs7 padding
# encrypted = cipher_1.encrypt(padded_text)
# encoded_encrypted = base64.b64encode(encrypted)
# cipher_1 = AES.new(key_bytes_1, AES.MODE_CBC, iv_1)
# # # Encode the encrypted bytes to base64
# padded_plaintext = padding.pad(plaintext_bytes, 64)
# encrypted_bytes_1 = cipher_1.encrypt(padded_plaintext)
# encrypted_base64_1 = base64.b64encode(encrypted_bytes_1).decode('utf-8')
# print(encrypted_base64_1,"enc")
# text_1 = encrypted_base64_1.decode('utf-8')
# print("Encrypted Data:", encoded_encrypted)
# plaintext = "Hello, World!"
# key = b'jahernoticelivecredentials'
salt = b'\x49\x76\x61\x6e\x20\x4d\x65\x64\x76\x65\x64\x65\x76'
iv = PBKDF2(key, salt, 16, 1000)[:16]  # Derive the IV using PBKDF2
# Create the AES cipher object
cipher = AES.new(key, AES.MODE_CBC, iv)
# Apply PKCS#7 padding to the plaintext
padding_length = AES.block_size - (len(plaintext) % AES.block_size)
padded_plaintext = plaintext + chr(padding_length) * padding_length
# Encrypt the padded plaintext
cipher_text = cipher.encrypt(padded_plaintext)
# Convert the cipher text to base64
cipher_text_base64 = base64.b64encode(cipher_text).decode('utf-8')
# Print the cipher text
print(cipher_text_base64)