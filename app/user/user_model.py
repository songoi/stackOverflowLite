class User(object):
    def get_users(self):
        return self.users_list

    def register_user(self, username, usermail, birthday, userpassword):
        self.username = username
        self.usermail = usermail
        self.birthday = birthday
        self.userpassword = userpassword

        id = len(self.users_list) + 1
        new_user = {
            "mail" : usermail,
            "name" : username,
            "birthday" : birthday,
            "userID" : id,
            "password" : userpassword

        }
        self.users_list.append(new_user)
        return new_user

    def login(self, usermail, userpassword):
        for user in self.users_list:
            if user["mail"] == usermail:
                if user["password"] == userpassword:
                    return True
                else:
                    return False