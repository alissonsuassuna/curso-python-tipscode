class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 #Seguidores
        self.following = 0 #Seguindo

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Jesus Cristo")
user_2 = User("002", "João Batista")
user_3 = User("003", "Rei Davi")


user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)