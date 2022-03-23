import app_functions
import unittest
import io
import sys
import sqlite3
import os

class TestAppFunctions(unittest.TestCase):
    
    def testVerifyPasswordCorrect(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        app_functions.verifyPassword("pizza", "pizza")
        sys.stdout = sys.__stdout__ 

        self.assertEqual(capturedOutput.getvalue(), "Passwords are correct\n")
        

    def testVerifyPasswordIncorrect(self):
        self.assertRaises(SystemExit, app_functions.verifyPassword, "abcdef", "xyzdf")


    def testGenerateRandomSalt(self):
        returnedSalt = app_functions.generateRandomSalt()
        self.assertEqual(len(returnedSalt), 16)

    
    def testHashPassword(self):
        salt = "h018srijerzcsw0g"
        hashedPassword = app_functions.hashPassword("pizza", salt)
        self.assertEqual(hashedPassword, "7dc7bdfb48786d31aff85997b11b17ef4a0943f12d29791969241be8292e689b")

    
    def testAddDataToDB(self):
        hashedPassword = "7dc7bdfb48786d31aff85997b11b17ef4a0943f12d29791969241be8292e689b"
        salt = "h018srijerzcsw0g"

        app_functions.addDataToDB(hashedPassword, salt, "testDB.db")

        con = sqlite3.connect('testDB.db')
        cur = con.cursor()
        cur.execute('''SELECT * FROM PASSWORDS;''')
        tableContent = cur.fetchall()
        con.close()
        os.remove("testDB.db") 

        self.assertEqual(tableContent, [('7dc7bdfb48786d31aff85997b11b17ef4a0943f12d29791969241be8292e689b', 'h018srijerzcsw0g')])


if __name__ == '__main__':
    unittest.main()