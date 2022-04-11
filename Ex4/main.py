from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from cryptography.fernet import Fernet
from assymetric_functions import decrypt_text, encrypt_text
from assymetric_functions import read_private_key, read_public_key, read_private_key_OpenSSH, read_public_key_OpenSSH
from cryptography.hazmat.primitives.asymmetric import rsa
import binascii

# uvicorn main:app --reload

app = FastAPI()

data = {
    "symmetric": {},
    "asymmetric": {}
}


@app.get("/symmetric/key")
def get_symmetric_key():
    keyHEX = Fernet.generate_key().hex()
    return {"key": keyHEX}


@app.post("/symmetric/key")
def post_symmetric_key(keyHEX : str):
    keyB64 = binascii.unhexlify(keyHEX)
    try:
        f = Fernet(keyB64)
        f.encrypt(b"abcdefgh").decode()
    except:
        return {"Message": "Your keys are probably incorrect"}
    
    data["symmetric"]["keyB64"] = keyB64
    data["symmetric"]["keyHEX"] = keyHEX
    return {"Message": "Keys added successfully to the database!"}


@app.post("/symmetric/encode")
def post_symmetric_encode(text : str):
    f = Fernet(data["symmetric"]["keyB64"])
    encoded_text = f.encrypt(text.encode()).decode()
    return {"encoded_text": encoded_text}


@app.post("/symmetric/decode")
def post_symmetric_decode(text : str):
    f = Fernet(data["symmetric"]["keyB64"])
    byte_text = text.encode()
    decoded_text = f.decrypt(byte_text)
    return {"decoded_text": decoded_text}


@app.get("/asymmetric/key")
def get_asymmetric_key():
    private_key = rsa.generate_private_key(65537, 2048)

    private_key_B64 = read_private_key(private_key)
    public_key_B64 = read_public_key(private_key)

    data["asymmetric"]["private_key_B64"] = private_key_B64
    data["asymmetric"]["public_key_B64"] = public_key_B64

    data["asymmetric"]["private_key_HEX"] = private_key_B64.hex()
    data["asymmetric"]["public_key_HEX"] = public_key_B64.hex()

    return {"private_key": data["asymmetric"]["private_key_HEX"], 
        "public_key": data["asymmetric"]["public_key_HEX"]}


@app.get("/asymmetric/key/ssh")
def get_asymmetric_key_ssh():
    private_key = rsa.generate_private_key(65537, 2048)

    private_key_openSSH = read_private_key_OpenSSH(private_key)
    public_key_OpenSSH = read_public_key_OpenSSH(private_key)

    return {"private_key_openSSH": private_key_openSSH, "public_key_OpenSSH": public_key_OpenSSH}


@app.post("/asymmetric/key")
def post_asymmetric_key(private_key_HEX: str, public_key_HEX: str):
    
    try:
        private_key_B64 = binascii.unhexlify(private_key_HEX)
        public_key_B64 = binascii.unhexlify(public_key_HEX)
    except:
        return {"Message": "Your keys are probably incorrect"}
    
    data["asymmetric"]["private_key_B64"] = private_key_B64
    data["asymmetric"]["public_key_B64"] = public_key_B64

    data["asymmetric"]["private_key_HEX"] = private_key_HEX
    data["asymmetric"]["public_key_HEX"] = public_key_HEX

    return {"Message": "Keys added successfully to the database!"}


@app.post("/asymmetric/encode")
def post_asymmetric_encode(clear_text: str, ):
    return encrypt_text(clear_text)


@app.post("/asymmetric/decode")
def post_asymmetric_decode(encrypted_text: str):
    return decrypt_text(encrypted_text)


@app.get("/data")
def get_data():
    return data


@app.post("/symmetric/pizza")
def post_symmetric_key(text : str):
    print(data["asymmetric"]["public_key_B64"])
    f = Fernet(data["asymmetric"]["public_key_B64"])

    encoded_text = f.encrypt(text.encode()).decode()
    return encoded_text