# database/db_Connection.py
import oracledb

def get_connection():
    return oracledb.connect(
        user="userpy",
        password="qqqq",
        dsn="localhost:1521/xepdb1"
    )
