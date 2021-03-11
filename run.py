from logging import debug
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/apply')
def apply():
    return render_template('apply.html')

@app.route('/login')
def login():
    return render_template('login.html')







if __name__ =='__main__':
    app.run(debug=True)