'''
Validates the inputs from the account creation
'''
# For handeling the gui elements
import tkinter
# For hashing the usernames and passwords
from scr.utilities.hashing.hash_api import Hash

HASH_API = Hash()


class NewAccount():
    '''
    validates and calls the new account methods
    '''

    def __init__(self, inputs, settings_path, space_lbl):
        '''
        Checks the inputs are valid then creats the account
        '''

        self.username_ent = inputs.username_ent
        self.password_ent = inputs.password_ent
        self.repeatpassword_ent = inputs.repeatpassword_ent

        self.settings_path = settings_path
        self.space_lbl = space_lbl

        # cheks the inputs are all filled
        if not self.exists_validation():
            self.username_ent.delete(0, tkinter.END)
            self.password_ent.delete(0, tkinter.END)
            self.repeatpassword_ent.delete(0, tkinter.END)
            self.space_lbl.config(
                text="Sorry you must fill in all of the inputs")

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
