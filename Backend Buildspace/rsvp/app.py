import re
from flask import Flask,render_template,request
from cs50 import SQL
app = Flask(__name__)
db = SQL("sqlite:///rsvp.db")
@app.route("/")
def index():
    return render_template("index.html")
REGISTRANTS = {}
DATA={}
@app.route("/rsvp",methods=["GET", "POST"])
def rsvp():

    if request.method == "POST":
        STATUS = request.form.get('status')
        USERNAME = request.form.get('username')
        db.execute("INSERT INTO rsvp (name,coming) VALUES(?,?)",USERNAME,STATUS)
        REGISTRANTS = db.execute("SELECT name , coming FROM rsvp")
        i = 0
        for _ in REGISTRANTS:
            name_match = re.search(r"'name': '([^']+)'", str(_))
            coming_match = re.search(r"'coming': '([^']+)'", str(_))
            name = name_match.group(1)
            coming = coming_match.group(1)
            DATA[name]=coming

        return render_template("rsvp.html",reg=DATA)  
    else:
        REGISTRANTS = db.execute("SELECT name , coming FROM rsvp")
        i = 0
        for _ in REGISTRANTS:
            name_match = re.search(r"'name': '([^']+)'", str(_))
            coming_match = re.search(r"'coming': '([^']+)'", str(_))
            name = name_match.group(1)
            coming = coming_match.group(1)
            DATA[name]=coming
        return render_template("rsvp.html",reg=DATA)