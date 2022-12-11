"""
D ata
B ase
F unctions

Functions created for interacting with the database programmatically.
Works pretty nicely I think?
"""

import config
import mysql.connector
from mysql.connector import errorcode


class DatabaseFunctions:
    # init a connection pool as to not completely flood the server with connectors lmao
    def __init__(self):
        try:
            conf = config.Config()
            self.cnx = mysql.connector.pooling.MySQLConnectionPool(pool_size=10,
                                                                   pool_name="we_have_one_brain_cell",
                                                                   host=conf.DB_HOST,
                                                                   user=conf.DB_USER,
                                                                   password=conf.DB_PASSWORD,
                                                                   database=conf.DB_DATABASE
                                                                   )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Access is denied. Check username and/or password.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Bad database. Make sure the database exists.")
            else:
                print(err)


    def get_school_ratings(self, school_id:int):
        cnx = self.cnx.get_connection()
        cursor = cnx.cursor()
        # there's probably not 50,000 schools on rmp
        cursor.execute("SELECT * from SCHOOL_INDIVIDUAL_RATING WHERE s_id = %s", (school_id,))
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return result

    
    def get_school_info(self, school_id:int):
        cnx = self.cnx.get_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM school WHERE s_id = %s", (school_id,))
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return result
    

    def get_all_school_info(self):
        cnx = self.cnx.get_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM school LIMIT 100000")
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return result
