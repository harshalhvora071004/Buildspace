
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name","Harsh")
    return render_template("index.html",name=name)

@app.route("/blognew")
def blog():
    return render_template("blog1.html",Title=Title,Author=Author,Text=Text)

@app.route("/blog")
def blog1():
    return render_template("blog11.html",Title=Title,Author=Author,Text=Text)

@app.route("/todo1")
def todo1():
    return render_template("todo1.html")

@app.route('/counter', methods=['GET', 'POST'])
def counter():
    if request.method == 'POST':
        text = request.form['text']
        word_count = len(text.split())
        return render_template('counter.html', word_count=word_count, text=text)
    return render_template('counter.html', word_count=None, text=None)

@app.route("/Search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        phrase = request.form.get('searchphrase')
        phrases = ['Flask','Python','Html']
        if phrase in phrases:
            phrase = phrase + ' Is a Programming Language useful for doing Backend Tasks in Builspace Link'
            return render_template('Search.html', searchphrase=phrase,SEARCH = 1,placeholder = phrase)
        else:
            return render_template('Search.html', searchphrase=f'{phrase} is not a Keyword ',SEARCH = 1,placeholder = phrase)
    else:
        return render_template("Search.html",searchphrase = None,SEARCH = None)
    
    
Title = "Harshal's Food Blog"
Author = "~ Harshal Vora"
Text = "What is Lorem Ipsum?  Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
@app.route("/Harshal")
def Harshal():
    return render_template("Harshal.html",Title=Title,Author=Author,Text=Text)
@app.route("/Home")
def Home():
    return render_template("Home.html",Title=Title,Author="Home",Text=Text)
@app.route("/Articles")
def Articles():
    return render_template("Articles.html",Title=Title,Author="Articles",Text=Text)
@app.route("/About")
def About():
    return render_template("About.html",Title=Title,Author="About",Text=Text)
@app.route("/Contact")
def Contact():
    return render_template("Contact.html",Title=Title,Author="Contact",Text=Text)



TODOO = {}
count = 0
@app.route("/todo")
def todo():
    return render_template("todo.html")

@app.route("/todopre", methods=['POST',"GET"])
def todopre():
    if request.method == 'POST':
        instance = request.form.get('instance')
        count =+ 1
        TODOO[instance]=count
        return render_template("todo2.html",todoo=TODOO)
    return render_template("todo2.html",todoo=TODOO)

    