from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from cryptography.fernet import Fernet
from assymetric_functions import encryptText, decryptText
from cryptography.hazmat.primitives.asymmetric import rsa

# uvicorn main:app --reload

app = FastAPI()

data = {
    "symmetric": {},
    "asymmetric": {}
}


@app.get("/symmetric/key")
def get_symmetric_key():
    key = Fernet.generate_key().decode()
    return {"key": key}


@app.post("/symmetric/key")
def post_symmetric_key(key : str):
    try:
        f = Fernet(key.encode())
        f.encrypt(b"abcdefgh").decode()
    except:
        return {"Message": "Your key is probably incorrect"}

    data["symmetric"]["key"] = key
    return {"Message": "Key added successfully to data"}


@app.post("/symmetric/encode")
def post_symmetric_encode(text : str):
    f = Fernet(data["symmetric"]["key"])
    encoded_text = f.encrypt(text.encode()).decode()
    return {"encoded_text": encoded_text}


@app.post("/symmetric/decode")
def post_symmetric_decode(text : str):
    f = Fernet(data["symmetric"]["key"])
    byte_text = text.encode()
    decoded_text = f.decrypt(byte_text)
    return {"decoded_text": decoded_text}


@app.get("/asymmetric/key")
def get_asymmetric_key():
    private_key = rsa.generate_private_key(65537, 2048)
    public_key = private_key.public_key()  

    data["asymmetric"]["private_key"] = private_key
    data["asymmetric"]["public_key"] = public_key

    return {"private_key": private_key, "public_key": public_key}


# @app.post("/asymmetric/key")
# def post_asymmetric_key():



@app.get("/data")
def get_data():
    return data