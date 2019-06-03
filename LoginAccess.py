
'''
The main file to run to load the login access system
'''
from scr import main_backend

SETTINGS_PATH = r""  # pylint: disable=line-too-long
LOG_PATH = r""  # pylint: disable=line-too-long

if __name__ == "__main__":
    main_backend.Run(SETTINGS_PATH, LOG_PATH)
