user_list = [
    {
        "mail" : "donald@duck.com",
        "name": "Donald Duck",
        "birthday" : "12.4.1988",
        "userID" : 1,
        "password" : "thelegendliveson"
    }
]

class User(object): 
    def get_users(self):
        return users_list

    def register_user(self, username, usermail, birthday, userpassword):
        self.username = username
        self.usermail = usermail
        self.birthday = birthday
        self.userpassword = userpassword

        id = len(user_list) + 1
        new_user = {
            "mail" : usermail,
            "name" : username,
            "birthday" : birthday,
            "userID" : id,
            "password" : userpassword
        }
        user_list.append(new_user)
        return new_user

    def login(self, usermail, userpassword):
        for user in user_list:
            if user["mail"] == usermail:
                if user["password"] == userpassword:
                    return True
                else:
                    return False