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

        self.config(bg=self.colour_data["background"])

        self.title_lbl = Title(self.colour_data, self)
        self.title_lbl.pack(fill=tkinter.X, expand=True, side=tkinter.TOP)


class Title(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    Stores the title and title spacing of the screen
    '''

    def __init__(self, colour_data, parent, *args, **kwargs):
        '''
        Loads the main frame of the GUI
        '''
        logging.info("Loading title")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.colour_data = colour_data

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
