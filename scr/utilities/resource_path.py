'''
This is used to get static files from the pyinstaller executable
'''
import sys
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)  # pylint: disable = protected-access, no-member

    return os.path.join(os.path.abspath("."), relative_path)
