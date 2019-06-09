'''
Sets the the main LoginAccess datbase in the settings folder
'''
# Allows for the manipulation of databases
import sqlite3


def database_setup(databse_path):
    '''
    Creats the main databast tables and default values
    '''

    with sqlite3.connect(databse_path) as con:
        cur = con.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                'Username' STRING PRIMARY KEY,
                'Password' STRING NOT NULL,
                'Group' STRING NOT NULL,
                'Created On' STRING DEFAULT CURRENT_TIMESTAMP
            )
        """)

    return
