from flask import Blueprint

user = Blueprint("user",__name__)

@user.route('/')
def home():
    return "<h1>This works<h1>"