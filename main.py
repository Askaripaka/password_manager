import display
import insert


def main():
    print("""WELCOME TO PASSMANAGER \n

    ENTER 1: TO ENTER CREDENTALS \n 

    ENTER 2: TO VIEW passwords \n""")

    opt = input("-> ")

    match opt:
        case "1":
            insert.InsertDatabase("passwords.db").insert_into_db()
            insert.InsertDatabase("passwords.db").db_close()
        case "2":
            display.SelectDatabase("passwords.db").get_from_database()


if __name__ == "__main__":
    main()
