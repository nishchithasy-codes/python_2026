#Inheritance
class user:
    def __init__(self,username):
        self.username = username
    def login(self):
        print(f"{self.username} logged in.")
class admin(user):
    def delete_user(self):
        print(f"Admin deleted the user {self.username}!")

people = admin("vamshi")
print(people.username)
people.login()
people.delete_user()


class family:
    def __init__(self,surname):
        self.surname = surname
    
class child(family):
    def __init__(self,surname,name):
        super().__init__(surname)
        self.name = name

person1 = child("Gowda","Akshay")
print(f"{person1.name} {person1.surname}")