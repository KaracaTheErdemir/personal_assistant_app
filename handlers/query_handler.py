# db_queries.py

import psycopg2
import logging
from psycopg2.extras import RealDictCursor

from config_manager import get_database_config

def connect_db():
    try:
        db_config = get_database_config()
        connection = psycopg2.connect(
            database = db_config['database'],
            user = db_config['user'],
            password = db_config['password'],
            host = db_config['host'],
            port = db_config['port']
        )
        return connection
    except Exception as error:
        print("Error connecting to the database:", error)
        return None

def insert_data(table_name, data):
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            columns = ', '.join(data.keys())
            values = ', '.join([f"%({key})s" for key in data.keys()])
            insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
            cursor.execute(insert_query, data)
            connection.commit()
            logging.info(f"Data inserted into table '{table_name}'")
        except Exception as error:
            logging.info("Error inserting data:", error)
        finally:
            cursor.close()
            connection.close()

def fetch_data(query):
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor(cursor_factory=RealDictCursor)
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as error:
            logging.info("Error fetching data:", error)
            return None
        finally:
            cursor.close()
            connection.close()

def update_data(option):
    try:
        logging.info(f"Updating data for option: {option}")
        # Database update logic here
        return f"Data for {option} updated successfully."
    except Exception as e:
        logging.error(f"Error updating data: {type(e).__name__} - {str(e)}")
        return "An error occurred while updating data."

# Example Usage:
# insert_data("your_table", {"column1": "value1", "column2": "value2"})
# data = fetch_data("SELECT * FROM your_table WHERE condition")
# print(data)
