import os
import psycopg2
import psycopg2.extras
import tabulate
from dotenv import load_dotenv


def get_database():
    """
    Used for testing standard queries in SQL.
    """
    load_dotenv()

    host= os.getenv('HOST')
    user = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    dbname = os.getenv('DBNAME') 
    port = os.getenv('PORT')

    conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port, 
                            cursor_factory=psycopg2.extras.DictCursor)
    cur = conn.cursor()
    cur.execute("SELECT * FROM sales")
    column_names = [desc[0] for desc in cur.description]

    return cur.fetchall(), column_names