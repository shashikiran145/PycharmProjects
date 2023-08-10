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
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "shashi")
user_2 = User("002", "kiran")

user_1.follow(user_2)
# user_2.follow(user_1)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
