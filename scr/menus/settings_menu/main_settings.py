'''
Loads the GUI for the settings classes
'''
# For logging
import logging
# For the GUI
import tkinter

# For going back to the main menu
from scr.menus.main_menu import main_menu
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

        Buttons(self.settings_path, self.username, self.username_hash,
                self.colour_data, self, self.top_parent).pack(
                    fill=tkinter.BOTH, side=tkinter.TOP, expand=True, padx=3, pady=3)

        logging.info("Settings loaded sucessfully")

        return


class Buttons(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    Loads all of the new account screens buttons
    '''

    def __init__(self, settings_path, username, username_hash, colour_data, parent, top_parent, *args, **kwargs):  # pylint: disable=too-many-arguments, line-too-long
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
        self.username_hash = username_hash

        self.config(bg=self.colour_data["background"])

        self.settings = ["account settings", "cosmetics",
                         "bug reporter", "suggestions", "advanced"]

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

        return

    def back(self):
        '''
        Takes the user back to the login screen
        '''
        logging.info("Exiting the settings menu")
        self.parent.destroy()
        main_menu.MainMenu(self.settings_path, self.top_parent, self.username,
                           self.colour_data).pack(fill=tkinter.BOTH, expand=True)

        return
