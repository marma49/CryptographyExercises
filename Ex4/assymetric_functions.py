from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.serialization import load_ssh_private_key
from cryptography.exceptions import InvalidSignature
from binascii import unhexlify


def create_private_key() -> str:
    """Creates hex private key

    Returns:
        str: Hex private key
    """
    private_key_obj = rsa.generate_private_key(65537, 2048)

    private_key_str = private_key_obj.private_bytes(
        serialization.Encoding.PEM, 
        serialization.PrivateFormat.TraditionalOpenSSL, 
        serialization.NoEncryption()
    )
    return private_key_str.hex()


def create_public_key(private_key_str: str) -> str:
    """Creates hex public key from hex private key

    Args:
        private_key_str (str): Hex private key

    Returns:
        str: Hex public key
    """
    private_key_obj = load_pem_private_key(unhexlify(private_key_str), None)

    public_key_str = private_key_obj.public_key().public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return public_key_str.hex()


def create_private_key_OpenSSH() -> str:
    """Creates hex private OpenSSH key

    Returns:
        str: Hex private OpenSSH key
    """
    private_key_obj = rsa.generate_private_key(65537, 2048)

    private_key_str = private_key_obj.private_bytes(
        serialization.Encoding.PEM, 
        serialization.PrivateFormat.OpenSSH, 
        serialization.NoEncryption()
    )
    return private_key_str.hex()


def create_public_key_OpenSSH(private_key_str: str) -> str:
    """Creates a hex public OpenSSH key from a hex private key 

    Args:
        private_key_str (str): Hex private OpenSSH key

    Returns:
        str: Public OpenSSH key as a hex
    """
    private_key_obj = load_ssh_private_key(unhexlify(private_key_str), None)

    public_key_str = private_key_obj.public_key().public_bytes(
        serialization.Encoding.OpenSSH,
        serialization.PublicFormat.OpenSSH
    )
    return public_key_str.hex()


def encrypt_text(clear_text: str, public_key_str: str) -> str:
    """Encrypts text by using hex public key

    Args:
        clear_text (str): Text which you want to encrypt
        public_key_str (str): Public key

    Returns:
        str: Encrypted text
    """
    public_key_obj = load_pem_public_key(unhexlify(public_key_str), None)

    encrypted_text = public_key_obj.encrypt(clear_text.encode(), padding.OAEP(
        padding.MGF1(hashes.SHA256()),
        hashes.SHA256(),
        None))
    return encrypted_text.hex()


def decrypt_text(encrypted_text: str, private_key_str: str) -> str:
    """Decrypts text by using hex private key

    Args:
        encrypted_text (str): Encrypted text
        private_key_str (str): Private key

    Returns:
        str: Decrypted text
    """
    private_key_obj = load_pem_private_key(unhexlify(private_key_str), None)

    decrypted_text = private_key_obj.decrypt(unhexlify(encrypted_text), padding.OAEP(
        padding.MGF1(hashes.SHA256()),
        hashes.SHA256(),
        None))
    return decrypted_text.decode()


def verify_message(clear_text: str, signature: str, public_key_str: str):
    """Check if text was encrypted with a given public key

    Args:
        clear_text (str): Clear text of message
        signature (str): Signed message
        public_key_str (str): Hex public text

    Returns:
        _type_: _description_
    """
    public_key = load_pem_public_key(unhexlify(public_key_str), None)
    try: 
        public_key.verify(
            unhexlify(signature),
            clear_text.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
    except InvalidSignature:
        return False
    return True

    
def sign_message(private_key_str: str, clear_text: str) -> str:
    """Signs message

    Args:
        private_key_str (str): Hex private key
        clear_text (str): Message to sign

    Returns:
        str: Signed message
    """
    private_key_obj = load_pem_private_key(unhexlify(private_key_str), None)

    signature = private_key_obj.sign(
        clear_text.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature.hex()
