from flask import make_response, request, jsonify

from app.user.user_model import User

from app.question.models import Question

from flask_api import FlaskAPI

myapp = FlaskAPI(__name__)

@myapp.route('/')
def home():
    return jsonify({"message" : "Welcome to StackOverflow Lite API"})

@myapp.route('/api/v1/users', methods = ["POST"])
def create_user():
     user_maker = User() 
     user_maker.register_user("kim", "kim@example.com", "birthday", "userpassword")

     users = user_maker.get_users()
     return make_response(jsonify( { "users" : users } ))

@myapp.route('/api/v1/questions', methods = ["GET", "POST"])
def list_all_questions():
    questions_object = Question()

    if request.method == 'GET':
        all_questions= questions_object.get_questions()
        return make_response(jsonify( { "questions": all_questions} ))

    if request.method == 'POST':
        new_question = request.data.get("your_question")
        questions_object.create_question(new_question)
        return make_response(jsonify({"questions": questions_object.get_questions()}))

@myapp.route('/api/v1/questions/<int:question_id>', methods = ['GET', 'POST', 'DELETE'])
def get_question(question_id):
    questions_object = Question()

    if request.method == 'GET':
        querried_question = questions_object.get_question_byID(question_id)
        return make_response(jsonify( { "question": querried_question} ))
    
    if request.method == 'POST':
        new_answer = request.data.get("your_answer")
        return make_response(jsonify( { "question":  questions_object.answer(new_answer,question_id)} ))
    
    if request.method == 'DELETE':  
        return make_response(jsonify( { "questions": questions_object.del_question("question_id")} ))