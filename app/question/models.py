question_list = [
            {
                "post_id" : 1,
                "question" : "whats the distance between the sun and the moon"
            }
        ]

class Question(object):
    def get_questions(self):
        return question_list

    def get_question_byID(self, question_id):
        for item in question_list:
            if item["post_id"] == question_id:
                return item
             


    def create_question(self, the_question):
        self.the_question = the_question

        id = len(question_list) + 1
        new_question = {
            "post_id" : id,
            "question" : the_question        
        }
        
        question_list.append(new_question)

        return self.get_question_byID(id)

    # def del_question(self, question_id):
    #     for item in question_list:
    #         if item["post_id"] == question_id: 
    #             item_index = question_list.index(item)
    #             question_list.remove(item)

    #     return question_list

    #         # return "No question with id {}".format(str(question_id))

        


