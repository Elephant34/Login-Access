'''
Used to load the GUI for account creation
It will then pass the values to the new acount functionality code for
the account to be added
'''
# For the GUI
import tkinter
# For logging key enets
import logging


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
