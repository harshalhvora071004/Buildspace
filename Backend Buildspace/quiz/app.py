from flask import Flask,render_template,request
from cs50 import SQL
import sqlite3
import random
db = SQL("sqlite:///quiz.db")
app = Flask(__name__)

question_id_list = []

answers = {}
ANSWER={}
CANSWER={}
cou = [1,2,3,4,5]

@app.route('/',methods=['GET'])
def index():    
    questions = {}
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
                CANSWER[q_id] = db.execute("SELECT correct_option FROM questions WHERE id = ?", q_id)[0]['correct_option']
                ANSWER[q_id] = list(answers.values())
        return render_template("index.html", rndm=questions, ans=ANSWER,coounter=cou)
answer_value = {}
answer_current_value = {}
@app.route("/store", methods=["POST"])
def store():
    Score = 0
    u_name = request.form.get("username")

    for q_id in question_id_list:
        # Get the selected answer from the form
        selected_answer = int(request.form.get(f"answer{q_id}"))

        # Compare the selected answer with the correct answer
        if selected_answer == int(CANSWER[q_id]):
            Score += 1

    question_id_list_str = ','.join(map(str, question_id_list))
    db.execute("INSERT INTO result (username, score, question_id_list) VALUES (?, ?, ?)", u_name, Score, question_id_list_str)

    return render_template("result.html", username=u_name, score=Score)

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

