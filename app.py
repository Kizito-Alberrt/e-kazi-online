from logging import debug
from flask import Flask,render_template,url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User:
    def _init_(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password 

    def _repr_(self):
        return f'<User: {self.username}>'

users = []
users.append(users(id=1, username='Derrick', password='password'))   
   




@app.route('/')
def home():
    return render_template('login.html' 'register.html')
    


if __name__ =='__main__':
    app.run(debug=True)