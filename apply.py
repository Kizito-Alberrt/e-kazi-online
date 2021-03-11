from logging import debug
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def apply():
    return render_template('apply.html')



if __name__ =='__main__':
    app.run(debug=True)

if __name__ == '__main__':
    submit_form()