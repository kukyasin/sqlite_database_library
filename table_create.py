import sqlite3

con=sqlite3.connect("library.db")
cursor=con.cursor()

def table_create():
    cursor.execute("CREATE TABLE IF NOT EXISTS bookshelf(Name TEXT,Author TEXT,Publisher TEXT,Page_Number INT)")
    con.commit()

table_create()

con.close()