'''
Sets up the logging files and log paths
'''
# The main logging libary
import logging
# Allows for path manipulation
import pathlib
# gets the current datetime string
from datetime import datetime
# Converts writen numbers into integers
from scr.utilities.responses import text2int, Illegal_Word, YES_RESPONSES


def log_setup():
    '''
    Gets the users log settings
    '''

    log_path = get_log_path()
    log_limmit = get_log_limmit()

    (log_path / "log_limmit.txt").write_text(str(log_limmit))

    logging_quick_setup(log_path)

    return log_path


def logging_quick_setup(log_path):
    '''
    Quickly sets up the log file when given the log path
    '''

    log_name = "{file_name}.log".format(
        file_name=str(datetime.now())[:-7].replace(":", "-"))

    # Sets up logging configurations
    logging.basicConfig(filename=log_path / log_name,
                        format='%(asctime)s:%(module)s:\n%(levelname)s:%(message)s\n',
                        level=logging.INFO)

    logging.info("Log initilization Successful")

    # Retrives the log limmit number
    log_limmit = int((log_path / "log_limmit.txt").read_text())

    # 0 is infinate so these steps will not need to happen
    if log_limmit != 0:
        log_list = sorted(list(log_path.glob("*.log")), reverse=True)
        del log_list[:log_limmit]

        logging.info("Clearing excess logs")

        for log_file in log_list:
            log_file.unlink()
            logging.info("Log file removed")

        logging.info("All log files removed successfully")


def confirm_inputs(log_path):
    '''
    Checks the user didn't enter any typos
    '''
    if str(input("Are you sure you wish for log files to be sotred in {path}: ".format(
            path=log_path))).lower() in YES_RESPONSES:
        return True

    print("Please enter your new inputs:")

    return False


def get_log_path():
    '''
    Gets the users wanted log path
    '''
    # Sets the default value
    log_path_default = "./logs"

    valid = False

    while not valid:

        confirmed = False

        while not confirmed:
            log_path = str(
                input("Please enter the location for all log files ([current path]/logs): "))

            # Removes any unwanted white space
            if log_path.strip() == "":
                log_path = log_path_default

            log_path = pathlib.Path(log_path).absolute()

            confirmed = confirm_inputs(log_path)

        valid = verify_log_path(log_path)

    return log_path


def verify_log_path(log_path, output=True):
    '''
    Verify the path exists or asks them if they want to create it
    '''

    # Creates the path if it doesn't exist
    try:
        log_path.mkdir(exist_ok=True)
    except FileNotFoundError:
        if output:
            print(
                "\nThat folder couldn't be accessed please check the path and try again")
        return False

    return True


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


def verify_log_limmit(log_limmit, output=True):
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
            if output:
                print(
                    "\nSorry, we didn't understand that, please check your input and try again")
            return validity

    # Ensures the number isn't negetive
    if log_limmit < 0:
        if output:
            print("\nSorry it cannot be a negetive number, please enter a new number")
        validity = False

    return validity
