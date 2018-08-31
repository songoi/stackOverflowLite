import unittest

import json

from app.api.V1.views import myapp




class BaseTest(unittest.TestCase):
    """
    Sets up needed prerequisites for testing the endpoints. 
    user_endpoint is modified at different endpoints. 
    """
    def setUp(self):   
        self.user_endpoint = '/api/v1/questions'
        self.myapp = myapp.test_client()
        self.new_question = "question example 1"
        self.new_answer = "answer example 1"
        self.edit_question = "this question has changed"
        self.question_id = 1
        self.invalid_question1 = "    "
        self.invalid_question2 = "., ./"
        self.invalid_question3 = "aq"
    
    def tearDown(self):
        pass

class TestQuestion(BaseTest):
    """
    Question class inherits from the base test where all the prerequisites are set.
    tests question endpoints by passing data through them and evaluating the response
    """
    def test_post_question(self):
        response = self.myapp.post(self.user_endpoint, 
                                   content_type='application/json',
                                   data=json.dumps(dict(question = self.new_question)))
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data.decode('utf-8'))
        self.assertIn("results", data)

    def test_invalid_question(self):
        response = self.myapp.post(self.user_endpoint, 
                                        content_type='application/json',
                                        data=json.dumps(dict(question = self.invalid_question1)))
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data.decode('utf-8'))
        message = data.get("results")
        self.assertIn("invalid user input", message)
 
    def test_no_question(self):
        response = self.myapp.post(self.user_endpoint, 
                                        content_type='application/json',
                                        data=json.dumps(dict(question = self.invalid_question2)))
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data.decode('utf-8'))
        message = data.get("results")
        self.assertIn("invalid user input", message)

    def test_short_question(self):
        response = self.myapp.post(self.user_endpoint, 
                                        content_type='application/json',
                                        data=json.dumps(dict(question = self.invalid_question3)))
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data.decode('utf-8'))
        message = data.get("results")
        self.assertIn("user input too short", message)

    def test_list_questions(self):

        response = self.myapp.get(self.user_endpoint)
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertIn("results", data)
     

    def test_get_question(self):
        response = self.myapp.get(self.user_endpoint+ '/1')
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        test_data = data.get("question")
        self.assertNotEqual(test_data, None)

    def test_edit_question(self):
        response = self.myapp.put(self.user_endpoint+ '/1', 
                                   content_type='application/json',
                                   data=json.dumps(dict(question = self.edit_question,
                                   question_id = self.question_id)))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertIn("message", data)

    def test_delete_question(self):
        response = self.myapp.delete(self.user_endpoint+ '/1')
        self.assertEquals(response.status_code, 202)
        data = json.loads(response.data.decode('utf-8'))
        test_data = data.get("question")
        self.assertNotEqual(self.new_question, test_data)

class Test_answer(BaseTest):
    def test_post_answer(self):
        response = self.myapp.post(self.user_endpoint+ '/1/answer',
                                   content_type='application/json',
                                   data=json.dumps(dict(answer = self.new_answer)))

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        test_data = data.get("results")
        self.assertIsNotNone(test_data)

    def test_get_answers(self):
        response = self.myapp.get(self.user_endpoint+ '/1/answer',
                                   content_type='application/json',
                                   data=json.dumps(dict(answer = self.new_answer)))

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        test_data = data.get("results")
        self.assertIsNotNone(test_data)

    def test_delete_answers(self):
        response = self.myapp.get(self.user_endpoint+ '/1/answer',
                                   content_type='application/json',
                                   data=json.dumps(dict(answer_id = 1)))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        test_data = data.get("results")
        self.assertIsNotNone(test_data)

    def test_invalid_question_id(self):
        """tests if a wrong question_id is set while answering a quesiton"""
        response = self.myapp.post(self.user_endpoint+ '/2/answer',
                                   content_type='application/json',
                                   data=json.dumps(dict(answer = self.new_answer)))

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        test_data = data.get("results")
        self.assertEqual("No question with id 2", test_data)
