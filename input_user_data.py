import sqlite3

con=sqlite3.connect("library.db")
cursor=con.cursor()


def input_user_data(name,author,publisher,page_number):
    cursor.execute("INSERT INTO bookshelf VALUES(?,?,?,?)",(name,author,publisher,page_number))
    con.commit()

name = input("Name: ")
author = input("Author: ")
publisher = input("Publisher: ")
page_number = int(input("Page Number: "))

input_user_data(name,author,publisher,page_number)

con.close()