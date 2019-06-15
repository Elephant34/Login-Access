'''
The main menu veiwed on login
'''
# For logging events
import logging
# For handeling the database
import sqlite3
# For GUI construction
import tkinter
# For spliting the string into a list
from ast import literal_eval

# For logging off
from scr.menus.login_menu import main_login
# For the help screen
from scr.menus.main_menu import menu_help
# For the settings
from scr.menus.settings_menu import main_settings
# For creating the title
from scr.menus.title import Title
# For hashing
from scr.utilities.hashing.hash_api import Hash
# Checks the colours are valid
from scr.utilities.verify_colour import verify_colour

HASH_API = Hash()

# Temperary until I sort out the groups setup propally
ALL_GROUPS = ['tools', 'games', 'education', "admin", "owner"]


class MainMenu(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    The main menu veiwed on login
    '''

    def __init__(self, settings_path, parent, username, colour_data, *args, **kwargs):
        '''
        Sets up the correct verables and loads the GUI
        '''
        logging.info("Main manu loading")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.top_parent = parent

        self.username = username
        self.username_hash = HASH_API.hash_text(self.username, secure=False)

        self.settings_path = settings_path

        self.colour_data = self.get_colour_data(colour_data)

        parent.config(bg=self.colour_data["background"])
        self.config(bg=self.colour_data["background"])

        self.title_fr = Title("Welcome {}!".format(
            self.username), self.colour_data, self)
        self.title_fr.pack(fill=tkinter.X, expand=True,
                           side=tkinter.TOP, padx=5, pady=1)

        MainButtons(self.settings_path, self.username,
                    self.colour_data, self, self.top_parent).pack(
                        fill=tkinter.BOTH, expand=True, side=tkinter.TOP, padx=5, pady=2)

        BottomButtons(self.settings_path, self.top_parent, self.colour_data, self).pack(
            fill=tkinter.X, expand=True, side=tkinter.BOTTOM, padx=5, pady=2)

        logging.info("Main menu GUI created successfully")

        return

    def get_colour_data(self, default_colour_data):
        '''
        Gets the colour data out of the database
        If no value exists the default will be used instead
        '''

        with sqlite3.connect(str(self.settings_path / "LoginAccess.db")) as con:
            cur = con.cursor()

            # Creats the table if it doesnt exist
            cur.execute("""
                CREATE TABLE IF NOT EXISTS Colours (
                'Username' STRING PRIMARY KEY,
                background TEXT NOT NULL,
                foreground TEXT NOT NULL,
                btn_background TEXT NOT NULL,
                btn_active TEXT NOT NULL,
                negetive_btn_background TEXT NOT NULL,
                negetive_btn_active TEXT NOT NULL,
                positive_btn_background TEXT NOT NULL,
                positive_btn_active NUMERIC NOT NULL,
                font TEXT NOT NULL,
                title_font NOT NULL,
                subtitle_font NOT NULL,
                FOREIGN KEY (Username) REFERENCES Users (Username) ON UPDATE CASCADE ON DELETE CASCADE
                )
            """)

            cur.execute(
                """SELECT * FROM Colours WHERE Username=?""", (self.username_hash,))

            try:
                colour_data = cur.fetchall()[0]
            except IndexError:
                # This will raise if the user hasn't got custon colours
                return default_colour_data

            colour_pos_lookup = [
                "",
                "background",
                "foreground",
                "btn_background",
                "btn_active",
                "negetive_btn_background",
                "negetive_btn_active",
                "positive_btn_background",
                "positive_btn_active",
                "font",
                "title_font",
                "subtitle_font"
            ]

            temp_colour_dict = {}

            for pos, colour in enumerate(colour_data):
                if pos == 0:
                    continue
                elif not verify_colour(str(colour)):
                    temp_colour_dict[
                        colour_pos_lookup[pos]] = default_colour_data[colour_pos_lookup[pos]]
                else:
                    temp_colour_dict[colour_pos_lookup[pos]] = str(
                        colour).replace(" ", "")

            logging.info("Colour data set successfully")

            return temp_colour_dict


class MainButtons(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    Loads all of the new account screens buttons
    '''

    def __init__(self, settings_path, username, colour_data, parent, top_parent, *args, **kwargs):  # pylint: disable=too-many-arguments
        '''
        Loads the button frame of the GUI
        '''
        logging.info("Loading main menu button section")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.colour_data = colour_data

        self.settings_path = settings_path

        self.parent = parent
        self.top_parent = top_parent

        self.username = username

        self.permissions = []

        self.config(bg=self.colour_data["background"])

        self.user_group, self.permissions = self.get_group()

        for permission in self.permissions:
            tkinter.Button(self,
                           text=permission.title(),
                           bg=self.colour_data["btn_background"],
                           activebackground=self.colour_data["btn_active"],
                           fg=self.colour_data["foreground"],
                           font=self.colour_data["font"],
                           command=lambda button_pressed=permission: self.menu_option(
                               button_pressed)
                           ).pack(fill=tkinter.BOTH, side=tkinter.TOP, expand=True, padx=2, pady=2)  # pylint: disable=bad-continuation
        tkinter.Label(self,
                      text="",
                      bg=self.colour_data["background"],
                      fg=self.colour_data["foreground"],
                      font=self.colour_data["font"],
                      ).pack(fill=tkinter.BOTH, side=tkinter.TOP, expand=True, padx=2, pady=2)  # pylint: disable=bad-continuation

    def get_group(self):
        '''
        Gets the group name and the group permissions
        '''

        with sqlite3.connect(str(self.settings_path / "loginAccess.db")) as con:
            cur = con.cursor()

            cur.execute("SELECT Permissions_Group FROM Users WHERE Username=?",
                        (HASH_API.hash_text(self.username, secure=False), ))

            group = cur.fetchall()[0][0]

            cur.execute(
                "SELECT Permissions FROM Groups WHERE Group_Name=?", (group, ))

            if group == "owner":
                permissions = ALL_GROUPS[:]
            else:
                # This is only temperary
                permissions = literal_eval(cur.fetchall()[0][0])

        permissions += ["settings", "help"]

        logging.info("Got user permissions")

        return group, permissions

    def menu_option(self, button_pressed):
        '''
        runs the correct command relevant to the button pressed
        '''
        logging.info("Button press for %s", button_pressed)

        if button_pressed == "help":
            logging.info("Loading help screen")
            self.parent.destroy()
            menu_help.Help(self.username, self.settings_path, self.colour_data,
                           self.top_parent).pack(fill=tkinter.BOTH, expand=True)
        elif button_pressed == "settings":
            logging.info("Loading settings main menu")
            self.parent.destroy()
            main_settings.MainMenu(self.settings_path, self.top_parent,
                                   self.username, self.colour_data).pack(fill=tkinter.BOTH, expand=True)

        return


class BottomButtons(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    Loads all of the new account screens buttons
    '''

    def __init__(self, settings_path, top_parent, colour_data, parent, *args, **kwargs):
        '''
        Loads the button frame of the GUI
        '''
        logging.info("Loading main menu bottom buttons")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.colour_data = colour_data

        self.settings_path = settings_path

        self.top_parent = top_parent
        self.parent = parent

        self.config(bg=self.colour_data["background"])

        # Quit button
        tkinter.Button(
            self,
            text="Quit",
            bg=self.colour_data["negetive_btn_background"],
            activebackground=self.colour_data["negetive_btn_active"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            command=lambda: main_login.exit_gui()  # pylint: disable=unnecessary-lambda
        ).pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True, padx=2, pady=2)

        # Back button
        tkinter.Button(
            self,
            text="Log Off",
            bg=self.colour_data["btn_background"],
            activebackground=self.colour_data["btn_active"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            command=lambda: self.logoff()  # pylint: disable=unnecessary-lambda
        ).pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True, padx=2, pady=2)

    def logoff(self):
        '''
        Takes the user back to the login screen
        '''
        logging.info("logging the user off")
        self.parent.destroy()
        main_login.LoginMenu(self.settings_path, self.top_parent).pack(
            fill=tkinter.BOTH,
            expand=True
        )
