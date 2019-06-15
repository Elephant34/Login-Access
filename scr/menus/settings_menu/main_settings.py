'''
Loads the GUI for the settings classes
'''
# For logging
import logging
# For the GUI
import tkinter

# For the title
from scr.menus.title import Title
# for the hashing system API
from scr.utilities.hashing.hash_api import Hash

HASH_API = Hash()


class MainMenu(tkinter.Frame):  # pylint: disable=too-many-ancestors
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

        self.title_fr = Title("Settings", self.colour_data, self)
        self.title_fr.pack(fill=tkinter.X, expand=True,
                           side=tkinter.TOP, padx=5, pady=1)

        logging.info("Logging loaded sucessfully")

        return
