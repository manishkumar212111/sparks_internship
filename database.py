import sqlite3

conn = sqlite3.connect('database.db')
'''with sqlite3.connect("database.db") as con:
    cur = con.cursor()
    cur.execute("INSERT INTO users (name,email,credit)    VALUES(?, ?, ?)",("Shalini singh","Shalinisingh002@gmail.com",500) )

    con.commit()
    msg = "Record successfully added"
    print msg
    '''
cur = conn.cursor()
a=cur.execute("select * from users")
a=cur.fetchall()
print a[0][2]
conn.close()