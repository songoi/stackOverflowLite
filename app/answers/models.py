from app.question.models import Question

answer_list:[
        {
        "question_id" : 1,
        "answer" : "205,524km"
        } 
]
class Answer(Question):
        
    def post_answer(self, your_answer, question_id):
            new_answer = {
                "question_id": question_id,
                "answer": your_answer
            }
            answer_list.append(new_answer)
            return Question.get_question_byID(question_id) + new_answer
    
    # def get_answers_to_question(self, question_id):
    #     all_answers = []
    #     for item in answer_list:
    #         if item["question_id"] == question_id:
    #             all_answers.append(item)
    #     return Question.get_question_byID(question_id) + all_answers 
             
