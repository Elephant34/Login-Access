'''
Sets the default colours of the program in a json file
These can be changed in the owner/admin menus
'''
# For writing the json to  file
import json
# To record a log of events
import logging
# To handel paths
import pathlib

COLOUR_DEFAULTS = {
    "background": "#7eccf7",
    "foreground": "Black",
    "btn_background": "#2db4ff",
    "btn_active": "#2da9ff",
    "negetive_btn_background": "#ef2804",
    "negetive_btn_active": "#f52804",
    "positive_btn_background": "#1ece18",
    "positive_btn_active": "#159b11",
    "font": ("Arial", 14),
    "title_font": ("Arial", 24, "bold"),
    "subtitle_font": ("Arial", 14, "bold"),
}


def set_default_colours(settings_path):
    '''
    Sets the default colours of the program in a json file
    These can be changed in the owner/admin menus
    '''

    settings_path = pathlib.Path(settings_path).absolute()

    json_path = str(settings_path / "default_colours.json")

    with open(json_path, "w") as json_file:
        json.dump(COLOUR_DEFAULTS, json_file, indent=4)

    logging.info("Writen default colours json file")
