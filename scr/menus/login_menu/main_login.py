'''
Stores the main code for the login menu screen seen when the exe is run
'''
# For the logging of key information
import logging
# For handeling GUI comands
import tkinter
# Used to extract the colours
import json
# To load the help menu
from scr.menus.login_menu.login_help import Help
# For loading the new account GUI
from scr.menus.login_menu.new_account import NewAccountGUI
# For creating the title
from scr.menus.title import Title


class LoginMenu(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    Stores all of the login menu commands and widgets
    '''

    def __init__(self, settings_path, parent, *args, **kwargs):
        '''
        Loads the main frame of the GUI
        '''
        logging.info("Loading main login menu screen")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        colours_path = str(settings_path / "default_colours.json")

        self.top_parent = parent

        self.settings_path = settings_path

        with open(colours_path) as json_file:
            self.colour_data = json.load(json_file)

        parent.config(bg=self.colour_data["background"])
        self.config(bg=self.colour_data["background"])

        # Loads the title
        self.title_fr = Title("Login:", self.colour_data, self)
        self.title_fr.pack(fill=tkinter.X, expand=True,
                           side=tkinter.TOP, padx=5, pady=1)

        self.login_fr = tkinter.Frame(self, bg=self.colour_data["background"])
        self.login_fr.pack(fill=tkinter.X, expand=True,
                           side=tkinter.TOP, padx=5, pady=2)

        # Loads the area for the user to enter their username and password
        self.user_input_fr = UserInputs(self.colour_data, self.login_fr)
        self.user_input_fr.pack(
            fill=tkinter.X, expand=True, side=tkinter.LEFT, padx=3, pady=2)
        # Fucuses the mouse cursor on the username entry
        self.user_input_fr.username_ent.focus()

        # Login buton
        tkinter.Button(
            self.login_fr,
            text="Login",
            bg=self.colour_data["positive_btn_background"],
            activebackground=self.colour_data["positive_btn_active"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            anchor=tkinter.CENTER,
            command=lambda: self.login()  # pylint: disable=unnecessary-lambda
        ).pack(fill=tkinter.BOTH, expand=True, side=tkinter.RIGHT, padx=2, pady=2)

        # Loads the main button frame
        self.button_fr = MainButtons(
            self.settings_path, self.colour_data, self.top_parent, self)
        self.button_fr.pack(fill=tkinter.X, expand=True,
                            side=tkinter.BOTTOM, padx=5, pady=2)

        # Sets the username to focus on the password when enter is pressed
        self.user_input_fr.username_ent.bind(
            "<Return>",
            lambda e: self.user_input_fr.password_ent.focus()
        )
        # If enter is pressed when on password entry it will atempt login
        self.user_input_fr.password_ent.bind(
            "<Return>",
            lambda e: self.login()
        )

        logging.info("Login menu GUI created successfully")

    def login(self):
        '''
        Gets the users inputs hashes them and attempt to login the user in
        '''

        print(str(self.user_input_fr.username_ent.get()))

        return


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
        )
        self.password_ent.pack(
            fill=tkinter.BOTH, expand=True, side=tkinter.RIGHT, padx=3, pady=2)


class MainButtons(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    The GUI to handel the user inputs
    '''

    def __init__(self, settings_path, colour_data, top_parent, parent, *args, **kwargs):
        '''
        Loads the title frame of the GUI
        '''
        logging.info("Loading main buttons (bottom three)")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.top_parent = top_parent

        self.settings_path = settings_path

        self.colour_data = colour_data

        self.config(bg=self.colour_data["background"])

        # Loads the quit button
        tkinter.Button(
            self,
            text="Exit",
            bg=self.colour_data["negetive_btn_background"],
            activebackground=self.colour_data["negetive_btn_active"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            anchor=tkinter.CENTER,
            command=lambda: exit_gui()  # pylint: disable=unnecessary-lambda
        ).pack(fill=tkinter.X, expand=True, side=tkinter.LEFT, padx=2, pady=2)

        # loads the help button
        tkinter.Button(
            self,
            text="Help",
            bg=self.colour_data["btn_background"],
            activebackground=self.colour_data["btn_active"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            anchor=tkinter.CENTER,
            command=lambda: self.load_help()  # pylint: disable=unnecessary-lambda
        ).pack(fill=tkinter.X, expand=True, side=tkinter.LEFT, padx=2, pady=2)

        # loads the new account button
        tkinter.Button(
            self,
            text="New Account",
            bg=self.colour_data["btn_background"],
            activebackground=self.colour_data["btn_active"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            anchor=tkinter.CENTER,
            command=lambda: self.load_new_account()  # pylint: disable=unnecessary-lambda
        ).pack(fill=tkinter.X, expand=True, side=tkinter.LEFT, padx=2, pady=2)

    def load_help(self):
        '''
        loads the help screen toplevel
        '''
        self.parent.destroy()
        Help(self.settings_path, self.colour_data, self.top_parent).pack(
            fill=tkinter.BOTH, expand=True)
        return

    def load_new_account(self):
        '''
        Loads the new account menu
        '''
        self.parent.destroy()
        NewAccountGUI(self.settings_path, self.colour_data, self.top_parent).pack(
            fill=tkinter.BOTH, expand=True)
        return


def exit_gui():
    '''Quits the program'''
    logging.info("Quiting program. Good bye.")
    raise SystemExit
