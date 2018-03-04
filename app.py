from flask import Flask, render_template, request, url_for
import sqlite3
import datetime

app = Flask(__name__)
con = sqlite3.connect('database.db')
cur = con.cursor()


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
    cur.execute('select * from users')
    a = cur.fetchall()
    return render_template('view_all_user.html', result=a)


@app.route('/credit_transfer')
def credit_transfer():
    cur.execute("select email from users")
    a = cur.fetchall()

    return render_template('credit_transfer.html', result=a)


@app.route('/credit_transfer_submit', methods=['POST', 'GET'])
def credit_transfer_submit():
    if request.method:
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
            a = cur.fetchall()
            return render_template('credit_transfer.html', result=a, fro=fro, to=to, amount=amount,
                                   message="Unknown error")
        if int(a[0][0]) < int(amount):
            cur.execute("select email from users")
            a = cur.fetchall()
            return render_template('credit_transfer.html', result=a, fro=fro, to=to, amount=amount,
                                   message="insufficient balance")
        f_credit = a[0][0]
        cur.execute("select credit from users where email=?", [to])
        a = cur.fetchall()
        t_credit = a[0][0]

        f_credit = f_credit - int(amount)
        t_credit = t_credit + int(amount)
        cur.execute("UPDATE users SET credit=? WHERE email=?", [f_credit], [fro])
        cur.execute("UPDATE users SET credit=? WHERE email=?", [t_credit], [to])
        cur.execute("insert into credit values(?,?,?)", [fro], [to], amount, datetime.date.today())
        return reduce(url_for('credit_transfer_submit'))
    cur.execute("select email from users")
    a = cur.fetchall()

    return render_template('credit_transfer.html', result=a, message="Successfully Transferred credit")


if __name__ == "__main__":
    app.run()
