'''
Creates the primary owner account
'''
# Allows for logging
import logging
# Allows for database manipulaton
import sqlite3
# Imports the hashing so the system never know the usersname or passwords given
from scr.utilities.hashing.hash_api import Hash


# Sets up the hashing class
HASH_API = Hash()


def owner_setup(database_path):
    '''
    Gets the needed info then creates the owner account
    '''

    print("We will now guide you through the creation of the owner account")
    print(
        "Please note- capitilisation is important (i.e. 'Name' isn't the same as 'name'")

    username = get_username()
    password = get_password()

    create_owner_account(username, password, database_path)

    return


def get_username():
    '''
    Gets the oweners account name
    '''

    username = HASH_API.hash_text(
        str(input("Please enter your username: ")), secure=False)

    logging.info("Got username %s", username)

    return username


def get_password():
    '''
    Gets the account password
    '''

    while True:

        password = HASH_API.hash_text(
            str(input("Please enter your password: ")))

        # Will return true if the given password matches the reented one
        if HASH_API.verify(str(input("Please re-enter your password: ")), password):
            break
        else:
            logging.warning("Password inputs didn't match")
            print("Sorry those inputs didn't match please try again")

    logging.info("Got password hash %s", password)

    return password


def create_owner_account(username, password_hash, database_path):
    '''
    Insets the user into the database
    '''

    group = HASH_API.hash_text("owner")

    with sqlite3.connect(str(database_path)) as con:
        cur = con.cursor()

        cur.execute("""
            INSERT INTO Users('Username', 'Password', 'group') VALUES (?, ?, ?)
        """, (username, password_hash, group))

    logging.info("Owner account inserted into database")

    return
