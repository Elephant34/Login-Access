'''
The main menu veiwed on login
'''
# For GUI construction
import tkinter
# For logging events
import logging
# For handeling the database
import sqlite3
# For creating the title
from scr.menus.title import Title
# For hashing
from scr.utilities.hashing.hash_api import Hash

HASH_API = Hash()


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

        title_lbl = Title("Welcome {}!".format(
            self.username), self.colour_data, self)
        title_lbl.pack(fill=tkinter.X, expand=True, padx=5, pady=1)

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
                title_font INTEGER NOT NULL,
                subtitle_font INTEGER NOT NULL,
                FOREIGN KEY (Username) REFERENCES Users (Username) ON UPDATE CASCADE ON DELETE CASCADE
                )
            """)

            cur.execute(
                """SELECT * FROM Colours WHERE Username=?""", (self.username_hash,))

            colour_data = cur.fetchall()[0]

            logging.info("Colour data set successfully")

            return default_colour_data
