'''
Creates a title for the menu with a space underneath
'''
# For creating the GUI
import tkinter
# For logging key events
import logging


class Title(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    Stores the title and title spacing of the screen
    '''

    def __init__(self, text, colour_data, parent, *args, **kwargs):
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
            text=text,
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
