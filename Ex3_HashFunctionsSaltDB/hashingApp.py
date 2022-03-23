from app_functions import *

password = input("Enter password: ")
repeatedPassword = input("Enter password again: ")
verifyPassword(password, repeatedPassword)

salt = generateRandomSalt()
hashedPassword = hashPassword(password, salt)

addDataToDB(hashedPassword, salt, "passwordsDB.db")