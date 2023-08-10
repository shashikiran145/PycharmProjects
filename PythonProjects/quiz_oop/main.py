# class User:
#     pass
# user_1 = User()
#
# user_1.id = "001"
# user_1.username = "shashi"
#
# print(user_1.username)
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username


user_1 = User("001", "shashi")

print(user_1.name)
