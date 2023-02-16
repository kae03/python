import sqlite3
conn=sqlite3.connect('emobilis.db')
print("opened db successfully")

conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL)VALUES('1','Kae','18','emobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL)VALUES('2','kel','12','Strathmore')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL)VALUES('3','ephy','18','emobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL)VALUES('4','vicky','12','Strathmore')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL)VALUES('5','leena','7','Strathmore')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL)VALUES('46','lisa','11','Strathmore')")

conn.commit()
print("records added successfully")
conn.close()