from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name","Harsh")
    return render_template("index.html",name=name)
@app.route("/questions")
def index():
    name = request.args.get("name","Harsh")
    return render_template("index.html",name=name)
@app.route("/quiz")
def index():
    name = request.args.get("name","Harsh")
    return render_template("index.html",name=name)
