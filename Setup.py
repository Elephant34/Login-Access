'''
This sets up the program for the user
'''
# Allows for manipulation of paths
import pathlib
# Allows for hashing of owners username and password
from scr.utilities.hashing import hash_api
# Calls the setup code moduals
from scr.setup import log_setup

VERSION = "Development"

HASHING = hash_api.Hash()

SETTING_PATH = pathlib.Path("./settings")

if __name__ == "__main__":
    print(
        "Welcome to Login Access!\nVersion-{version}\n".format(version=VERSION))

    print("Please follow these setup steps carfully:")
    print("Press enter for defaults in brackets ()")

    # Sets up the log files
    log_setup.log_setup()

    SETTING_PATH = str(
        input("Please enter the location to save setting files: (./settings)"))

    OWNER_NAME = HASHING.hash_text(
        input("Please enter the owner name: "), secure=False)
