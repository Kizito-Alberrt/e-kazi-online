from logging import debug
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('auth/login.html')


if __name__ =='__main__':
    app.run(debug=True)