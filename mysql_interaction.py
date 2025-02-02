import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="cleverestboo29", 
    database="alx_book_store"
)

cursor = conn.cursor()

cursor.execute("INSERT INTO Authors (author_name) VALUES (%s)", ("J.K. Rowling",))

cursor.execute("SELECT author_id FROM Authors WHERE author_name = %s", ("J.K. Rowling",))
author_id = cursor.fetchone()[0]

cursor.execute("""
    INSERT INTO Books (title, author_id, price, publication_date)
    VALUES (%s, %s, %s, %s)
""", ("Harry Potter and the Sorcerer's Stone", author_id, 19.99, "1997-06-26"))

conn.commit()

cursor.close()
conn.close()

print("Data inserted successfully!")
