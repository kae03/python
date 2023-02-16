import sqlite3
conn=sqlite3.connect('emobilis.db')
data=conn.execute("select * from Students")
for row in data:
    print("ID =", row[0])
    print("NAME=", row[0])
    print("AGE=", row[0])
    print("SCHOOL=", row[0],"\n")
conn.close()