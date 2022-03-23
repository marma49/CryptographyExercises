import hashlib
import random 
import string
import sqlite3


def verifyPassword(password: str, repeatedPassword: str):
    """Function veryfing password entered by user

    Args:
        password (str): Password entered by user
        repeatedPassword (str): Repeated password entered by user
    """
    if password != repeatedPassword:
        exit("Passwords are not equal!")
    else:
        print("Passwords are correct")


def generateRandomSalt() -> str:
    """Function to generate random salt

    Returns:
        str: Random salt which is 16 characters long
    """
    allCharacters = string.ascii_lowercase + string.digits
    salt = ''.join(random.choices(allCharacters, k=16))
    return salt


def hashPassword(password: str, salt: str) -> str:
    """Function to hash password by using pbkdf2_hmac

    Args:
        password (str): Password entered by user
        salt (str): Random salt

    Returns:
        str: Hashed password
    """
    hashedPassword = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 847295).hex()
    return hashedPassword


def addDataToDB(hashedPassword: str, salt: str, databaseName: str):
    """Function adding password and salt to database

    Args:
        hashedPassword (str): Password which was hashed
        salt (str): Salt used to hash hashedPassword
    """
    con = sqlite3.connect(databaseName)
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS PASSWORDS (
                    hashed_password    TEXT    NOT NULL, 
                    salt        TEXT    NOT NULL
                    );''')

    cur.execute(f"INSERT INTO PASSWORDS VALUES ('{hashedPassword}', '{salt}')")
    con.commit()
    con.close()
    print("Data added successfully")