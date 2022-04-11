from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def read_private_key(private_key):
    pem = private_key.private_bytes(
        serialization.Encoding.PEM, 
        serialization.PrivateFormat.TraditionalOpenSSL, 
        serialization.NoEncryption()
    )
    pem = ''.join(pem.decode().splitlines()[1:-1]).encode()
    return pem


def read_public_key(private_key):
    pub_pem = private_key.public_key().public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo
    )

    pub_pem = ''.join(pub_pem.decode().splitlines()[1:-1]).encode()
    return pub_pem


def encrypt_text(clear_text, public_key):
    encrypted_text = public_key.encrypt(clear_text.encode(), padding.OAEP(
        padding.MGF1(hashes.SHA256()),
        hashes.SHA256(),
        None))
    return encrypted_text


def decrypt_text(encrypted_text, private_key):
    decrypted_text = private_key.decrypt(encrypted_text, padding.OAEP(
        padding.MGF1(hashes.SHA256()),
        hashes.SHA256(),
        None))
    return decrypted_text


def read_private_key_OpenSSH(private_key):
    pem = private_key.private_bytes(
        serialization.Encoding.PEM, 
        serialization.PrivateFormat.OpenSSH, 
        serialization.NoEncryption()
    )
    return pem.hex()


def read_public_key_OpenSSH(private_key):
    pub_pem = private_key.public_key().public_bytes(
        serialization.Encoding.OpenSSH,
        serialization.PublicFormat.OpenSSH
    )
    return pub_pem.hex()



