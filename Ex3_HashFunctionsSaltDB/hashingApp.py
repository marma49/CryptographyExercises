import hashlib
import random 
import string
import sqlite3

def verifyPassword(password, repeatedPassword):
    if password != repeatedPassword:
        print("Password are not equal!")
        exit()

def generateRandomSalt():
    allCharacters = string.ascii_lowercase + string.digits
    salt = ''.join(random.choices(allCharacters, k=16))
    return salt

# def hashPassword(password, salt):
#     password = password + salt
#     hashedPassword = hashlib.sha256(password.encode()).hexdigest()
#     return hashedPassword

def hashPassword(password, salt):
    hashedPassword = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 500000).hex()
    return hashedPassword

def addDataToDB(hashedPassword, salt):
    con = sqlite3.connect('passwords.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS PASSWORDS (
                    hashed_password    TEXT    NOT NULL, 
                    salt        TEXT    NOT NULL
                    );''')

    cur.execute(f"INSERT INTO PASSWORDS VALUES ('{hashedPassword}', '{salt}')")
    con.commit()
    con.close()
    print("Data added successfully")


password = input("Enter password: ")
repeatedPassword = input("Enter password again: ")
verifyPassword(password, repeatedPassword)

salt = generateRandomSalt()
hashedPassword = hashPassword(password, salt)
addDataToDB(hashedPassword, salt)

