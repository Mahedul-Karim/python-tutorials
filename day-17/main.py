class User:
    
    def __init__(self,user_id,username):
        self.user_id = user_id
        self.username = username
        self.followers = 0

    def update_followers(self):
        self.followers += 1


user_1 = User("SfgidS","John Doe")
print(user_1.followers)
user_1.update_followers()
print(user_1.followers)

