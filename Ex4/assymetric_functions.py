from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


clear_text = "Ala ma kota".encode()
private_key = rsa.generate_private_key(65537, 2048)
public_key = private_key.public_key()  


def encryptText(clear_text, public_key):
    encrypted_text = public_key.encrypt(clear_text, padding.OAEP(
        padding.MGF1(hashes.SHA256()),
        hashes.SHA256(),
        None))
    return encrypted_text.hex()


def decryptText(encrypted_text, private_key):
    decrypted_text = private_key.decrypt(encrypted_text, padding.OAEP(
        padding.MGF1(hashes.SHA256()),
        hashes.SHA256(),
        None))
    return decrypted_text.decode()


a = encryptText("pizza")
print(a)



# encryption_data = {
    #     "encrypted_text": encrypted_text.hex(), 
    #     "private_key": private_key,
    #     "public_key": public_key
    # }