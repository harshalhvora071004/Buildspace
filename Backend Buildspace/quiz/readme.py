#Buildspace tasks started on 17th Sept 2023
from flask import Flask,render_template,request
from cs50 import SQL
import sqlite3
import random
db = SQL("sqlite:///quiz.db")
app = Flask(__name__)

question_id_list = []
questions = {}
answers = {}
ANSWER={}
CANSWER={}
cou = [1,2,3,4,5]

@app.route('/',methods=['GET'])
def index():    
    if request.method == 'GET':
        max_question_id = db.execute("SELECT MAX(id) as max_id FROM questions")[0]['max_id']
        if max_question_id is not None:
            i = 1
            while len(question_id_list) < 5:
                random_id = random.randint(1, max_question_id)
                if random_id not in question_id_list:
                    question_id_list.append(random_id)
            for q_id in question_id_list: 
                qdata = db.execute("SELECT question FROM questions WHERE id = ?", q_id)           
                questions[q_id] = qdata[0]['question']
                answers[1] = db.execute("SELECT option_1 FROM questions WHERE id = ?", q_id)[0]['option_1']
                answers[2] = db.execute("SELECT option_2 FROM questions WHERE id = ?", q_id)[0]['option_2']
                answers[3] = db.execute("SELECT option_3 FROM questions WHERE id = ?", q_id)[0]['option_3']
                answers[4] = db.execute("SELECT option_4 FROM questions WHERE id = ?", q_id)[0]['option_4']
                CANSWER[q_id] = db.execute("SELECT option_5 FROM questions WHERE id = ?", q_id)[0]['correct_answer']
                ANSWER[q_id] = list(answers.values())
        return render_template("index.html", rndm=questions, ans=ANSWER,coounter=cou)
@app.route("/store",methods=["POST"])
def store():
    for q_id in question_id_list:
        if CANSWER[q_id] == request.form.get("answer"+q_id):
            Score = Score + 1
    u_name = request.form.get("username")
    db.execute("INSERT INTO result (username, score,question_id_list) VALUES(?,?,?)",u_name,Score,question_id_list)
    return render_template("result.html",u_name=u_name, score=Score)
        
@app.route("/questions", methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        opt1 = request.form.get('answer1_text')
        opt2 = request.form.get('answer2_text')
        opt3 = request.form.get('answer3_text')
        opt4 = request.form.get('answer4_text')
        opt5 = request.form.get('correct_answer')
        question = request.form.get('question')
        u_name = request.form.get('username')
        for i in [opt1,opt2,opt3]:
            if i == opt4 :
                return render_template('error_rept.html')
                break
        for i in [opt1,opt2]:
            if i == opt3 :
                return render_template('error_rept.html')
                break
        if opt1 == opt2 :
                return render_template('error_rept.html')

        db.execute("INSERT INTO questions (question,option_1,option_2,option_3,option_4,correct_option,name) VALUES(?,?,?,?,?,?,?)",question,opt1,opt2,opt3,opt4,opt5,u_name)
        return render_template("questions.html")
    return render_template("questions.html")



# {% extends "Layout.html" %}
# {% block body %}
# <div style="left: 10vw; right: 10vw; top: 10vh; bottom: 10vh; position: absolute; font-size: 2vw;">
#     <div style="background-color:deepskyblue; border-style: solid; border-width: 1px; padding: 2vw;">
#         <form action="/store" method="post">
#             <h1 style="text-align: center;background-color:lightskyblue;">Builspace Quiz</h1>
#             <label for="username" style="display: block; white-space: nowrap;background-color: lightskyblue;">Username:</label>
#             <input type="text" id="username" name="username" style="width: 100%;"><br><br>

#             {% for question_id, question_text in rndm.items() %}
#                 <div style="background-color: aliceblue;">
#                     <label style="display: block; white-space: nowrap;background-color: lightskyblue;">
#                         Question {{ question_id }}: {{ question_text }}
#                     </label>
                    
#                     {% for answer_id in range(1, 5) %}
#                         {% set answer_text = ans[question_id][answer_id - 1] %}
#                         <label style="display: block; white-space: nowrap;">
#                             <input type="radio" name="answer{{ question_id }}" value="{{ answer_id }}" style="display: inline;"> {{ answer_text }}
#                         </label>
#                     {% endfor %}
#                 </div>
#                 <br><br>
#             {% endfor %}
            
#             <input type="submit" value="Submit">
#         </form>
#     </div>
# </div>
# {% endblock %} 
