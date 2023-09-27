from cs50 import SQL
from flask import Flask,render_template,request

app = Flask(__name__)
db = SQL("sqlite:///todolist.db")



@app.route("/")
def index():
    name = request.args.get("name","Harsh")
    return render_template("index.html",name=name)
@app.route("/todopre", methods=['POST',"GET"])
def todopre():
    if request.method == 'POST':
        instance = request.form.get('instance')
        db.execute("INERT INTO items(list) VALUES(?)", instance)
        return redirect("/todo2")
    return render_template("todo2.html",todoo=TODOO)

    

    