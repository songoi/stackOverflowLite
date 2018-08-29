question_list = []

class Question(object):
    def get_questions(self):
        return question_list

    def get_question_by_id(self, question_id):
        question =  [item for item in question_list if item["post_id"] == question_id]
        if len(question) == 0:
            return "No question with id {}".format(str(question_id))
        return question


    def create_question(self, the_question):
        self.the_question = the_question

        id = len(question_list) + 1
        new_question = {
            "post_id" : id,
            "question" : the_question,        
        }
        
        question_list.append(new_question)

        return self.get_question_by_id(id)

    def del_question(self, question_id):      
        if question_id >len(question_list) or question_id <= 0:
            return "No question with id {}".format(str(question_id))
                
        else: 
            for item in question_list:
                if item["post_id"] == question_id: 
                    question_list.remove(item)
                return question_list
        

    
