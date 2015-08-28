from flask import Flask, render_template, redirect, url_for
from flask import request

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print request.form['username']
        print request.form['password']
        return redirect(url_for('index', username=request.form['username']))
    else:
        return render_template('login.html')


@app.route("/index/<username>")
def index(username):
    return render_template('index.html',username=username)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


