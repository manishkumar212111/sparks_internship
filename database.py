import json,sqlite3
import datetime
val=datetime.date.today()
conn = sqlite3.connect('database.db')
print "Opened database successfully";
cur = conn.cursor()
now = datetime.datetime.now()
date_string = now.strftime('%Y-%m-%d')
fro="adkhfjsfh"
to="sdfsfjf"
amount=50
cur.execute('insert into credit values(?,?,?,?)',[fro, to, amount, date_string])
conn.commit()

cur.execute('select *from credit')
print cur.fetchall()
conn.close()