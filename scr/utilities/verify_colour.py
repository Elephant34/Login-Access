'''
Used for checking colour strings are valid
'''
from colour import Color


def verify_colour(colour_string):
    '''
    Checks the given string is a valid colour
    or hex colour value
    '''
    if colour_string == "":
        return False
    try:
        colour_string = colour_string.replace(" ", "")
        Color(colour_string)
        # if everything goes fine then return True
        return True
    except ValueError:  # The color code was not found
        return False

    return True
