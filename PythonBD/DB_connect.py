import mysql.connector as mysql

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = '123456'
DB_NAME = 'NetflixDB'

def get_conn(db=None):
    return mysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=db
    )

get_conn()
