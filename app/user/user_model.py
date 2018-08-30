user_list = []

class User(object):
    """returns all users"""
    def get_users(self):
        return user_list

    def register_user(self, data={}):
        self.username = data.get("username")
        self.usermail = data.get("usermail")
        self.userpassword = data.get("userpassword")

        id = len(user_list) + 1
        new_user = {
            "mail" : self.usermail,
            "name" : self.username,
            "userID" : id,
            "password" : self.userpassword
        }
        user_list.append(new_user)
        return new_user

    def login(self, usermail, userpassword):
        """check whether the user is in the list"""
        user = [user for user in user_list if user["mail"] == usermail and user["password"] == userpassword]
        if len(user) == 1:
            return True
        return False