# db_connection.py
import pymysql

def get_connection():
    return pymysql.connect(
        host='127.0.0.1',
        user="root",
        password="4478",
        db="thatDay",
        charset="utf8"
    )
