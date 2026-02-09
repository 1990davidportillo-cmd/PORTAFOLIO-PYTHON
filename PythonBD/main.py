import sys
import mysql.connector as mysql
from db_connect import get_conn, DB_NAME

def connect():
    return get_conn(DB_NAME)

def listar_series(limit=10):
    with connect() as conn:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("""
                SELECT serie_id, titulo, año_lanzamiento, genero
                FROM series
                ORDER BY serie_id
                LIMIT %s
            """, (limit,))

            rows = cur.fetchall()

            if not rows:
                print("No hay series")

            for r in rows:
                print(r)

listar_series()
