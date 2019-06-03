'''
This contians the real setup for the GUI to load
This being run is what really starts the program
'''
import logging
import tkinter
import pathlib
from scr.setup.log_setup import logging_quick_setup


def Run(setting_path, log_path):
    '''
    Starts to load varables, objects and the GUI
    '''

    setting_path = pathlib.Path(setting_path)
    log_path = pathlib.Path(log_path)

    logging_quick_setup(log_path)

    logging.info("Running main program")

    root = tkinter.Tk()

    root.mainloop()

    return
