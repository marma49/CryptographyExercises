from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


clear_text = "Ala ma kota".encode()
private_key = rsa.generate_private_key(65537, 2048)
public_key = private_key.public_key()  

def readPrivateKey(private_key):
    pem = private_key.private_bytes(
        serialization.Encoding.PEM, 
        serialization.PrivateFormat.TraditionalOpenSSL, 
        serialization.NoEncryption()
    )
    pem = pem.decode().splitlines()[1:-1]
    return pem


def readPublicKey():
    pub_pem = private_key.public_key().public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo
    )

    pub_pem = pub_pem.decode().splitlines()[1:-1]
    return pub_pem

def encryptText(clear_text, public_key):
    encrypted_text = public_key.encrypt(clear_text.encode(), padding.OAEP(
        padding.MGF1(hashes.SHA256()),
        hashes.SHA256(),
        None))
    return encrypted_text


def decryptText(encrypted_text, private_key):
    decrypted_text = private_key.decrypt(encrypted_text, padding.OAEP(
        padding.MGF1(hashes.SHA256()),
        hashes.SHA256(),
        None))
    return decrypted_text


a = encryptText("pizza", public_key)
print(a.hex())

b = decryptText(a, private_key)
print(b)



# encryption_data = {
    #     "encrypted_text": encrypted_text.hex(), 
    #     "private_key": private_key,
    #     "public_key": public_key
    # }