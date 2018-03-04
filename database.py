import sqlite3

conn = sqlite3.connect('database.db')
print "Opened database successfully";

conn.execute('insert into users values("Rakesh","rakesh@gmail.com","500")')
print "Table created successfully";
conn.close()