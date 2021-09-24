import psycopg2
from config import config


def connect():
    """Connect to PostgreSQL DB Server"""
    conn = None

    try:
        # read connection params
        params = config()

        # connect to the PostgreSQL server
        print("Connection to PostgreSQL Server")
        conn = psycopg2.connect(**params)

        # create a cursor
        curr = conn.cursor()

        # execute a statement
        print("PostgreSQL database version:")
        curr.execute("SELECT version();")

        # display the PostgreSQL database server version
        db_version = curr.fetchone()
        print(db_version)

        # close db connection
        curr.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed")


if __name__ == "__main__":
    connect()
