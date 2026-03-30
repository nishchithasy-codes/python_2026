    #*********************************SOLID PRINCIPLES IN PYTHON****************************************

'''
S >>> single responsibility principle
O >>> open/closed principle
L >>> Liskov substitution principle
I >>> Interface segregation principle
D >>> Dependency inversion principle
'''

#Single responsibility principle

class student:
    def  __init__(self,name):
        self.name = name

class StudentData:
    def save(self,student):
        print(f"Saving student, {student.name} to database....")

class ReportCard:
    def generate(self,student):
        print(f"Generating report card for student>>>{student.name}.")

s1 = student("Chandan")
db = StudentData()
rc = ReportCard()

db.save(s1)
rc.generate(s1)
print("\n")

#Open/closed principle

class Discount:
    def get_discount(self):
        return 0
    
class RegularCustomer:
    def get_discount(self):
        print("Discount is 10%")
    
class PremiumCustomer:
    def get_discount(self):
        print("DIscount is 20%")
    
d1 = Discount()
r1 = RegularCustomer()
p1 = PremiumCustomer()

r1.get_discount()
p1.get_discount()