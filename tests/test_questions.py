import unittest

import json

from app.api.V1.views import myapp




<<<<<<< HEAD:tests/test_questions.py
class Test_questions(unittest.TestCase):   
=======
class BaseTest(unittest.TestCase):   
>>>>>>> Endpoints and their tests:tests/test_app.py
    user_endpoint = '/api/v1/questions'
    myapp = myapp.test_client()
    new_question = "question example 1"
    new_answer = "answer example 1"

class TestQuetion(BaseTest):
    
    def test_post_question(self):
        response = myapp.post(user_endpoint, content_type='application/json', 
            data=json.dumps(dict(question = new_question))
        self.assertEqual(response.status_code, 200)
        self.assertIn(respose, "question example 1" )
 
        
    def test_list_all_questions(self):
        response = myapp.get(self.user_endpoint)
        self.assertEquals(response.status_code, 200)
        assertIn(response)
    

    def test_get_question(self):
        response = self.myapp.get(self.user_endpoint+ '/1')
        self.assertEquals(response.status_code, 200)

        response = self.myapp.post(self.user_endpoint+ '/1')
        self.assertEquals(response.status_code, 200)
        
        response = self.myapp.delete(self.user_endpoint+ '/1')
        self.assertEquals(response.status_code, 200)
    
    
    def test_create_user(self):
        response = self.myapp.post(self.user_endpoint)
        self.assertEqual(response.status_code, 200)
        
    
if __name__ == '__main__':
    unittest.main()