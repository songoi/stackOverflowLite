[![Build Status](https://travis-ci.org/songoi/stackOverflowLite.svg?branch=dev-api)](https://travis-ci.org/songoi/stackOverflowLite) [![Coverage Status](https://coveralls.io/repos/github/songoi/stackOverflowLite/badge.svg?branch=api-v1)](https://coveralls.io/github/songoi/stackOverflowLite?branch=api-v1)    [![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)  

**StackOverflow-lite**  
A platform where people can ask questions and provide answers

#API
challenge two sets up API endpoints that save data in a data structure. the endpoints can do the following:
 - get all questions
 - get a question
 - delete a question
 - post a question
 - edit a posted question
 - post an answer to a question
 - fetch all answers to a question
 - delete an answer

**How to Set up:**
- In a virtual environment, install requirements.txt file
- run server using python run.py runserver
- use postman to test the endpoints by using the following endpoints

 #Endpoint | Functionality| input
 -----------|------------|-------|
 GET /api/v1/questions | fetch all questions |
 POST /api/v1/questions | post a new question | "question"
 GET /api/v1/questions/<int:question_id> | fetch a specific question|
 PUT / /api/v1/questions/<int:question_id> | edit an existing question | "the_question", "question_id"
 DELETE /api/v1/questions/<int:question_id> | delete a specific question |
 POST /api/v1/questions/<int:question_id>/answer | post an answer to question | "answer" "question_id"
 GET /api/v1/questions/<int:question_id>/answer| get all answers to a question |
 DELET //api/v1/questions/<int:question_id>/answer | delete an answer | "answer_id"


 while using POST on postman, use raw JSON (application/json)"

 Access the API on [Heroku link] (https://stack-overflow-lite-api.herokuapp.com/)