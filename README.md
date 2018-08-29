[![Build Status](https://travis-ci.org/songoi/stackOverflowLite.svg?branch=api-v1)](https://travis-ci.org/songoi/stackOverflowLite) [![Coverage Status](https://coveralls.io/repos/github/songoi/stackOverflowLite/badge.svg?branch=api-v1)](https://coveralls.io/github/songoi/stackOverflowLite?branch=api-v1)    [![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)    [![Test Coverage](https://api.codeclimate.com/v1/badges/d1f032c3c8a41327871c/test_coverage)](https://codeclimate.com/github/songoi/stackOverflowLite/test_coverage)

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
A platform where people can ask questions and provide answers

#API
challenge two sets up API endpoints that save data in a data structure. the endpoints can do the following:
 - get all questions
 - get a question
 - post a question
 - post an answer to a question

 #Endpoint | Functionality
 GET /api/v1/questions | fetch all questions
 POST /api/v1/questions | post a new question
 GET /api/v1/questions/<int:question_id> | fetch a specific question
 DELETE /api/v1/questions/<int:question_id> | delete a specific question
 POST /api/v1/questions/<int:question_id>/answer | post an answer to question
>>>>>>> Add continuous intergration and heroku build
