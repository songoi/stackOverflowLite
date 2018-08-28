from flask import make_response, request, jsonify, redirect, url_for

from functools import wraps

from app.user.user_model import User

<<<<<<< HEAD
from app.question.question_models import Question, Check_user_input
=======
from app.question.question_models import Question
>>>>>>> feedback implementation

from flask_api import FlaskAPI

myapp = FlaskAPI(__name__)


<<<<<<< HEAD

questions_object = Question()

validity = Check_user_input()



=======
@myapp.route('/api/v1/questions', methods = ["GET", "POST"])
def list_questions(the_question = None):
    questions_object = Question()
>>>>>>> feedback implementation

<<<<<<< HEAD
@myapp.route('/')
def home():
    return jsonify({"message" : "Welcome to StackOverflow Lite API"})

@myapp.route('/api/v1/questions', methods = ["GET", "POST"])
def list_question():
    
    if request.method == "GET":
        all_questions = questions_object.get_questions()
=======
    if request.method == 'GET':
        all_questions = questions_object.get_questions()
       
>>>>>>> Endpoints and their tests
        return make_response(jsonify( { "questions": all_questions} ))

<<<<<<< HEAD
    if request.method == "POST":   
        req_data = request.get_json()     
        new_question = req_data["question"]

        response = questions_object.create_question(new_question)
        
        return make_response(jsonify({"question": response}))

=======
    if request.method == 'POST':
        req_data = request.get_json()
           
        new_question = req_data.get('question')
        
        questions_object.create_question(new_question)
    
        return make_response(jsonify({"questions": questions_object.get_questions()}))
>>>>>>> feedback implementation

<<<<<<< HEAD
@myapp.route('/api/v1/questions/<int:question_id>', methods = ["GET", "DELETE"])
def get_question(question_id):
=======
@myapp.route('/api/v1/questions/<int:question_id>', methods = ['GET', 'POST', 'DELETE'])
def get_question(question_id = None):
    questions_object = Question()
>>>>>>> Endpoints and their tests

<<<<<<< HEAD
    if request.method == "GET":
        response = questions_object.get_question_by_id(question_id)
        return make_response(jsonify( { "question": response} ))
       
    if request.method == "DELETE": 
        remaining_questions = questions_object.del_question(question_id)
        return make_response(jsonify( { "questions": remaining_questions } ))

@myapp.route('/api/v1/questions/<int:question_id>/answer', methods = ["POST", "GET"])
def get_answers(question_id):
    
    if request.method == "POST":        
        req_data = request.get_json()
        answer = req_data.get("answer")

        return make_response(jsonify( { "answer": answer} ))

    if request.method == "GET":
        answers = get_answers_to_question(question_id)
        return make_response(jsonify( { "answer":  answers} ))

@myapp.route('/api/v1/user/new_user', methods = ["POST"])
def create_user(user_name, user_mail, user_birthday, userpassword):
    req_data = request.get_json()
    name = req_data["user_name"]
    mail = req_data["user_mail"]
    birthday = req_data["birthday"]
    password = req_data["userpassword"]
    
    make_user = User() 
    
    make_user.register_user(name, mail, birthday, password)

    return make_response(jsonify( { "message" : "successfully registered as user" } ))

@myapp.route("/api/v1/login", methods = ["POST"])
def authorize(usermail, userpassword):
    req_data = request.get_json()
    login_mail = req_data["usermail"]
    login_password = req_data["userpassword"]

    logged_in = User.login(login_mail, login_password)

    if logged_in == True:
        return make_response(jsonify( { "message" : "log in successful" } ))
    
    return make_response(jsonify( { "message" : "wrong user credentials" } ))
=======
    if request.method == 'GET':
        querried_question = questions_object.get_question_by_id(question_id)
        return make_response(jsonify( { "question": querried_question} ))
    
    if request.method == 'DELETE':      
        return make_response(jsonify( { "questions": questions_object.del_question(question_id)} ))



@myapp.route('/api/v1/questions/<int:question_id>/answer', methods = ['POST'])
def post_answer(question_id = None, answer):
    answer_object = Answer()
    req_data = get_json()
    new_answer = request.data.get("your_answer")
<<<<<<< HEAD
    return make_response(jsonify( { "question":  questions_object.answer(new_answer,question_id)} ))
    
>>>>>>> feedback implementation
=======
    return make_response(jsonify( { "question":  answer_object.post_answer(new_answer,question_id)} ))
    
>>>>>>> Endpoints and their tests
