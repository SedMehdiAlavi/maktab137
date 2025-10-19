class User:
    users = []

    def __init__(self, name):
        self.name = name
        User.users.append(self)

    @classmethod
    def get_user_count(self):
        return len(User.users)


u1 = User("Alice")
u2 = User("Bob")
print(User.get_user_count())

