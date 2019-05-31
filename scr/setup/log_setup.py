'''
Sets up the logging files and log paths
'''
# Allows for path manipulation
import pathlib
# Converts writen numbers into integers
from scr.utilities.responses import text2int, Illegal_Word


def log_setup():
    '''
    Gets the users log settings
    '''

    get_log_path()
    get_log_limmit()


def get_log_path():
    '''
    Gets the users wanted log path
    '''
    # Sets the default value
    log_path_default = "./logs"

    valid = False

    while not valid:
        log_path = str(
            input("Please enter the location for all log files ([current path]/logs): "))

        if log_path == "":
            log_path = log_path_default

        verify_log_path(log_path)

    return log_path


def verify_log_path(log_path):
    '''
    Verify the path exists or asks them if they want to create it
    '''

    log_path = pathlib.Path(log_path).absolute()

    # Creates the path if it doesn't exist
    log_path.mkdir(exist_ok=True)

    return


def get_log_limmit():
    '''
    Gets the users wanted log limmit
    '''
    log_limmit_default = "0"

    valid = False

    while not valid:
        log_limmit = str(
            input("Please enter the number of logs you wish to store(0 [Unlimited]): "))

        if log_limmit == "":
            log_limmit = log_limmit_default

        valid = verify_log_limmit(log_limmit)

    return log_limmit


def verify_log_limmit(log_limmit):
    '''
    Verifies the limmit to the number of log files
    '''
    validity = False

    # Tests if the input is a number
    try:
        # The value succeeded therefore continue
        log_limmit = int(log_limmit)
        validity = True
    except ValueError:
        # Not a direct number :(

        try:
            # Attempts to convert the words into a number
            log_limmit = text2int(log_limmit)
            validity = True
        except Illegal_Word:
            # text cannot be converted into a string
            print(
                "\nSorry, we didn't understand that, please check your input and try again")
            return validity

    # Ensures the number isn't negetive
    if log_limmit < 0:
        print("\nSorry it cannot be a negetive number, please enter a new number")
        validity = False

    return validity
