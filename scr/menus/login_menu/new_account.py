'''
Used to load the GUI for account creation
It will then pass the values to the new acount functionality code for
the account to be added
'''
# For the GUI
import tkinter
# For logging key enets
import logging
# To display the title
from scr.menus.title import Title
# TO go back to the main login screen
from scr.menus.login_menu import main_login
# For account creation
from scr.account_handlers.new_account import NewAccount


class NewAccountGUI(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    Loads all of the new account GUI widgets
    '''

    def __init__(self, settings_path, colour_data, parent, *args, **kwargs):
        '''
        Loads the new account frame of the GUI
        '''
        logging.info("Loading new account GUI frame")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.settings_path = settings_path

        self.colour_data = colour_data

        self.parent = parent

        self.config(bg=self.colour_data["background"])

        self.title_lbl = Title("New Account:", self.colour_data, self)
        self.title_lbl.pack(fill=tkinter.X, expand=True,
                            side=tkinter.TOP, padx=5, pady=1)

        # Loads the area for the user to enter their username and password
        self.user_input_fr = UserInputs(self.colour_data, self)
        self.user_input_fr.pack(
            fill=tkinter.X, expand=True, side=tkinter.TOP, padx=3, pady=2)
        # Fucuses the mouse cursor on the username entry
        self.user_input_fr.username_ent.focus()

        self.buttons_fr = Buttons(
            self.settings_path, self.parent, self.colour_data, self)
        self.buttons_fr.pack(
            fill=tkinter.X, expand=True, side=tkinter.TOP, padx=5, pady=1)

        # Sets the username to focus on the password when enter is pressed
        self.user_input_fr.username_ent.bind(
            "<Return>",
            lambda e: self.user_input_fr.password_ent.focus()
        )
        # If enter is pressed when on password entry it will atempt login
        self.user_input_fr.password_ent.bind(
            "<Return>",
            lambda e: self.user_input_fr.repeatpassword_ent.focus()
        )

        self.user_input_fr.repeatpassword_ent.bind(
            "<Return>",
            lambda e: self.buttons_fr.new_account()
        )


class UserInputs(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    The GUI to handel the user inputs
    '''

    def __init__(self, colour_data, parent, *args, **kwargs):
        '''
        Loads the title frame of the GUI
        '''
        logging.info("Loading user inputs")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.colour_data = colour_data

        self.config(bg=self.colour_data["background"])

        self.username_gui()
        self.password_gui()
        self.repeatpassword_gui()

    def username_gui(self):
        '''
        sets up the username entry lable and entry
        '''
        self.username_fr = tkinter.Frame(
            self,
            bg=self.colour_data["background"],
        )

        self.username_fr.pack(fill=tkinter.BOTH, expand=True, side=tkinter.TOP)

        # Username label
        tkinter.Label(
            self.username_fr,
            text="Username:",
            bg=self.colour_data["background"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            anchor=tkinter.CENTER
        ).pack(fill=tkinter.BOTH, expand=True, side=tkinter.LEFT, padx=3, pady=2)

        # Username entry
        self.username_ent = tkinter.Entry(
            self.username_fr,
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
        )
        self.username_ent.pack(
            fill=tkinter.BOTH, expand=True, side=tkinter.RIGHT, padx=3, pady=2)

    def password_gui(self):
        '''
        Sets the password label and entr widgets
        '''
        self.password_fr = tkinter.Frame(
            self,
            bg=self.colour_data["background"],
        )

        self.password_fr.pack(fill=tkinter.BOTH, expand=True, side=tkinter.TOP)

        tkinter.Label(
            self.password_fr,
            text="Password:",
            bg=self.colour_data["background"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            anchor=tkinter.CENTER
        ).pack(fill=tkinter.BOTH, expand=True, side=tkinter.LEFT, padx=3, pady=2)

        # password entry
        self.password_ent = tkinter.Entry(
            self.password_fr,
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            show="•"
        )
        self.password_ent.pack(
            fill=tkinter.BOTH, expand=True, side=tkinter.RIGHT, padx=3, pady=2)

    def repeatpassword_gui(self):
        '''
        Sets the password label and entr widgets
        '''
        self.repeatpassword_fr = tkinter.Frame(
            self,
            bg=self.colour_data["background"],
        )

        self.repeatpassword_fr.pack(
            fill=tkinter.BOTH, expand=True, side=tkinter.TOP)

        tkinter.Label(
            self.repeatpassword_fr,
            text="Repeat Password:",
            bg=self.colour_data["background"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            anchor=tkinter.CENTER
        ).pack(fill=tkinter.BOTH, expand=True, side=tkinter.LEFT, padx=3, pady=2)

        # password entry
        self.repeatpassword_ent = tkinter.Entry(
            self.repeatpassword_fr,
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            show="•"
        )
        self.repeatpassword_ent.pack(
            fill=tkinter.BOTH, expand=True, side=tkinter.RIGHT, padx=3, pady=2)


class Buttons(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    Loads all of the new account screens buttons
    '''

    def __init__(self, settings_path, top_parent, colour_data, parent, *args, **kwargs):
        '''
        Loads the button frame of the GUI
        '''
        logging.info("Loading new account buttons")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.colour_data = colour_data

        self.settings_path = settings_path

        self.top_parent = top_parent
        self.parent = parent

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

        # create account button
        tkinter.Button(
            self,
            text="Create Account",
            bg=self.colour_data["positive_btn_background"],
            activebackground=self.colour_data["positive_btn_active"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            command=lambda: self.new_account()  # pylint: disable=unnecessary-lambda
        ).pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True, padx=2, pady=3)

    def back(self):
        '''
        Takes the user back to the login screen
        '''
        logging.info("Exiting the help menu")
        self.parent.destroy()
        main_login.LoginMenu(self.settings_path, self.top_parent).pack(
            fill=tkinter.BOTH,
            expand=True
        )

        return

    def new_account(self):  # pylint: disable=no-self-use
        '''
        Verifies the new account and creates it
        '''
        logging.info("Loading the new account methods")

        NewAccount(
            self.parent.user_input_fr,
            self.settings_path,
            self.parent.title_lbl.space_lbl
        )

        return
