from flask import make_response, request, url_for, jsonify

from app.user.user_model import User

from app.question.question_models import Question

from flask_api import FlaskAPI

myapp = FlaskAPI(__name__)


@myapp.route('/api/v1/questions', methods = ["GET", "POST"])
def list_all_questions():
    questions_object = Question()

    if request.method == 'GET':
        all_questions= questions_object.get_questions()
        return make_response(jsonify( { "questions": all_questions} ))

    if request.method == 'POST':
        req_data = request.get_json()
        new_question = req_data['your_question']

        questions_object.create_question(new_question)
    
        return make_response(jsonify({"questions": questions_object.get_questions()}))

@myapp.route('/api/v1/questions/<int:question_id>', methods = ['GET', 'POST', 'DELETE'])
def get_question(question_id):
    questions_object = Question()

    if request.method == 'GET':
        querried_question = questions_object.get_question_by_id(question_id)
        return make_response(jsonify( { "question": querried_question} ))
    
    if request.method == 'DELETE':      
        return make_response(jsonify( { "questions": questions_object.del_question("question_id")} ))



@myapp.route('/api/v1/questions/<int:question_id>/answer', methods = ['POST'])
def post_answer(question_id):

    req_data = get_json()
    new_answer = request.data.get("your_answer")
    return make_response(jsonify( { "question":  questions_object.answer(new_answer,question_id)} ))
    