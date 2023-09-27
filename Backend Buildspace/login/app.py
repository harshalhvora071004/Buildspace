from cs50 import SQL
import sqlite3
from flask import Flask,render_template,request

app = Flask(__name__)
db = SQL("sqlite:///login.db")
@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u_name = request.form.get("username")
        p_word = request.form.get("password")    
        if db.execute(f"SELECT 1 FROM login WHERE username = ? ",u_name):
            if db.execute(f"SELECT * FROM login WHERE username = ? AND password = ?",u_name,p_word):
                return render_template("welcome.html",Username=u_name)    
            return render_template("error.html",ERROR = p_word,ERRORNAME = 'PASSWORD')
        else:
            return render_template("error.html",ERROR = u_name,ERRORNAME="USERNAME")
    if  request.method == "GET":
        return render_template("login.html",username=None,password=None)
@app.route("/signup",methods=["POST","GET"])
def signup():
    if request.method == "POST":
        u_name = request.form.get("username")
        p_word = request.form.get("password")    
        if db.execute(f"SELECT 1 FROM login WHERE username = ?",u_name):
            return render_template("error.html")
        else:
            db.execute("INSERT INTO login (username, password) VALUES(?,?)", u_name, p_word)
            return render_template("welcome.html",Username=u_name)
    return render_template("signup.html",username=None,password=None)
