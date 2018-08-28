import unittest

import json

from app.api.V1.views import myapp




class BaseTest(unittest.TestCase):
    def setUp(self):   
        self.user_endpoint = '/api/v1/questions'
        self.myapp = myapp.test_client()
        self.new_question = "question example 1"
        self.new_answer = "answer example 1"
    
    def tearDown(self):
        pass

class TestQuestion(BaseTest):
    
    def test_post_question(self):
        response = self.myapp.post(self.user_endpoint, 
                                   content_type='application/json',
                                   data=json.dumps(dict(question = self.new_question)))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertIn("questions", data)

    def test_list_questions(self):
        response = self.myapp.get(self.user_endpoint)
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertIn("questions", data)
     

    def test_get_question(self):
        response = self.myapp.get(self.user_endpoint+ '/1')
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        test_data = data.get("question")
        self.assertEqual(len(test_data), 1)

    def test_delete_question(self):
        response = self.myapp.delete(self.user_endpoint+ '/2')
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        test_data = data.get("question")
        self.assertNotEqual(self.new_question, test_data)
    
    # def test_post_answer(self):
    #     response = self.myapp.post(self.user_endpoint+ '/2/answer',
    #                                content_type='application/json',
    #                                data=json.dumps(dict(answer = self.new_answer)))

    #     self.assertEqual(response.status_code, 200)