class User(object):
    def __init__(self, username, usermail, userpassword, birthday):
        self.username = username
        self.usermail = usermail
        self.birthday = birthday
        self.userpassword = userpassword
        self.users_list = []

    def get_users(self):
        return self.users_list

    def register_user(self, username, usermail, birthday, userpassword):
        id = len(self.users_list) + 1
        new_user = {
            "mail" : usermail,
            "name" : username,
            "birthday" : birthday,
            "userID" : id,
            "password" : userpassword

        }
        return self.users_list.append(new_user)

    def login(self, usermail, userpassword, username=None):
        for user in self.users_list:
            if user["name"] or user["userpassword"] in self.users_list:
                if user["password"] == userpassword and user["mail"] == usermail:
                    print ("login successfull")
                else:
                    print("authorizeation denied")
