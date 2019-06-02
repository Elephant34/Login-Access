'''
Setup file for the settings storage
'''
# Allows for logging
import logging
# Allows for path manipulation
import pathlib
# Gets the valid yes options
from scr.utilities.responses import YES_RESPONSES
# Sets up the main database
from scr.setup.database_setup import database_setup


def setting_setup():
    '''
    Gets the users log settings
    '''

    settings_path = get_settings_path()

    database_path = str(settings_path / "loginAccess.db")

    database_setup(database_path)

    return settings_path


def get_settings_path():
    '''
    Gets the user to input the path to the settings files
    '''
    settings_path_default = "./settings"

    valid = False

    while not valid:

        confirmed = False

        while not confirmed:
            settings_path = str(
                input(
                    "Please enter the location for all setting files ([current path]/settings): ")
            )

            if settings_path.strip() == "":
                settings_path = settings_path_default

            settings_path = pathlib.Path(settings_path).absolute()

            confirmed = confirm_inputs(settings_path)

        valid = verify_settings_path(settings_path)

    logging.info("Settings path created %s", settings_path)

    return settings_path


def verify_settings_path(settings_path, output=True):
    '''
    Verify the path exists or asks them if they want to create it
    '''

    # Creates the path if it doesn't exist
    try:
        settings_path.mkdir(exist_ok=True)
    except FileNotFoundError:
        if output:
            print(
                "\nThat folder couldn't be accessed please check the path and try again")
        logging.warning("Settings folder not found!")
        return False

    return True


def confirm_inputs(settings_path):
    '''
    Checks the user didn't enter any typos
    '''
    if str(input("Are you sure you wish for setting files to be sotred in {path}: ".format(
            path=settings_path))).lower() in YES_RESPONSES:
        return True

    print("Please enter your new inputs:")

    return False
