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
                'Public_Username' STRING,
                'Password' STRING NOT NULL,
                'Permissions_Group' STRING NOT NULL,
                'Created_On' STRING DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS Groups (
                'Group_Name' STRING PRIMARY KEY,
                'Permissions' STRING NOT NULL
            )
        """)

    return
