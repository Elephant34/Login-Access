'''
Loads the help frame for the users login
'''
# For the GUI
import tkinter
# for logging events
import logging


class Help(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    Loads all of the help screens methods
    '''

    def __init__(self, colour_data, parent, *args, **kwargs):
        '''
        Loads the help frame of the GUI
        '''
        logging.info("Loading help frame")
        # The the relevant frame methods
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.colour_data = colour_data

        self.config(bg=self.colour_data["background"])

        tkinter.Label(self, text="HELP STARTED").pack()
