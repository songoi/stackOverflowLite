from app.question.question_models import Question

answer_list = []

class Answer(Question):
    def post_answer(self, answer, question_id):
        """
        accepts an answer and question id. answer is appended to the answer-list after an 
        answer id is generated from the the length of the answer-list.
        the method then returns all the answers to that question after adding the answer
        """
        self.your_answer = answer
        self.question_id = question_id
        
        current_question = self.get_question_by_id(question_id)
        answer_id = len(answer_list) + 1
        new_answer = {
            "question_id":question_id,
            "answer_id": answer_id,
            "answer": answer
        }
        answer_list.append(new_answer)
        
        return self.get_answers_to_question(question_id)

    def get_answers_to_question(self, question_id):
        all_answers = [item for item in answer_list if item["question_id"] == question_id]
        
        if len(all_answers) == 0:
            return "No answers for the question with id {}".format(str(question_id))
        return all_answers

    def delete_answer(self, answer_id, question_id):
        """
        check if the question exits and if it does, get to the answer by its id and delete it
        if it does not, return a message 
        """
        valid = self.get_answers_to_question(question_id)
        if isinstance(valid, list) == True:
            for item in answer_list:
                if item["answer_id"] == answer_id: 
                    answer_list.remove(item)
                return self.get_answers_to_question(question_id)
        return "No question with id {}".format(str(question_id))

