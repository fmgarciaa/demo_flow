import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

# Database credentials
db_host = os.getenv('HOST')
db_port = os.getenv('PORT')
db_name = os.getenv('DBNAME')
db_user = os.getenv('USER')
db_password = os.getenv('PASSWORD')


def extract():
    try:
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password
        )

        cur = conn.cursor()
        cur.execute('select leg_mat_ps_, leg_mat_id_ from edw_dp_sales_report.dim_material_all limit 50;')
        rows = cur.fetchall()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        cur.close()
        conn.close()
