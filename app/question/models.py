question_list = [
            {
                "post_id" : 1,
                "question" : "whats the distance between the sun and the moon",
                "answer":[ 
                {
                    "answer_id" : 1,
                    "answer" : "205,524km"
                } ]
            }
        ]

class Question(object):
    def get_questions(self):
        return question_list

    def get_question_byID(self, question_id):
        for item in question_list:
            print("Current Item:", item)
            if item["post_id"] == question_id:
                return item
            return "No question with id {}".format(str(question_id))


    def create_question(self, the_question):
        self.the_question = the_question

        id = len(question_list) + 1
        new_question = {
            "post_id" : id,
            "question" : the_question,
            "answer" : []        
        }
        
        question_list.append(new_question)

        return self.get_question_byID(id)

    def del_question(self, question_id):
        print(len(question_list))

        for item in question_list:
            if item["post_id"] == question_id: 
                question_list.remove(item)
                return question_list

            return "No question with id {}".format(str(question_id))

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
        


