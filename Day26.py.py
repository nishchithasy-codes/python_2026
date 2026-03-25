class mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    
    def display(self):
        print(f"{self.brand} coasts around {self.price}")

m1 = mobile("Nokia",10000)
m2 = mobile("iphone",70000)
m1.display()
m2.display()


class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display_info(self):
        print(f"{self.name} scored {self.marks} marks.")

s1 = student("Chandan",99)
s2 = student("Darshan",90)
s1.display_info()
s2.display_info()