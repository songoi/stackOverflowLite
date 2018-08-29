from flask import g, make_response, request, jsonify, redirect, url_for

from functools import wraps

from app.user.user_model import User

from app.question.models import Question

from flask_api import FlaskAPI

myapp = FlaskAPI(__name__)

# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if user is None:
#             return redirect(url_for("authorize"))
#         return f(**args, **kwargs)
#     return decorated_function



@myapp.route('/')
def home():
    return jsonify({"message" : "Welcome to StackOverflow Lite API"})

@myapp.route('/api/v1/user/new_user', methods = ["POST"])
def create_user(user_name, user_mail, user_birthday, userpassword):
    name = request.data.get("user_name")
    mail = request.data.get("user_mail")
    birthday = request.data.get("birthday")
    password = request.data.get("userpassword")
    
    make_user = User() 
    
    make_user.register_user("name", "mail", "birthday", "password")

    return make_response(jsonify( { "message" : "successfully registered as user" } ))

@myapp.route("/api/v1/login", methods = ["POST"])
def authorize(usermail, userpassword):
    login_mail = request.data.get("usermail")
    login_password = request.data.get("userpassword")

    logged_in = User.login(login_mail, login_password)

    if logged_in == True:
        return make_response(jsonify( { "message" : "log in successful" } ))
    else:
        return make_response(jsonify( { "message" : "wrong user credentials" } ))


# @myapp.route('/api/v1/questions', methods = ["GET", "POST"])
# # @login_required
# def list_question():
#     questions_object = Question()

#     if request.method == "GET":
#         all_questions = questions_object.get_questions()
#         return make_response(jsonify( { "questions": all_questions} ))

#     if request.method == "POST":
#         new_question = request.data.get("your_question")
#         questions_object.create_question(new_question)
#         return make_response(jsonify({"questions": questions_object.get_questions()}))

@myapp.route('/api/v1/questions/<int:question_id>', methods = ["GET", "POST", "DELETE"])
# @login_required
def get_question(question_id):
    questions_object = Question()

    if request.method == "GET":
        querried_question = questions_object.get_question_byID(question_id)
        return make_response(jsonify( { "question": querried_question} ))
       
    # if request.method == "DELETE": 
    #     remaining_questions = questions_object.del_question("question_id")
    #     return make_response(jsonify( { "questions": remaining_questions } ))

@myapp.route('/api/v1/questions/<int:question_id>/answer', methods = ["POST", "GET"])
# @login_required
def get_answers(question_id, your_answer):
    
    if request.method == "POST":
        new_answer = request.data.get("your_answer")

        return make_response(jsonify( { "question":  Answer.post_answer(new_answer, question)} ))

    if request.method == "GET":
        answers = get_answers_to_question(question)
        return make_response(jsonify( { "question":  answers} ))

