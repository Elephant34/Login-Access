'''
Sets up the logging files and log paths
'''
# Allows for path manipulation
import pathlib
# Converts writen numbers into integers
from scr.utilities.text2int import text2int, Illegal_Word


def log_setup():
    '''
    Gets the users log settings
    '''

    # get_log_path()
    get_log_limmit()


def get_log_path():
    '''
    Gets the users wanted log path
    '''
    # Sets the default value
    log_path = pathlib.Path("./logs")

    log_path = str(
        input("Please enter the location for all log files (./logs): "))

    return log_path


def get_log_limmit():
    '''
    Gets the users wanted log limmit
    '''
    log_limmit = "0"

    valid = False

    while not valid:
        log_limmit = str(
            input("Please enter the number of logs you wish to store(0 [Unlimited])"))

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
            pass

    # Ensures the number isn't negetive
    if log_limmit < 0:
        validity = False

    return validity
