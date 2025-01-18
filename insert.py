import os
import sqlite3
from cryptography.fernet import Fernet
from dotenv import load_dotenv


class InsertDatabase:
    def __init__(self, dbname) -> None:
        self.dbname = dbname
        self.connecion = sqlite3.connect(dbname)
        self.cur = self.connecion.cursor()
        self.exec = self.cur.execute

    def usr_in(self):

        self.exec(
            "CREATE TABLE IF NOT EXISTS passwords(application TEXT, username TEXT, password TEXT) ")

        app = input("Enter the application here -> ")
        usrname = input("Enter the username here -> ")
        passwd = input("Enter the password here -> ")

        return app, usrname.encode(), passwd.encode()

    def insert_into_db(self):
        app, usrname, passwd = self.usr_in()

        load_dotenv()
        key = os.getenv("KEY")
        engine = Fernet(key)

        usrname_crypt = engine.encrypt(usrname)
        passwd_crypt = engine.encrypt(passwd)

        self.exec("INSERT INTO passwords VALUES (?,?,?)",
                  (app, usrname_crypt, passwd_crypt))

        self.connecion.commit()

    def db_close(self):
        self.cur.close()
        self.connecion.close()
