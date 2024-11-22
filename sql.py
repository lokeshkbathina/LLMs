import sqlite3

# connect to sqlite
connection = sqlite3.connect('student.db')

# create a cursor object to inser record, create table, retrieve
cursor = connection.cursor()

# create the table
table_info ="""
CREATE TABLE STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25, SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

# insert some more records
cursor.execute('''INSERT INTO STUDENT VALUES('Adam', 'Data Section', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Baron', 'Computer Vision', 'B', 55)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Caesar', 'AWS', 'A', 70)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Derek', 'Data Section', 'A', 99)''')

# display all the records
print("The inserted records are")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

# close the connection
connection.commit()
connection.close()