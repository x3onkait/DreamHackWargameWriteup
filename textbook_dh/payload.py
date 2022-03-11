from Crypto.Cipher import AES
import hashlib
from Crypto.Util.Padding import unpad

prime = b"dd7ec16da4376b1f0ef97e69b2f7f544d8d62c53ca3291058c1ad9dcf7ce0b53fd89bd034337095c78d6dd133721ccaae56b542a06cbdc61407d3f76f00d38d94c72611da709a0df3929b41d850b05f63c46e793ddb3afc38d71e59024346c4dfd07a76e728163b91ff6d15ef6edf924fcb9878b8ac94ffaea6f01df296dd48b"
AESKEY = hashlib.md5(str("1").encode()).digest()

cipher = AES.new(AESKEY, AES.MODE_ECB)

aliceEncryptedData = b"e48e9174a9103e249f4bb809e13d58d49283e2438954799030be4854328adacbeb310c79bce3e91719f218158359af0d"
bobEncryptedData = b"2a69648d494907e551b69b74676f2e528644a526e5f7bc8b6300f1bd8ad5f091a9e40939960ea5bd0ad2ceff23a14f96"

FLAG = unpad(cipher.decrypt(bytes.fromhex(aliceEncryptedData.decode())), 16)
FLAG += unpad(cipher.decrypt(bytes.fromhex(bobEncryptedData.decode())), 16)

print(f"FLAG : {FLAG}")
