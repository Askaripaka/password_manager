from cryptography.fernet import Fernet
import os
from insert import InsertDatabase
from dotenv import load_dotenv


class SelectDatabase(InsertDatabase):
    def __init__(self, dbname) -> None:
        super().__init__(dbname)

    def get_from_database(self):
        credentials = self.exec("SELECT * FROM passwords")

        cred = credentials.fetchall()

        load_dotenv()
        key = os.getenv('KEY')

        engine = Fernet(key)

        print("FORMAT : APPLICATION | USERNAME | PASSWORD \n")

        for row in cred:
            app, usrname, passwd = row

            decrypted_username = engine.decrypt(usrname)
            decrypted_pass = engine.decrypt(passwd)

            print(f"{app}  | {decrypted_username.decode()}  | {
                  decrypted_pass.decode()}  ")


if __name__ == "__main__":
    SelectDatabase(dbname="passwords.db").get_from_database()
