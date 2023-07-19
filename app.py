from flask import Flask, render_template, request, flash 
from sql_queries import *
from config import *
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)