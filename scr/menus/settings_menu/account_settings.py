'''
Loads the GUI for the settings classes
'''
# For logging
import logging
# For the GUI
import tkinter
# For databse handeling
import sqlite3

# For going back to the main menu
from scr.menus.settings_menu import main_settings
# For the title
from scr.menus.title import Title
# for the hashing system API
from scr.utilities.hashing.hash_api import Hash

HASH_API = Hash()


class AccountSettings(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    The main settings menu
    '''

    def __init__(self, settings_path, parent, username, colour_data, *args, **kwargs):
        '''
        Sets up the correct verables and loads the GUI
        '''
        logging.info("Settings manu loading")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.top_parent = parent

        self.username = username
        self.username_hash = HASH_API.hash_text(self.username, secure=False)

        self.settings_path = settings_path

        self.colour_data = colour_data

        parent.config(bg=self.colour_data["background"])
        self.config(bg=self.colour_data["background"])

        self.title_fr = Title("Account Settings", self.colour_data, self)
        self.title_fr.pack(fill=tkinter.X, expand=True,
                           side=tkinter.TOP, padx=5, pady=1)

        Buttons(self.settings_path, self.username, self.username_hash,
                self.colour_data, self, self.top_parent).pack(
                    fill=tkinter.BOTH, side=tkinter.TOP, expand=True, padx=3, pady=3)

        logging.info("Account settings loaded sucessfully")

        return


class Buttons(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    Loads all of the new account screens buttons
    '''

    def __init__(self, settings_path, username, username_hash, colour_data, parent, top_parent, *args, **kwargs):  # pylint: disable=too-many-arguments, line-too-long
        '''
        Loads the button frame of the GUI
        '''
        logging.info("Loading account settings button section")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.colour_data = colour_data

        self.settings_path = settings_path

        self.parent = parent
        self.top_parent = top_parent

        self.username = username
        self.username_hash = username_hash

        self.config(bg=self.colour_data["background"])

        self.settings = ["change username", "change password",
                         "add email adress", "add public username", "request upgrade"]

        for setting in self.settings:
            tkinter.Button(self,
                           text=setting.title(),
                           bg=self.colour_data["btn_background"],
                           activebackground=self.colour_data["btn_active"],
                           fg=self.colour_data["foreground"],
                           font=self.colour_data["font"],
                           command=lambda button_pressed=setting: self.menu_option(
                               button_pressed)
                           ).pack(fill=tkinter.BOTH, side=tkinter.TOP, expand=True, padx=2, pady=2)  # pylint: disable=bad-continuation
        tkinter.Label(self,
                      text="",
                      bg=self.colour_data["background"],
                      fg=self.colour_data["foreground"],
                      font=self.colour_data["font"],
                      ).pack(fill=tkinter.BOTH, side=tkinter.TOP, expand=True, padx=2, pady=2)  # pylint: disable=bad-continuation

        # Back button
        tkinter.Button(
            self,
            text="Back",
            bg=self.colour_data["btn_background"],
            activebackground=self.colour_data["btn_active"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            command=lambda: self.back()  # pylint: disable=unnecessary-lambda
        ).pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True, padx=2, pady=2)

    def menu_option(self, button_pressed):
        '''
        Loads the menu based off the correct button pressed
        '''
        logging.info("Loading setting %s", button_pressed)

        if button_pressed == "change username":
            logging.info("Loading change account main menu")
            self.parent.destroy()
            ChangeUsername(
                self.settings_path, self.top_parent, self.username, self.colour_data).pack(
                    fill=tkinter.BOTH, expand=True)
        elif button_pressed == "add public username":
            logging.info("Loading public username settings")
            self.parent.destroy()
            ChangePublicUsername(
                self.settings_path, self.top_parent, self.username, self.colour_data).pack(
                    fill=tkinter.BOTH, expand=True)
        elif button_pressed == "add email adress":
            logging.info("Loading email settings")
            self.parent.destroy()
            ChangeEmailAdress(
                self.settings_path, self.top_parent, self.username, self.colour_data).pack(
                    fill=tkinter.BOTH, expand=True)
        return

    def back(self):
        '''
        Takes the user back to the login screen
        '''
        logging.info("Exiting the account settings menu")
        self.parent.destroy()
        main_settings.SettingsMenu(self.settings_path, self.top_parent,
                                   self.username, self.colour_data).pack(
                                       fill=tkinter.BOTH, expand=True)

        return


class ChangeUsername(tkinter.Frame):  # pylint: disable=too-many-ancestors, too-many-instance-attributes
    '''
    Loads the frame for changing the username
    '''

    def __init__(self, settings_path, parent, username, colour_data, *args, **kwargs):
        '''
        Sets up the correct verables and loads the GUI
        '''
        logging.info("Change username manu loading")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.top_parent = parent

        self.username = username
        self.username_hash = HASH_API.hash_text(self.username, secure=False)

        self.settings_path = settings_path

        self.colour_data = colour_data

        parent.config(bg=self.colour_data["background"])
        self.config(bg=self.colour_data["background"])

        self.title_fr = Title("Change Username", self.colour_data, self)
        self.title_fr.pack(fill=tkinter.X, expand=True,
                           side=tkinter.TOP, padx=5, pady=1)

        self.username_fr = tkinter.Frame(
            self,
            bg=self.colour_data["background"]
        )
        self.username_fr.pack(fill=tkinter.X, expand=True,
                              side=tkinter.TOP, padx=3, pady=2)

        # New username entry
        tkinter.Label(
            self.username_fr,
            text="New Username:",
            bg=self.colour_data["background"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            anchor=tkinter.CENTER
        ).pack(fill=tkinter.BOTH, expand=True, side=tkinter.LEFT, padx=3, pady=2)

        # Username entry
        self.new_username_ent = tkinter.Entry(
            self.username_fr,
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
        )
        self.new_username_ent.pack(
            fill=tkinter.BOTH, expand=True, side=tkinter.RIGHT, padx=3, pady=2)

        # Spacing label
        tkinter.Label(
            self,
            text="",
            bg=self.colour_data["background"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            anchor=tkinter.CENTER
        ).pack(fill=tkinter.BOTH, expand=True, side=tkinter.TOP, padx=3, pady=2)

        self.button_fr = tkinter.Frame(
            self,
            bg=self.colour_data["background"]
        )
        self.button_fr.pack(fill=tkinter.X, expand=True,
                            side=tkinter.TOP, padx=3, pady=2)

        # Back button
        tkinter.Button(
            self.button_fr,
            text="Back",
            bg=self.colour_data["btn_background"],
            activebackground=self.colour_data["btn_active"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            command=lambda: self.back()  # pylint: disable=unnecessary-lambda
        ).pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True, padx=2, pady=2)

        # Change username button
        tkinter.Button(
            self.button_fr,
            text="Change Username",
            bg=self.colour_data["positive_btn_background"],
            activebackground=self.colour_data["positive_btn_active"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            command=lambda: self.change_username()  # pylint: disable=unnecessary-lambda
        ).pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True, padx=2, pady=2)

        self.new_username_ent.bind(
            "<Return>", lambda e: self.change_username())

    def back(self):
        '''
        Takes the user back to the login screen
        '''
        logging.info("Exiting the account settings menu")
        self.destroy()
        AccountSettings(self.settings_path, self.top_parent, self.username,
                        self.colour_data).pack(fill=tkinter.BOTH, expand=True)

        return

    def change_username(self):
        '''
        Chacks the new username is valid then changes the username
        '''

        new_username = str(self.new_username_ent.get())
        new_username_hash = HASH_API.hash_text(
            new_username, secure=False)

        with sqlite3.connect(str(self.settings_path / "loginAccess.db")) as con:
            cur = con.cursor()

            try:
                cur.execute("UPDATE Users SET Username = ? WHERE Username = ?", (
                    new_username_hash, self.username_hash))
            except sqlite3.IntegrityError:
                self.new_username_ent.delete(0, tkinter.END)
                self.title_fr.space_lbl.config(
                    text="Sorry, that username is already taken")
                self.title_fr.space_lbl.update_idletasks()
                return

        self.new_username_ent.delete(0, tkinter.END)
        self.title_fr.space_lbl.config(
            text="Username changed sucessfully!")
        self.username = new_username
        self.username_hash = HASH_API.hash_text(self.username, secure=False)


class ChangePublicUsername(tkinter.Frame):  # pylint: disable=too-many-ancestors, too-many-instance-attributes
    '''
    Loads the frame for changing the username
    '''

    def __init__(self, settings_path, parent, username, colour_data, *args, **kwargs):
        '''
        Sets up the correct verables and loads the GUI
        '''
        logging.info("Change username manu loading")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.top_parent = parent

        self.username = username
        self.username_hash = HASH_API.hash_text(self.username, secure=False)

        self.settings_path = settings_path

        self.colour_data = colour_data

        parent.config(bg=self.colour_data["background"])
        self.config(bg=self.colour_data["background"])

        self.title_fr = Title("Change Public Username", self.colour_data, self)
        self.title_fr.pack(fill=tkinter.X, expand=True,
                           side=tkinter.TOP, padx=5, pady=1)

        self.username_fr = tkinter.Frame(
            self,
            bg=self.colour_data["background"]
        )
        self.username_fr.pack(fill=tkinter.X, expand=True,
                              side=tkinter.TOP, padx=3, pady=2)

        # New username entry
        tkinter.Label(
            self.username_fr,
            text="New Public Username:",
            bg=self.colour_data["background"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            anchor=tkinter.CENTER
        ).pack(fill=tkinter.BOTH, expand=True, side=tkinter.LEFT, padx=3, pady=2)

        # Username entry
        self.new_public_username_ent = tkinter.Entry(
            self.username_fr,
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
        )
        self.new_public_username_ent.pack(
            fill=tkinter.BOTH, expand=True, side=tkinter.RIGHT, padx=3, pady=2)

        # Spacing label
        tkinter.Label(
            self,
            text="",
            bg=self.colour_data["background"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            anchor=tkinter.CENTER
        ).pack(fill=tkinter.BOTH, expand=True, side=tkinter.TOP, padx=3, pady=2)

        self.button_fr = tkinter.Frame(
            self,
            bg=self.colour_data["background"]
        )
        self.button_fr.pack(fill=tkinter.X, expand=True,
                            side=tkinter.TOP, padx=3, pady=2)

        # Back button
        tkinter.Button(
            self.button_fr,
            text="Back",
            bg=self.colour_data["btn_background"],
            activebackground=self.colour_data["btn_active"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            command=lambda: self.back()  # pylint: disable=unnecessary-lambda
        ).pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True, padx=2, pady=2)

        # Change username button
        tkinter.Button(
            self.button_fr,
            text="Change Public Username",
            bg=self.colour_data["positive_btn_background"],
            activebackground=self.colour_data["positive_btn_active"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            command=lambda: self.change_public_username()  # pylint: disable=unnecessary-lambda
        ).pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True, padx=2, pady=2)

        self.new_public_username_ent.bind(
            "<Return>", lambda e: self.change_public_username())

    def back(self):
        '''
        Takes the user back to the login screen
        '''
        logging.info("Exiting the account settings menu")
        self.destroy()
        AccountSettings(self.settings_path, self.top_parent, self.username,
                        self.colour_data).pack(fill=tkinter.BOTH, expand=True)

        return

    def change_public_username(self):
        '''
        Chacks the new username is valid then changes the username
        '''

        new_public_username = str(self.new_public_username_ent.get())

        with sqlite3.connect(str(self.settings_path / "loginAccess.db")) as con:
            cur = con.cursor()

            cur.execute("UPDATE Users SET Public_Username = ? WHERE Username = ?", (
                new_public_username, self.username_hash))

        self.new_public_username_ent.delete(0, tkinter.END)
        self.title_fr.space_lbl.config(
            text="Username changed sucessfully!")

        return

class ChangeEmailAdress(tkinter.Frame):  # pylint: disable=too-many-ancestors, too-many-instance-attributes
    '''
    Loads the frame for changing the username
    '''

    def __init__(self, settings_path, parent, username, colour_data, *args, **kwargs):
        '''
        Sets up the correct verables and loads the GUI
        '''
        logging.info("Change email manu loading")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.top_parent = parent

        self.username = username
        self.username_hash = HASH_API.hash_text(self.username, secure=False)

        self.settings_path = settings_path

        self.colour_data = colour_data

        parent.config(bg=self.colour_data["background"])
        self.config(bg=self.colour_data["background"])

        self.title_fr = Title("Change Email Adress", self.colour_data, self)
        self.title_fr.pack(fill=tkinter.X, expand=True,
                           side=tkinter.TOP, padx=5, pady=1)