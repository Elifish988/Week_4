import psycopg2
from psycopg2 import pool
from flask_sqlalchemy import SQLAlchemy


connection_pool = psycopg2.pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            dbname="missions_wwii",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )

def get_db_connection():
    if connection_pool:
        conn = connection_pool.getconn()
        return conn


def release_db_connection(conn):
    connection_pool.putconn(conn)



db = SQLAlchemy()

