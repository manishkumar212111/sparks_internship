import json,sqlite3
import datetime
val=datetime.date.today()
conn = sqlite3.connect('database.db')
print "Opened database successfully";
cur = conn.cursor()

cur.execute('select *from users')
print cur.fetchall()
conn.close()