# coding: UTF-8
from flask import Flask, render_template, redirect, url_for,jsonify
from flask import request,session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from flask.ext.bootstrap import Bootstrap
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from werkzeug.security import generate_password_hash,check_password_hash
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TRARDOWN'] = True
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


class UserAddForm(Form):
    username = StringField('Username')
    # password = PasswordField('Password')
    # telephone = StringField('Telephone')
    # email = StringField('Email')
    # validate = BooleanField('validate')
    # submit = SubmitField('')


@app.route('/login', methods=['POST', 'GET'])
def login():
    """
    登陆函数页面

    """
    if request.method == 'POST':
        print request.form['username']

        return redirect(url_for('index', name='dd')) #返回登陆后的页面
    else:
        return render_template('login.html')#返回登陆页面


@app.route("/index/<name>")
def index(name):
    return render_template('htmls/indexpage.html', name=name)


@app.route('/logout')
def logout():
    print '123'
    return render_template('login.html')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/save')
def save_user():
    print 'dd111'


@app.route('/footer')
def footer_page():
    return render_template('htmls/footer.html')


@app.route('/banner')
def banner_page():
    return render_template('htmls/banner.html')


@app.route('/test')
def test():
    return render_template('login.html')


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
