'''
This sets up the program for the user
'''
# Allows for logging of events
import logging
# Allows for the moderfication of file paths
import pathlib
# Allows the program to call commands
from os import system
# Calls the setup code moduals
from scr.setup import log_setup, setting_setup, owner_setup

VERSION = "Development"

if __name__ == "__main__":
    print(
        "Welcome to Login Access!\nVersion-{version}\n".format(version=VERSION))

    print("Please follow these setup steps carfully:")
    print("Press enter for defaults in brackets ()")

    # Sets up the log files
    LOG_PATH = log_setup.log_setup()

    logging.info("Log setup complete")

    logging.info("Settings setup starting")
    SETTING_PATH = setting_setup.setting_setup()
    logging.info("Settings setup complete")

    logging.info("Owner account creation started")
    owner_setup.owner_setup(SETTING_PATH / "loginAccess.db")
    logging.info("Owner account creation completed successfuly")

    logging.info("Started executable setup")

    FILE_PATH = pathlib.Path("./LoginAccess.py").absolute()

    with open(FILE_PATH, "w") as file:
        file.write("""
'''
The main file to run to load the login access system
'''
from scr import main_backend

SETTINGS_PATH = r"{settings_path}"  # pylint: disable=line-too-long
LOG_PATH = r"{log_path}"  # pylint: disable=line-too-long

if __name__ == "__main__":
    main_backend.Run(SETTINGS_PATH, LOG_PATH)

        """.format(settings_path=SETTING_PATH, log_path=LOG_PATH))

    logging.info("Paths written to LoginAccess.py")

    logging.info("Attempt to create executable")

    system("pyinstaller loginAccess.spec")

    logging.info("executable created successfully")
