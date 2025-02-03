import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store;"
            cursor.execute(create_db_query)
            connection.commit()
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

create_database()


            
        