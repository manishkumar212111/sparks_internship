from flask import redirect,Flask, render_template, request, url_for
import sqlite3
import datetime

app = Flask(__name__)

def add_database(fro,to,f_credit,t_credit,amount):

    con = sqlite3.connect('database.db')
    cur = con.cursor()
    try:
        cur.execute("UPDATE users SET credit=? WHERE email=?", [int(f_credit), fro])
        con.commit()
        cur.execute("UPDATE users SET credit=? WHERE email=?", [int(t_credit), to])
        con.commit()
        now = datetime.datetime.now()
        date_string = now.strftime('%Y-%m-%d')
        cur.execute("insert into credit values(?,?,?,?)", [fro, to, int(amount), date_string])
        con.commit()
        con.close()

        return "Success"
    except:
        con.rollback()
        return "error in insert operation"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/credit')
def credit():
    return render_template('main.html')


@app.route('/view_all_user')
def view_all_user():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('select * from users')
    a = cur.fetchall()
    con.close()
    return render_template('view_all_user.html', result=a)


@app.route('/credit_transfer')
def credit_transfer():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("select email from users")
    a = cur.fetchall()
    con.close()
    return render_template('credit_transfer.html', result=a)


@app.route('/credit_transfer_submit', methods=['POST', 'GET'])
def credit_transfer_submit():
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    if request.method == 'POST':
        fro = request.form['from']
        to = request.form['to']
        amount = request.form['amount']
        if fro == to:
            cur.execute("select email from users")
            a = cur.fetchall()
            return render_template('credit_transfer.html', result=a, fro=fro, to=to, amount=amount,
                                   message="Sender and reciever must be different")

        if int(amount) > 10000:
            cur.execute("select email from users")
            a = cur.fetchall()
            return render_template('credit_transfer.html', result=a, fro=fro, to=to, amount=amount,
                                   message="Amount must be smaller than 10000")

        cur.execute("select credit from users where email=?", [fro])
        a = cur.fetchall()
        if a is None:
            cur.execute("select email from users")
            a1 = cur.fetchall()
            return render_template('credit_transfer.html', result=a1, fro=fro, to=to, amount=amount,
                                   message="Unknown error")
        if int(a[0][0]) < int(amount):
            cur.execute("select email from users")
            a1 = cur.fetchall()
            return render_template('credit_transfer.html', result=a1, fro=fro, to=to, amount=amount,
                                   message="insufficient balance")
        f_credit = int(a[0][0])
        cur.execute("select credit from users where email=?", [to])
        a = cur.fetchall()
        if a is None:
            cur.execute("select email from users")
            a1 = cur.fetchall()
            return render_template('credit_transfer.html', result=a1, fro=fro, to=to, amount=amount,
                               message="insufficient balance")

        t_credit = int(a[0][0])

        f_credit = f_credit - int(amount)
        t_credit = t_credit + int(amount)
        con.commit()
        return add_database(fro,to,f_credit,t_credit,amount)
        return redirect(url_for('credit_transfer_submit'))
    cur.execute("select email from users")

    a = cur.fetchall()
    con.close()
    return render_template('credit_transfer.html', result=a, message="Successfully Transferred credit")


@app.route('/search',methods=['POST','GET'])
def search():
    if request.method=='POST':
        search=request.form['search']

        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute('select *from users where email=? or name=?',[search,search])
        a=cur.fetchall()
        if a is None:
            return render_template('main.html',message=a)
        else:
            return render_template('main.html', notfound="Norecprd found")

    return render_template('main.html',message="error")


if __name__ == "__main__":
    app.run()
