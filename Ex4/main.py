from msilib.schema import Error
from re import A
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from cryptography.fernet import Fernet

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




@app.get("/data")
def get_data():
    return data