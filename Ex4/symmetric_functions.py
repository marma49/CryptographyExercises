from cryptography.fernet import Fernet
from binascii import unhexlify

def create_key() -> str:
    """Creates hex symmetric key

    Returns:
        str: Hex symmetric key
    """
    key = Fernet.generate_key()
    return key.hex()


def encrypt_text(text: str, key: str) -> str:
    """Encrypts text

    Args:
        text (str): Text to encrypt
        key (str): Key

    Returns:
        str: Encrypted text
    """
    f = Fernet(unhexlify(key))
    encoded_text = f.encrypt(text.encode())
    return encoded_text.hex()


def decrypt_text(encrypted_text: str, key: str) -> str:
    """Decrypts text

    Args:
        encrypted_text (str): Encrypted text
        key (str): Key used to encrypt

    Returns:
        str: Decrypted text
    """
    f = Fernet(unhexlify(key))
    return f.decrypt(unhexlify(encrypted_text)).decode()

