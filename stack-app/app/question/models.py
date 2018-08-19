class Question(object):
    def __init__(self, post):
        self.post = post
        self.question_list = []

    def get_questions(self):
        return self.question_list

    def create_question(self, post):
        id = len(self.question_list) + 1
        new_question = {
            "post_id" : id,
            "question" : post           
        }
        return self.question_list.append(new_question)

    def del_question(self, post, post_id = None):
        for item in self.question_list:
            if post or post_id in item:
                self.question_list.remove(item)