# db_queries.py

import psycopg2
from psycopg2.extras import RealDictCursor

def connect_db():
    try:
        connection = psycopg2.connect(
            database="your_database",
            user="your_user",
            password="your_password",
            host="localhost",
            port="5432"
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
            print(f"Data inserted into table '{table_name}'")
        except Exception as error:
            print("Error inserting data:", error)
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
            print("Error fetching data:", error)
            return None
        finally:
            cursor.close()
            connection.close()

# Example Usage:
# insert_data("your_table", {"column1": "value1", "column2": "value2"})
# data = fetch_data("SELECT * FROM your_table WHERE condition")
# print(data)
