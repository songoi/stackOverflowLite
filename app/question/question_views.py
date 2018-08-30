from flask import Blueprint

question = Blueprint("question", __name__)


@question.route('/')
def home():
    return "<h1>This works<h1>"

