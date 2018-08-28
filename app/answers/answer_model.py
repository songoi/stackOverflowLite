from question.question_models import Question

answer_list = [
    {
        "question_id":1,
        "answer":"2,054,0042km"
    }
]

class Answer(Question):
    def post_answer(self, your_answer, question_id):
            current_question = get_question_by_id(question_id)
            answer_id = len(answer_list)
            new_answer = {
                "question_id":question_id
                "answer_id": answer_id
                "answer": your_answer
            }
            answer_list.append(new_answer)
            
            return current_question + new_answer
    
    def get_answers_to_question(self, question_id):
        all_answers = [item for item in answer_list if item["question_id"] == question_id]
        
        if len(answer) == 0:
            return "No answers for the question with id {}".format(str(question_id))
        return all_answers

    def delete_answer(self, answer_id, question_id):
        """
        check if the question exits and if it does, get to the answer by its id and delete it
        if it does not, 
        """
        valid = get_answers_to_question(question_id)
            if isinstance(valid, list) == True:
                for item in answer_list:
                    if item["answer_id"] == answer_id: 
                        answer_list.remove(item)
                    return get_answers_to_question(question_id)
            return "No question with id {}".format(str(question_id))

