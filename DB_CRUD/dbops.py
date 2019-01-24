import config as cf
import mysql.connector

#connect to database
def connect():
    conn = mysql.connector.connect (
            host=cf.database_config["host"],
            user=cf.database_config["user"],
            password=cf.database_config["password"],
            database=cf.database_config["database"]
        )
    return conn