import sqlite3 


dbpath = "BooksDB.db"
con = sqlite3.connect(dbpath)
cursor = con.cursor()

f = open("책목록.txt", 'r', encoding='UTF8')

script = "CREATE TABLE Books(Title text, Author text);"
cursor.execute(script)

while (1):

    title = f.readline()
    if not title : break
    author = f.readline()
    if not author : break

    script = "INSERT INTO Books VALUES(%s, %s);" % (title,author)
  
    cursor.execute(script)

con.commit()

script = "SELECT * FROM books;"
cursor.execute(script)

result = cursor.fetchall()

for n in result :
    print(n)

f.close
