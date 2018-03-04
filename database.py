from flask import redirect,Flask, render_template, request, url_for
import sqlite3
import datetime


con = sqlite3.connect('database.db')
cur = con.cursor()

fro = "Manish@gmail.com"
to = "Rohan@gmail.com"
amount = "200"
cur.execute("select credit from users where email=?", [fro])
a = cur.fetchall()
print a
f_credit = int(a[0][0])
cur.execute("select credit from users where email=?", [to])
a = cur.fetchall()
print a
t_credit = int(a[0][0])
f_credit = f_credit - int(amount)
t_credit = t_credit + int(amount)
cur.execute("UPDATE users SET credit=? WHERE email=?", (int(f_credit), fro))
con.commit()
cur.execute("UPDATE users SET credit=? WHERE email=?", (int(t_credit), to))
con.commit()
now = datetime.datetime.now()
date_string = now.strftime('%Y-%m-%d')
cur.execute("insert into credit values(?,?,?,?)", (fro, to, int(amount), date_string))
con.commit()
cur.execute('select *from users')
print cur.fetchall()
cur.execute('select *from credit')
print cur.fetchall()