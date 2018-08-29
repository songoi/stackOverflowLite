[![Build Status](https://travis-ci.org/songoi/stackOverflowLite.svg?branch=dev-api)](https://travis-ci.org/songoi/stackOverflowLite) [![Coverage Status](https://coveralls.io/repos/github/songoi/stackOverflowLite/badge.svg?branch=dev-api)](https://coveralls.io/github/songoi/stackOverflowLite?branch=api-v1)    [![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)  

<<<<<<< HEAD
<<<<<<< HEAD
**Stack Overflow API**  
A platform where you can ask questions, get answers to a specific question.
User interface is built with HTML and CSS.

**EndPoint**  
my endpoints

questions:
GET	api/v1/questions
	- get all questions

POST	api/v1/questions
	- post your question. Provide your_question


GET	api/v1/questions/<int:question_id>
	- get a specific question by question_id


DELETE	api/v1/questions/<int:question_id>
	- delete a specific question by giving its ID


answers:
POST	api/v1/questions/<int:question_id>/answer
	- post an answer by specifying the question_id and your_answer


=======
#StackOverflow-lite  
=======
# StackOverflow-lite  
>>>>>>> Add guide on how to set upAPI
A platform where people can ask questions and provide answers

#API
challenge two sets up API endpoints that save data in a data structure. the endpoints can do the following:
 - get all questions
 - get a question
 - post a question
 - post an answer to a question

**How to Set up:**
- In a virtual environment, install requirements.txt file
- run server using python run.py runserver
- use postman to test the endpoints by using the following endpoints

 #Endpoint | Functionality
 -----------|------------|
 GET /api/v1/questions | fetch all questions
 POST /api/v1/questions | post a new question
 GET /api/v1/questions/<int:question_id> | fetch a specific question
 DELETE /api/v1/questions/<int:question_id> | delete a specific question
 POST /api/v1/questions/<int:question_id>/answer | post an answer to question
<<<<<<< HEAD
>>>>>>> Add continuous intergration and heroku build
=======

 while posting a question: on postman, use raw JSON (application/json) with the key: "question"
 while posting an answer: on postman, use raw JSON (application/json) with the keys: "answer" and "question_id"
>>>>>>> Add guide on how to set upAPI
