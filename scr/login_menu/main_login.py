'''
Stores the main code for the login menu screen seen when the exe is run
'''
# For the logging of key information
import logging
# For handeling GUI comands
import tkinter
# Used to extract the colours
import json


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

        with open(colours_path) as json_file:
            self.colour_data = json.load(json_file)

        parent.config(bg=self.colour_data["background"])
        self.config(bg=self.colour_data["background"])

        self.title_fr = Title(self.colour_data, self)
        self.title_fr.pack(fill=tkinter.X, expand=True,
                           side=tkinter.TOP, padx=5, pady=1)

        self.user_input_fr = UserInputs(self.colour_data, self)
        self.user_input_fr.pack(
            fill=tkinter.X, expand=True, side=tkinter.TOP, padx=5, pady=2)


class Title(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    Stores the title and title spacing of the screen
    '''

    def __init__(self, colour_data, parent, *args, **kwargs):
        '''
        Loads the title frame of the GUI
        '''
        logging.info("Loading title")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.colour_data = colour_data

        self.config(bg=self.colour_data["background"])

        # Label to show the main title text
        tkinter.Label(
            self,
            text="Login:",
            bg=self.colour_data["background"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["title_font"],
            anchor=tkinter.W
        ).pack(fill=tkinter.BOTH, expand=True, side=tkinter.TOP)

        # Spacer label- this may be used to show other text and so is saved
        self.space_lbl = tkinter.Label(
            self,
            text="",
            bg=self.colour_data["background"],
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
            anchor=tkinter.CENTER
        )
        self.space_lbl.pack(fill=tkinter.BOTH, expand=True, side=tkinter.TOP)


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

        # Username entry
        self.password_ent = tkinter.Entry(
            self.password_fr,
            fg=self.colour_data["foreground"],
            font=self.colour_data["font"],
        )
        self.password_ent.pack(
            fill=tkinter.BOTH, expand=True, side=tkinter.RIGHT, padx=3, pady=2)
