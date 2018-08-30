from flask import Flask 

myapp = Flask(__name__)

from app.user.user_views import user

from app.answer.answer_views import answer

from app.question.question_views import question

myapp.register_blueprint(user, url_prefix='/auth')

myapp.register_blueprint(answer, url_prefix='/questions')

myapp.register_blueprint(question, url_prefix='/questions')
