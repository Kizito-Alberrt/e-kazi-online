from typing import Text
from app.config import Config
from logging import debug
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template, request, jsonify
from flask import Blueprint
from flaskext.mysql import MySQL


from flask import request
app = Flask(__name__)
mysql = MySQL(app)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_JOB"] = "root"
app.config["MYSQL_DESCRIPTION"] = ""
app.config["MYSQL_DB"] = ""
app.config["MYSQL_CURSORCLASS"] = "DirectCursor"




db = SQLAlchemy(app)



 forms
=======
posts = Blueprint('jobs', __name__, template_folder ='templates')
 master
@app.route('/')
def home():
    return render_template('home.html')

@app.route("/livesearch", methods=["POST","GET"])
def livesearch():
    searchbox = request.form.get(Text)
    cursor = mysql.connection.cursor()
    query ="select word_eng from words where word_eng LIKE '{}%' order by word_eng".format(searchbox)
    cursor.execute(query)
    result = cursor.fetchall()

    return jsonify(result)

@app.route('/jobs')
def jobs():
    global jobs
    q = request.args.get('q')


    if q:
        jobs = jobs.query.filter(jobs.title.contains(q) |
        jobs.body.contains(q))

    
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


@app.route('/administrative')
def administrative():
    return render_template('administrative.html')







if __name__ =='__main__':
    app.run(debug=True)