import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# cursor.execute("create table test(id int primary key," \
# "name varchar(10));")

# cursor.execute("insert into test(name, id) Values('Arian', 1)")
# cursor.execute("insert into test(name, id) Values('Sepehr', 2)")

table = cursor.execute("select * from test")
print(table.fetchall())

