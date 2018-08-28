question_list = [
<<<<<<< HEAD
            {
                "post_id" : 1,
                "question" : "whats the distance between the sun and the moon"
            }
        ]
=======
    {
        "post_id" : 1,
        "question" : "whats the distance between the sun and the moon"
    }
]
>>>>>>> feedback implementation

class Question(object):
    def get_questions(self):
        return question_list

    def get_question_by_id(self, question_id):
<<<<<<< HEAD
        for item in question_list:
            if item["post_id"] == question_id:
<<<<<<< HEAD
                 print(item)
        
        return item
             
=======
                return item
            return "No question with id {}".format(str(question_id))
>>>>>>> feedback implementation
=======
        question =  [item for item in question_list if item["post_id"] == question_id]
        if len(question) == 0:
            return "No question with id {}".format(str(question_id))
        return question
>>>>>>> Handle question logic


    def create_question(self, the_question):
        self.the_question = the_question

        id = len(question_list) + 1
        new_question = {
            "post_id" : id,
<<<<<<< HEAD
            "question" : the_question        
=======
            "question" : the_question,        
>>>>>>> feedback implementation
        }
        
        question_list.append(new_question)

<<<<<<< HEAD
<<<<<<< HEAD
        return question_list
        # self.get_question_byID(id)

    def del_question(self, question_id):
        for item in question_list:
            if item["post_id"] == question_id: 
                item_index = question_list.index(item)
                question_list.remove(item)

        return question_list

class Check_user_input(object):
    def check_validity(self, user_input):
        data = " ".join(char for char in user_input if char.isalnum())
        if len(data) == 0:
            return "invalid user input"

        elif len(data) <=3:
            return "user input too short"

        else:
            return "valid"
            

        

=======
        return self.get_question_byID(id)
=======
        return self.get_question_by_id(id)
>>>>>>> Handle question logic

    def del_question(self, question_id):      
        if question_id >len(question_list) or question_id <= 0:
            return "No question with id {}".format(str(question_id))
                
        else: 
            for item in question_list:
                if item["post_id"] == question_id: 
                    question_list.remove(item)
                return question_list
        

    
>>>>>>> feedback implementation

