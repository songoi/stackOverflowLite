from flask import make_response, request, jsonify

<<<<<<< Updated upstream
=======
from app.question import models

>>>>>>> Stashed changes
from flask_api import FlaskAPI

# from app.user import User

app = FlaskAPI(__name__)


@app.route('/api/v1/users', methods=["GET"])
def home():
    pass
# def list_users():
#      """
#        Instantiate the User Class
#      """
#      userMaker = User(""songoi", "songoi@example.com", "password", "birthday")
#      """
#       Register the user so that the users list inside the User model can have users
#      """   
#      userMaker.register_user("kim", "kim@example.com", "birthday")
#      """
#      Get the users now through the class method
#      """
#      users = userMaker.get_users()
#      return make_response(jsonify( { "users" : users } ))