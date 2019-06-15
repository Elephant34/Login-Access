'''
Loads the help frame for the main menu
'''
# For the GUI
import tkinter
# for logging events
import logging
# For opening the wiki
import webbrowser
# For title creation
from scr.menus.title import Title
# To take the user back to the main menu
from scr.menus.main_menu import main_menu


class Help(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    Loads all of the help screens methods
    '''

    def __init__(self, username, settings_path, colour_data, parent, *args, **kwargs):
        '''
        Loads the help frame of the GUI
        '''
        logging.info("Loading help frame")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.settings_path = settings_path

        self.colour_data = colour_data

        self.parent = parent

        self.username = username

        self.config(bg=self.colour_data["background"])

        Title("Help:", self.colour_data, self).pack(fill=tkinter.X, expand=True,
                                                    side=tkinter.TOP, padx=5, pady=1)

        # The main help text container
        help_message = (
            "Welcome to Login Access Help, on the main menu pressing any button "
            "will allow you to interact with that feature of the program "
            "if you cannot see any buttons or they are not working "
            "please contact your system administator. If you have any other question about how "
            "this sytem works please see the wiki by pressing the button below. "
            "Thank you\n"
        )
        message = tkinter.Message(
            self,
            text=help_message,
            bg=self.colour_data["background"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            anchor=tkinter.W
        )
        message.pack(fill=tkinter.BOTH, expand=True,
                     side=tkinter.TOP, padx=5, pady=3)

        Buttons(self.settings_path, self.username, self.parent, self.colour_data, self).pack(
            fill=tkinter.X, expand=True, side=tkinter.TOP, padx=5, pady=1)

        message.bind(
            "<Configure>", lambda e: message.config(width=e.width-10))


class Buttons(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    Loads all of the help screens buttons
    '''

    def __init__(self, settings_path,  # pylint: disable=too-many-arguments
                 username, top_parent, colour_data, parent, *args, **kwargs):
        '''
        Loads the button frame of the GUI
        '''
        logging.info("Loading help buttons")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.colour_data = colour_data

        self.settings_path = settings_path

        self.top_parent = top_parent
        self.parent = parent

        self.username = username

        self.config(bg=self.colour_data["background"])

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

        # Wiki butten to load the full github wiki
        tkinter.Button(
            self,
            text="Wiki",
            bg=self.colour_data["btn_background"],
            activebackground=self.colour_data["btn_active"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            command=lambda: self.load_wiki()  # pylint: disable=unnecessary-lambda
        ).pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True, padx=2, pady=3)

    def back(self):
        '''
        Takes the user back to the login screen
        '''
        logging.info("Exiting the help menu")
        self.parent.destroy()
        main_menu.MainMenu(self.settings_path, self.top_parent, self.username,
                           self.colour_data).pack(fill=tkinter.BOTH, expand=True)

        return

    def load_wiki(self):  # pylint: disable=no-self-use
        '''
        Opens the github wiki page
        https://github.com/Elephant34/Login-Access/wiki
        '''
        logging.info("Loading the wiki page")

        webbrowser.open(
            "https://github.com/Elephant34/Login-Access/wiki/")

        return
