import json,sqlite3
import datetime
val=datetime.date.today()
conn = sqlite3.connect('database.db')
print "Opened database successfully";
cur = conn.cursor()

cur.execute('select *from users')

search ="Manish"

con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute('select *from users where email like "%?%" or name like "%?%"', [search, search])
print cur.fetchall()
conn.close()