from flask import Flask, render_template, redirect, url_for
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TRARDOWN'] = True
db = SQLAlchemy(app)


class UserAddForm(Form):
    username = StringField('Username')
    # password = PasswordField('Password')
    # telephone = StringField('Telephone')
    # email = StringField('Email')
    # validate = BooleanField('validate')
    # submit = SubmitField('')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return redirect(url_for('index', username=request.form['username']))
    else:
        return render_template('login.html')


@app.route("/index/<username>", methods=['POST', 'GET'])
def index(username):
    if request.method == 'POST':
        print 'tt'
        form = UserAddForm()
        print form.username.data


    else:
        return render_template('index.html', username=username)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/save')
def save_user():
    print 'dd111'


if __name__ == '__main__':
    app.run(debug=True)


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(100), unique=True)
    telephone = db.column(db.String(20))
    email = db.column(db.String(20))
    password = db.column(db.String(20))
    validate = db.column(db.Boolean)

    def __repr__(self):
        return '<User %r>' % self.username
