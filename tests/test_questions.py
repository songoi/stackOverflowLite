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
            "user_name": "john doe",
            "user_mail": "john@doe.com",
            "birthday": "12.03.2022",
            "userpassword": "testpassword" 
        }     



class Test_questions(BaseTests):   
    user_endpoint = '/api/v1/questions'
    
    def test_get_questions(self):
        response = BaseTests.client.get(self.user_endpoint)
        self.assertEquals(response.status_code, 200)

        self.assertIn("whats the distance between the sun and the moon", str(response.data)) 

    def test_post_question(self):
        response = BaseTests.client.post(self.user_endpoint)
        self.assertEquals(response.status_code, 200)


    def test_list_all_questions(self):
        response = self.myapp.get(self.user_endpoint)
        self.assertEquals(response.status_code, 200)
    
        response = self.myapp.post(self.user_endpoint)
        self.assertEquals(response.status_code, 200)
    
        response = self.myapp.post(self.user_endpoint+ '/1')
        self.assertEquals(response.status_code, 200)
        
        response = self.myapp.delete(self.user_endpoint+ '/1')
        self.assertEquals(response.status_code, 200)
    

if __name__ == '__main__':
    unittest.main()