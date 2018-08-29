from flask import make_response, request, url_for, jsonify

from app.user.user_model import User

from app.question.question_models import Question

from app.answers.answer_model import Answer

from flask_api import FlaskAPI

myapp = FlaskAPI(__name__)

"""
sets up the different routes by passing the method used on the route
and manipulates the data using models imported from the questions and 
answer model
"""
@myapp.route('/')
def home():
    return jsonify({"message" : "Welcome to StackOverflow Lite API"})

@myapp.route('/api/v1/questions', methods = ["GET", "POST"])
def list_questions(the_question = None):
    """
    an instance of the Questions class is set then used to pass the different
    methods defined in the class
    """
    questions_object = Question()

    if request.method == 'GET':
        all_questions = questions_object.get_questions()
       
        return make_response(jsonify( { "questions": all_questions} ))

    if request.method == 'POST':
        """
        retrieves data from the endpoint in json format, which is then used in the 
        response
        """
        req_data = request.get_json()
           
        new_question = req_data.get('question')
        
        questions_object.create_question(new_question)
    
        return make_response(jsonify({"questions": questions_object.get_questions()}))

@myapp.route('/api/v1/questions/<int:question_id>', methods = ['GET', 'POST', 'DELETE'])
def get_question(question_id = None):
    questions_object = Question()

    if request.method == 'GET':
        querried_question = questions_object.get_question_by_id(question_id)
        return make_response(jsonify( { "question": querried_question} ))
    
    if request.method == 'DELETE':      
        return make_response(jsonify( { "questions": questions_object.del_question(question_id)} ))



@myapp.route('/api/v1/questions/<int:question_id>/answer', methods = ['POST'])
def post_answer(answer = None, question_id = None):
    """
    makes an instance of the Answer class which is then used to pass into the endpoint
    the different methods defined in the class
    """
    answer_object = Answer()
    req_data = request.get_json()
    new_answer = req_data.get("answer")
    print (new_answer)
    return make_response(jsonify( { "answer":  answer_object.post_answer(new_answer,question_id)}))