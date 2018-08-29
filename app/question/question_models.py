question_list = []

class Question(object):
    def get_questions(self):
        """
        returns the whole list of questions
        """
        return question_list

    def get_question_by_id(self, question_id):
        """
        iterate through the list of questions. if any item matches the id provided, add to the new list.
        if the length of the new list is zero then no question with the id
        """
        question =  [item for item in question_list if item["post_id"] == question_id]
        if len(question) == 0:
            return "No question with id {}".format(str(question_id))
        return question


    def create_question(self, the_question):
        """
        generate an id from the length of the question list and add the new question to the list
        """
        self.the_question = the_question

        id = len(question_list) + 1
        new_question = {
            "post_id" : id,
            "question" : the_question,        
        }
        
        question_list.append(new_question)

        return self.get_question_by_id(id)

    def del_question(self, question_id):
        """
        check that a question with the id is available, if not, return string. if available then 
        delete it
        """
        response = self.get_question_by_id(question_id)      
        if isinstance(response, str):
            return "No question with id {}".format(str(question_id))
        else: 
            for item in question_list:
                if item["post_id"] == question_id: 
                    question_list.remove(item)
                return question_list
        

    
