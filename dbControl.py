from typeBook import *

import sqlite3 # built-in library (Python 2.x & 3.x)

class dbControl :
    dbpath = "BooksDB.db"
    con = sqlite3.connect(dbpath)
    cursor = con.cursor()

    def __init__(self):
        return

    def makeListAll(self):
        script = """ SELECT * FROM Books """

        self.cursor.execute(script)

        Books = self.cursor.fetchall()

        bookList = []

        for title, author in Books:
            bookList.append(typeBook(title, author))

        return bookList

    def SearchAuthor(self, name):

        script = """ SELECT * FROM Books WHERE author = %s""" %name 

        self.cursor.execute(script)

        Books = self.cursor.fetchall()

        bookList = []

        for title, author in Books:
            bookList.append(typeBook(title, author))

        return bookList



    def SearchTitle(self, name):

        script = """ SELECT * FROM Books WHERE author = %s""" %name 

        self.cursor.execute(script)

        Books = self.cursor.fetchall()

        bookList = []

        for title, author in Books:
            bookList.append(typeBook(title, author))

        return bookList
        




    

