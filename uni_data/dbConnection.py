import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        print("Database connection established.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        raise

# def get_db_connection():
#     # Connect to the database
#     connection = mysql.connector.connect(
#     host="localhost",
#     database="MASTER_ANALYTICS",
#     user="DB_USER",
#     password="DB_PASSWORD"
# )
#     return connection
