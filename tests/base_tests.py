import unittest

import json

from app.api.V1.views import myapp

from app.answers.answer_models import answer_list

from app.question.question_models import question_list

class BaseTests(unittest.TestCase):
    def set_up(self):
        self.client = self.myapp.test_client()
        self.answer_list = answer_list
        self.questions = question_list
        self.new_question = "question example 2"
        self.new_answer = "answer example 2"
        self.req_data = {
            "user_name": "john doe"
            "user_mail": "john@doe.com"
            "birthday": "12.03.2022"
            "userpassword": "testpassword" 
        }     



if __name__ == '__main__':
    unittest.main()