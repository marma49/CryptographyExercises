from fastapi import FastAPI, Path
from cryptography.fernet import Fernet
from assymetric_functions import *
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
    private_key = create_private_key()
    public_key = create_public_key(private_key)

    data["asymmetric"]["private_key"] = private_key
    data["asymmetric"]["public_key"] = public_key

    return {"private_key": data["asymmetric"]["private_key"], 
        "public_key": data["asymmetric"]["public_key"]}


@app.get("/asymmetric/key/ssh")
def get_asymmetric_key_ssh():
    private_key_OpenSSH = create_private_key_OpenSSH()
    public_key_OpenSSH = create_public_key_OpenSSH(private_key_OpenSSH)

    return {"private_key_openSSH": private_key_OpenSSH, "public_key_OpenSSH": public_key_OpenSSH}


@app.post("/asymmetric/key")
def post_asymmetric_key(private_key: str, public_key: str):
    
    data["asymmetric"]["private_key"] = private_key
    data["asymmetric"]["public_key"] = public_key

    return {"Message": "Keys added successfully to the database!"}


@app.post("/asymmetric/verify")
def post_asymmetric_verify(clear_text, signature):
    public_key_str = data["asymmetric"]["public_key"]
    if verify_message(clear_text, signature, public_key_str) == True:
        return {"Message": "Message verified correctly to be encrypted with given public key"}
    else:
        return {"Message": "Message verified incorrectly"}


@app.post("/asymmetric/sign")
def post_asymmetric_sign(clear_text):
    private_key_str = data["asymmetric"]["private_key"]
    signed_message = sign_message(private_key_str, clear_text)

    return {"Signed message": signed_message}


@app.post("/asymmetric/encode")
def post_asymmetric_encode(clear_text: str):
    encrypted_text = encrypt_text(clear_text, data["asymmetric"]["public_key"])
    return {"encrypted text": encrypted_text}


@app.post("/asymmetric/decode")
def post_asymmetric_decode(encrypted_text: str):
    decrypted_text = decrypt_text(encrypted_text, data["asymmetric"]["private_key"])
    return {"decrypted text": decrypted_text}


@app.get("/data")
def get_data():
    return data


