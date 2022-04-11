from fastapi import FastAPI, Path
from cryptography.fernet import Fernet
import symmetric_functions
import assymetric_functions
import binascii

# uvicorn main:app --reload

app = FastAPI()

data = {
    "symmetric": {},
    "asymmetric": {}
}

@app.get("/symmetric/key")
def get_symmetric_key():
    key = symmetric_functions.create_key()
    return {"key": key}


@app.post("/symmetric/key")
def post_symmetric_key(key : str):
    data["symmetric"]["key"] = key
    return {"Message": "Key added successfully to the database!"}


@app.post("/symmetric/encode")
def post_symmetric_encode(clear_text : str):
    encrypted_text = symmetric_functions.encrypt_text(
        clear_text, 
        data["symmetric"]["key"])

    return {"encoded_text": encrypted_text}


@app.post("/symmetric/decode")
def post_symmetric_decode(encrypted_text : str):
    decrypted_text = symmetric_functions.decrypt_text(
        encrypted_text, 
        data["symmetric"]["key"])

    return {"decoded_text": decrypted_text}


@app.get("/asymmetric/key")
def get_asymmetric_key():
    private_key = assymetric_functions.create_private_key()
    public_key = assymetric_functions.create_public_key(private_key)

    data["asymmetric"]["private_key"] = private_key
    data["asymmetric"]["public_key"] = public_key

    return {"private_key": data["asymmetric"]["private_key"], 
        "public_key": data["asymmetric"]["public_key"]}


@app.get("/asymmetric/key/ssh")
def get_asymmetric_key_ssh():
    private_key_OpenSSH = assymetric_functions.create_private_key_OpenSSH()
    public_key_OpenSSH = assymetric_functions.create_public_key_OpenSSH(private_key_OpenSSH)

    return {"private_key_openSSH": private_key_OpenSSH, "public_key_OpenSSH": public_key_OpenSSH}


@app.post("/asymmetric/key")
def post_asymmetric_key(private_key: str, public_key: str):
    
    data["asymmetric"]["private_key"] = private_key
    data["asymmetric"]["public_key"] = public_key

    return {"Message": "Keys added successfully to the database!"}


@app.post("/asymmetric/verify")
def post_asymmetric_verify(clear_text, signature):
    public_key_str = data["asymmetric"]["public_key"]
    if assymetric_functions.verify_message(clear_text, signature, public_key_str) == True:
        return {"Message": "Message verified correctly to be encrypted with given public key"}
    else:
        return {"Message": "Message verified incorrectly"}


@app.post("/asymmetric/sign")
def post_asymmetric_sign(clear_text):
    private_key_str = data["asymmetric"]["private_key"]
    signed_message = assymetric_functions.sign_message(private_key_str, clear_text)

    return {"Signed message": signed_message}


@app.post("/asymmetric/encode")
def post_asymmetric_encode(clear_text: str):
    encrypted_text = assymetric_functions.encrypt_text(clear_text, data["asymmetric"]["public_key"])
    return {"encrypted text": encrypted_text}


@app.post("/asymmetric/decode")
def post_asymmetric_decode(encrypted_text: str):
    decrypted_text = assymetric_functions.decrypt_text(encrypted_text, data["asymmetric"]["private_key"])
    return {"decrypted text": decrypted_text}


@app.get("/data")
def get_data():
    return data


