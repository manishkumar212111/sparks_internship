from flask import Flask,render_template
import sqlite3
app = Flask(__name__)\

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
    return render_template('view_all_user.html',result=a)




if __name__ == "__main__":
    app.run()