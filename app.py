from flask import Flask,render_template

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




if __name__ == "__main__":
    app.run()