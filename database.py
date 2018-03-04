import json,sqlite3
import datetime
val=datetime.date.today()
conn = sqlite3.connect('database.db')
print "Opened database successfully";
cur = conn.cursor()
now = datetime.datetime.now()
f_credit=10
fro="Manish@gmail.com"
date_string = now.strftime('%Y-%m-%d')
cur.execute("UPDATE users SET credit=? WHERE email=?", [f_credit, fro])
conn.commit()
cur.execute('select *from users')
print cur.fetchall()
conn.close()