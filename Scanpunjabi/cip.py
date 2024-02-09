# import base64
# from Crypto.Cipher import AES
# from Crypto.Protocol.KDF import PBKDF2

 

# # Define the plaintext, key, IV, and salt
plaintext = "Data Source=132.148.165.161,14251;Initial Catalog=jahernotice;User Id=esmsrvdb;Password=esmsys-2018;"
# key = b'jahernoticelivecredentials'
# salt = b'\x49\x76\x61\x6e\x20\x4d\x65\x64\x76\x65\x64\x65\x76'
# iv = PBKDF2(key, salt, 16, 1000)[:16]  # Derive the IV using PBKDF2
# # Create the AES cipher object
# cipher = AES.new(key, AES.MODE_CBC, iv)
# # Apply PKCS#7 padding to the plaintext
# padding_length = 16 - (len(plaintext) % 16)
# padded_plaintext = plaintext + chr(padding_length) * padding_length
# # Encrypt the padded plaintext
# cipher_text = cipher.encrypt(padded_plaintext.encode('utf-8'))
# # Convert the cipher text to base64
# encoded_cipher_text = base64.b64encode(cipher_text).decode('utf-8')
# # Print the encoded cipher text
# print(encoded_cipher_text)

import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

 

# Define the plaintext, key, IV, and salt
# plaintext = "Your plaintext message"
passphrase = "jahernoticelivecredentials"
salt = b'\x49\x76\x61\x6e\x20\x4d\x65\x64\x76\x65\x64\x65\x76'
# iterations = 1000
# key = PBKDF2(passphrase, salt, dkLen=32, count=iterations)[:64]
# leng = print(len(key),"length")
# iv = PBKDF2(passphrase, salt, dkLen=16, count=iterations)[:16]
# print(len(iv),"ivlength")
# cipher = AES.new(key, AES.MODE_CBC, iv)
# padding_length = 64 - (len(plaintext) % 16)
# padding_length = 16 - (len(plaintext) % 16)
# plaintext += chr(padding_length)*padding_length
# plaintext = plaintext[:-plaintext[-1]]
# print(padding_length)
# padded_plaintext = plaintext + chr(length) * padding_length

 

# Encrypt the padded plaintext
# cipher_text = cipher.encrypt(plaintext.encode('utf-8'))
# Convert the cipher text to base64
# encoded_cipher_text = base64.b64encode(cipher_text).decode('utf-8')
# Print the encoded cipher text
# print(encoded_cipher_text)
_encryptionKey=passphrase.encode("utf-8")
key_bytes = PBKDF2(_encryptionKey, salt, dkLen=16)
session_key=key_bytes[:32]
iv= key_bytes[:16]
cipher = AES.new(session_key, AES.MODE_CBC, iv)
cipher_text = cipher.encrypt(plaintext.encode('utf-8'))
encoded_cipher_text = base64.b64encode(cipher_text).decode('utf-8')
print(encoded_cipher_text)