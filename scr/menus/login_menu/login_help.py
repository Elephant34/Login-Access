'''
Loads the help frame for the users login
'''
# For the GUI
import tkinter
# for logging events
import logging
# For title creation
from scr.menus.title import Title
# To take the user back to the login screen
from scr.menus.login_menu import main_login


class Help(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    Loads all of the help screens methods
    '''

    def __init__(self, settings_path, colour_data, parent, *args, **kwargs):
        '''
        Loads the help frame of the GUI
        '''
        logging.info("Loading help frame")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.settings_path = settings_path

        self.colour_data = colour_data

        self.parent = parent

        self.config(bg=self.colour_data["background"])

        Title("Help:", self.colour_data, self).pack(fill=tkinter.X, expand=True,
                                                    side=tkinter.TOP, padx=5, pady=1)

        Buttons(self.settings_path, self.parent, self.colour_data, self).pack(
            fill=tkinter.X, expand=True, side=tkinter.TOP, padx=5, pady=1)


class Buttons(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    Loads all of the help screens buttons
    '''

    def __init__(self, settings_path, top_parent, colour_data, parent, *args, **kwargs):
        '''
        Loads the button frame of the GUI
        '''
        logging.info("Loading help frame")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.colour_data = colour_data

        self.settings_path = settings_path

        self.top_parent = top_parent
        self.parent = parent

        self.config(bg=self.colour_data["background"])

        tkinter.Button(
            self,
            text="Back",
            bg=self.colour_data["btn_background"],
            activebackground=self.colour_data["btn_active"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            command=lambda: self.back()  # pylint: disable=unnecessary-lambda
        ).pack(fill=tkinter.BOTH, expand=True, padx=2, pady=2)

    def back(self):
        '''
        Takes the user back to the login screen
        '''
        self.parent.destroy()
        main_login.LoginMenu(self.settings_path, self.top_parent).pack(
            fill=tkinter.BOTH,
            expand=True
        )

        return
