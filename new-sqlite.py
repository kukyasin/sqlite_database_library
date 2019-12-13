import sqlite3

con=sqlite3.connect("library.db")
cursor=con.cursor()

def table_create():
    cursor.execute("CREATE TABLE IF NOT EXISTS bookshelf(Name TEXT,Author TEXT,Publisher TEXT,Page_Number INT)")
    con.commit()

def add_data():
    cursor.execute("INSERT INTO bookshelf VALUES ('Book 1','Author 1','Publisher 1','Page Number 1')")
    con.commit()

def add_data2(name,author,publisher,page_number):
    cursor.execute("INSERT INTO bookshelf VALUES(?,?,?,?)",(name,author,publisher,page_number))
    con.commit()

# table_create()

# add_data()

name = input("Name: ")
author = input("Author: ")
publisher = input("Publisher: ")
page_number = int(input("Page Number: "))

add_data2(name,author,publisher,page_number)

con.close()