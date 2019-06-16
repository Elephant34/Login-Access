'''
Tests if the username and password are valid
'''
# For logging key events
import logging
# For reading the data off teh databse
import sqlite3

# For hashing the username and password
from scr.utilities.hashing.hash_api import Hash

HASH_API = Hash()


def check_login(settings_path, username_ent, password_ent):
    '''
    Ensures the username and password match a valid account
    '''
    logging.info("Attempting to login")

    with sqlite3.connect(str(settings_path / "LoginAccess.db")) as con:
        cur = con.cursor()

        cur.execute("SELECT Password FROM Users WHERE Username = ?",
                    (HASH_API.hash_text(str(username_ent.get()), secure=False), ))

        try:
            user_password = cur.fetchall()[0][0]
        except IndexError:
            logging.warning("Username doesn't exist")
            # Couldn't find a password with the username therefore the username doesn't exist
            return False

    if HASH_API.verify(str(password_ent.get()), user_password):
        logging.info("Login successful")
        return True

    logging.warning("Incorrect password entered")
    return False
