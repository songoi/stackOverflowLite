from app.question.question_m

answer_list = [
        {
        "question_id" : 1,
        "answer" : "205,524km"
        } 
]
class Answer(Question):
        
    def post_answer(self, your_answer):
        new_answer = {
            "question_id": question_id,
            "answer": your_answer
        }
        answer_list.append(new_answer)
        return get_answers_to_question(question_id)
    
    def get_answers_to_question(self, question_id):
        all_answers = []
        for item in answer_list:
            if item["question_id"] == question_id:
                all_answers.append(item)
        return all_answers 
             
