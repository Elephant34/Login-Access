
'''
The main file to run to load the login access system
'''
from scr import main_backend

SETTINGS_PATH = r"C:\Users\Ambrose\Documents\Ambrose\ProgramingStuff\Python\Tkinter\Login Access GUI\8.X\Development\settings"  # pylint: disable=line-too-long
LOG_PATH = r"C:\Users\Ambrose\Documents\Ambrose\ProgramingStuff\Python\Tkinter\Login Access GUI\8.X\Development\logs"  # pylint: disable=line-too-long

if __name__ == "__main__":
    main_backend.Run(SETTINGS_PATH, LOG_PATH)

        