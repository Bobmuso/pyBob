import sqlite3
import pandas as pd

#Creating Database and Connecting to Database in python
conn = sqlite3.connect('books.db')
cursor = conn.cursor()
print('Connected to database successfully')

cursor.execute('SELECT name From sqlite_master WHERE type = "table"; ')
tables = cursor.fetchall()
print('Tables in the database:', tables)

#Create and view authors table
cursor.execute('''CREATE TABLE authors(
                  authorID INTEGER PRIMARY KEY,
                  firstName TEXT NOT NULL,
                  lastName TEXT NOT NULL);''')
authors = [(1, 'J.K', 'Rowling'), (2, 'J.R.R', 'Tolken'), (3, 'Goerge', 'Orwell')]
cursor.executemany('''INSERT INTO authors VALUES (?, ?, ?)''', authors)
conn.commit()

query = '''SELECT *
           FROM authors'''
authorsDf = pd.read_sql_query(query, conn)
print(authorsDf)

#Deleting tables
"""
conn = sqlite3.connect('books.db')
cursor = conn.cursor()
print('Connected to database successfully')

cursor.execute('SELECT name From sqlite_master WHERE type = "table"; ')
tables = cursor.fetchall()
print('Tables in the database:', tables)

for eachTable in tables:
    cursor.execute(f'Drop table {eachTable[0]}')
    print(f'Table {eachTable[0]} dropped')
    
conn.commit()
"""

#Create the titles Table
cursor.execute('''CREATE TABLE titles(
                  ISBN TEXT PRIMARY KEY,
                  title TEXT NOT NULL,
                  editionNumber INTEGER NOT NULL,
                  copyright TEXT NOT NULL);''')

titlesInfo = [('123-456789', 'Harry Potter', 1, '2000'),
              ('234-567891', 'The hobbit', 1, '1937'),
              ('345-126789', '1984', 1, '1949')]
cursor.executemany('''INSERT INTO titles VALUES (?, ?, ?, ?)''', titlesInfo)
conn.commit()

query = '''SELECT *
           FROM titles'''
titlesDf = pd.read_sql_query(query, conn)
print(titlesDf)

cursor.execute('''CREATE TABLE authorISBN(
                  authorID INTEGER,
                  ISBN TEXT,
                  PRIMARY KEY (authorID, ISBN),
                  FOREIGN KEY (authorID) REFERENCE authors(authorID),
                  FOREIGN KEY (ISBN) REFERENCE titles(ISBN);''')

# match Zero or more char
# query = 'SELECT * FROM titles WHERE title LIKE "Harry%"'

#match any char
# query = 'SELECT * FROM authors WHERE firstName = "J._"'

#order by
# query = 'SELECT * FROM titles ORDER BY title'

#sort by multi columns
# query = 'SELECT * FROM authors ORDER BY lastName, firstName'

#combine where and order
# query = 'SELECT * FROM titles WHERE editionNumber = 1 ORDER BY title'

# merge inner join
# query = '''SELECT firstName, lastName, titles
#            FROM authors
#            INNER JOIN authorISBN ON authors.authorID = authorISBN.authorID
#            INNER JOIN titles ON authorsISBN.ISBN = titles.ISBN'''

#update
#query = 'UPDATE authors SET lastName = "Rowling-Morgan" WHERE lastName = "Rowling"'

#delete
#query = 'DELETE FROM authors WHERE lastname = "Rowling-Morgan"'