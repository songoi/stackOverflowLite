from flask import Blueprint

answer = Blueprint("answer", __name__)

@answer.route('/answer')
def home():
    return "<h1>This works<h1>"