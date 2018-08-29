import unittest

import json

from app.api.V1.views import myapp




class Test_questions(unittest.TestCase):   
    user_endpoint = '/api/v1/questions'
    myapp = myapp.test_client()

    def test_create_user(self):
        response = self.myapp.post(self.user_endpoint)
        self.assertEqual(response.status_code, 200)
        
    def test_list_all_questions(self):
        response = self.myapp.get(self.user_endpoint)
        self.assertEquals(response.status_code, 200)
    
        response = self.myapp.post(self.user_endpoint)
        self.assertEquals(response.status_code, 200)
    
    def test_get_question(self):
        response = self.myapp.get(self.user_endpoint+ '/1')
        self.assertEquals(response.status_code, 200)

        response = self.myapp.post(self.user_endpoint+ '/1')
        self.assertEquals(response.status_code, 200)
        
        response = self.myapp.delete(self.user_endpoint+ '/1')
        self.assertEquals(response.status_code, 200)
    

if __name__ == '__main__':
    unittest.main()