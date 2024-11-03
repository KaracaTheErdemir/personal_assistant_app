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

def fetch_data(table_name, limit = 10):
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor(cursor_factory=RealDictCursor)
            fetch_query = f"SELECT * FROM {table_name} LIMIT %s"
            cursor.execute(fetch_query, (limit,))
            result = cursor.fetchall()
            logging.info(f"Fetch data from table: '{table_name}'")
            print(result)
            return result
        except Exception as error:
            logging.info("Error fetching data:", error)
            return None
        finally:
            cursor.close()
            connection.close()

def update_data(table_name, data):
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            update_column, update_value = list(data.items())[1]
            identifier_column, identifier_value = list(data.items())[0]
            insert_query = f"UPDATE {table_name} SET {update_column} = '{update_value}' WHERE {identifier_column} = '{identifier_value}';"
            cursor.execute(insert_query, data)
            connection.commit()
            logging.info(f"Data inserted into table '{table_name}'")
        except Exception as error:
            logging.error("Error inserting data:", error)
        finally:
            cursor.close()
            connection.close()

# Example Usage:
# insert_data("your_table", {"column1": "value1", "column2": "value2"})
# data = fetch_data("SELECT * FROM your_table WHERE condition")
# print(data)

def delete_data(table_name, data):
    # will be corrected
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            column_name, column_value = list(data.items())[0]
            delete_query = f"DELETE FROM {table_name} WHERE {column_name} = %s"
            cursor.execute(delete_query, (column_value,))
            connection.commit()
            logging.info(f"Data deleted from table '{table_name}'")
        except Exception as error:
            logging.info("Error deleting data:", error)
        finally:
            cursor.close()
            connection.close()