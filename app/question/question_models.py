question_list = []

class Question(object):
    def get_questions(self):
        """
        returns the whole list of questions
        """
        if len(question_list) == 0:
            return "No questions to show"
        return question_list

    def get_question_by_id(self, question_id):
        """
        iterate through the list of questions. if any item matches the id provided, add to the new list.
        if the length of the new list is zero then no question with the id
        """
        question =  [item for item in question_list if item["question_id"] == question_id]
        if len(question) == 0:
            return "No question with id {}".format(str(question_id))
        return question


    def create_question(self, the_question):
        """
        generate an id from the length of the question list and add the new question to the list
        """
        self.the_question = the_question
        
        id = len(question_list) + 1
        """Check validity of the question characters eg commas, empty string, too short or asked recently""" 
        data = " ".join(char for char in the_question if char.isalnum())
        if len(data) == 0:
            return "invalid user input"

        elif len(data) <= 5:
            return "user input too short"
        
        elif len(data) > 500:
            return "user input too long"

        elif data == self.get_question_by_id(id-1):
            return "Similar Question has been asked a moment ago"
        
        else:
            new_question = {
            "question_id" : id,
            "question" : the_question,        
            }
        
            question_list.append(new_question)

            return self.get_question_by_id(id), "successful post"


    def del_question(self, question_id):
        """
        check that a question with the id is available, if not, return string. if available then 
        delete it
        """    
        for item in question_list:
            if item["question_id"] == question_id: 
                question_list.remove(item)
            return "Question Deleted successfully"

    def edit_question(self, question_id, new_question):
        question_to_edit = self.get_question_by_id(question_id)
        if question_to_edit == "No question with id {}".format(str(question_id)):
            return question_to_edit
        else:
            question_to_edit[0]["question"] = new_question
            return "Edit to the question successful"


