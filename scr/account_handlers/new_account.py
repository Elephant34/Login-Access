'''
Validates the inputs from the account creation
'''
# For handeling the gui elements
import tkinter
# For logging key events
import logging
# For handeling the databse
import sqlite3
# For hashing the usernames and passwords
from scr.utilities.hashing.hash_api import Hash
# For laoding the weak password list
from scr.utilities.resource_path import resource_path

HASH_API = Hash()


class NewAccount():
    '''
    validates and calls the new account methods
    '''

    def __init__(self, inputs, settings_path, space_lbl):
        '''
        Checks the inputs are valid then creats the account
        '''
        logging.info("Attempting account creation")

        self.username_ent = inputs.username_ent
        self.password_ent = inputs.password_ent
        self.repeatpassword_ent = inputs.repeatpassword_ent

        self.settings_path = settings_path
        self.space_lbl = space_lbl

        # cheks the inputs are all filled
        if not self.exists_validation():
            logging.info("Not all inputs given!")
            self.clear_inputs()
            self.space_lbl.config(
                text="Sorry you must fill in all of the inputs")
            return
        # Checks the two passwords are the same
        if not self.passwords_match():
            logging.info("passwords didn't match!")
            self.clear_inputs()
            self.space_lbl.config(
                text="Your passwords didn't match. Please try again")
            return
        # Checks password strength
        if not self.strong_password():
            logging.info("Weak password given")
            self.clear_inputs()
            self.space_lbl.config(
                text="Sorry your password was weak. Please try again")
            return

        self.space_lbl.config(text="Loading...")
        self.space_lbl.update_idletasks()

        account_callback = create_account(
            self.settings_path,
            HASH_API.hash_text(str(self.username_ent.get()), secure=False),
            HASH_API.hash_text(str(self.password_ent.get())),
            HASH_API.hash_text("standered")
        )
        if account_callback != True:
            self.clear_inputs()
            self.space_lbl.config(text=account_callback)

        self.space_lbl.config(text="Account creation sucessfull")
        return

    def clear_inputs(self):
        '''
        Clears the entry widgets
        '''
        self.username_ent.delete(0, tkinter.END)
        self.password_ent.delete(0, tkinter.END)
        self.repeatpassword_ent.delete(0, tkinter.END)

        self.username_ent.focus()

        return

    def exists_validation(self):
        '''
        Checks that all of the inputs feils have data inside of them
        '''

        if self.username_ent.get() == "":
            return False
        if self.password_ent.get() == "":
            return False
        if self.repeatpassword_ent.get() == "":
            return False

        return True

    def passwords_match(self):
        '''
        Checks the password and it's repeat match
        '''
        if str(self.password_ent.get()) == str(self.repeatpassword_ent.get()):
            return True

        return False

    def strong_password(self):
        '''
        Checks how strong the password is by length
        Validates the password isn't in the username
        '''
        with open(resource_path("./scr/account_handlers/bad_passwords.txt"), "r") as bad_passwd_f:
            bad_password_list = bad_passwd_f.read().splitlines()

        if str(self.password_ent.get()) in bad_password_list:
            return False

        if str(self.password_ent.get()) in str(self.username_ent.get()):
            return False
        if str(self.username_ent.get()) in str(self.password_ent.get()):
            return False

        if len(self.password_ent.get()) < 7:
            return False

        return True


def create_account(settings_path, username, password, group):
    '''
    Creates a user account and palces it into the database
    '''
    logging.info("Attempting account creation")

    database_path = settings_path / "LoginAccess.db"

    with sqlite3.connect(str(database_path)) as con:
        cur = con.cursor()

        try:
            cur.execute("""INSERT INTO Users("Username", "Password", "Group") VALUES (?, ?, ?)""",
                        (username, password, group))
        except sqlite3.IntegrityError:
            return "Username already exists"

    return True
