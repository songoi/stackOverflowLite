import unittest

import json

from app.api.V1.views import myapp


class Test_questions(unittest.TestCase):
    def test_create_user(self):
        response = self.myapp.post(self.user_endpoint)
        self.assertEqual(response.status_code, 200)
        


        
if __name__ == '__main__':
    unittest.main()