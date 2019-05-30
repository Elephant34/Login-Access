'''
Sets up the logging files and log paths
'''
# Alls for path manipulation
import pathlib


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
    log_path = pathlib.Path("./logs")

    log_path = str(
        input("Please enter the location for all log files (./logs): "))

    return log_path


def get_log_limmit():
    '''
    Gets the users wanted log limmit
    '''
    log_limmit = "0"

    log_limmit = str(
        input("Please enter the number of logs you wish to store(0 [Unlimited])"))

    return log_limmit
