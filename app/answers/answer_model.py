class Answer(object):
def answer(self, your_answer, question_id):
        current_question = self.get_question_byID(question_id)
        current_answers = current_question["answer"]
        answer_id = len(current_answers) + 1
        new_answer = {
            "answer_id": answer_id,
            "answer": your_answer
        }
        current_answers.append(new_answer)
        
        return current_question
        
