class User : 
    #the innit function runs anytime an object is created from this class 
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        
user_1 = User("001", "mario")
user_1.user_id = "002"

print(user_1)
print(user_1.user_id)