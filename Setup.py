'''
This sets up the program for the user
'''
#from scr.utilities.hashing import hash_api

VERSION = "Development"

# Sets all the default values
LOG_FILE = r".\logs"
LOG_LIMMIT = "0"

if __name__ == "__main__":
    print(
        "Welcome to Login Access!\nVersion-{version}\n".format(version=VERSION))

    print("Please follow these setup steps carfully:")
    print("Press enter for defaults in brackets ()")

    LOG_FILE = str(
        input(r"Please enter the location for all log files (.\logs): "))
    LOG_LIMMIT = str(
        input("Please enter the number of logs you wish to storezn(0 [Unlimited])"))
    #OWNER_NAME = Hash
