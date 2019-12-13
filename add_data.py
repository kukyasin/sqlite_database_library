import sqlite3

con=sqlite3.connect("library.db")
cursor=con.cursor()

def add_data():
    cursor.execute("INSERT INTO bookshelf VALUES ('Book 2','Author 2','Publisher 2','Page Number 2')")
    con.commit()

add_data()

con.close()