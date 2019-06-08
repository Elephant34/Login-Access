'''
This contians the real setup for the GUI to load
This being run is what really starts the program
'''
# For logging values
import logging
# To handel the GUI widgets
import tkinter
# To contain the relevant path information
import pathlib
# Sets up the logging system to the right directory
from scr.setup.log_setup import logging_quick_setup
# To open the main login menu
from scr.menus.login_menu.main_login import LoginMenu
# To open the static files
from scr.utilities.resource_path import resource_path


def Run(setting_path, log_path):
    '''
    Starts to load varables, objects and the GUI
    '''

    setting_path = pathlib.Path(setting_path).absolute()
    log_path = pathlib.Path(log_path).absolute()

    logging_quick_setup(log_path)

    logging.info("Running main program")

    root = tkinter.Tk()

    root.title("Login Access")
    root.wm_iconbitmap(resource_path("./scr/static_resources/mainIcon.ico"))

    # Loads the login menu screen
    LoginMenu(setting_path, root).pack(fill=tkinter.BOTH, expand=True)

    root.mainloop()

    return
