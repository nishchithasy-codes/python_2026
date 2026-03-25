#Creating a bank account with getters and setters

class account:
    def __init__(self,balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self,balance):
        if balance > 0:
            self.__balance = balance
        else:
            print("Balance should not be lesser than zero!")

amount = account(30000)
print("Initial balance:",amount.get_balance())
amount.set_balance(25000)
print("After setting, the balance is:",amount.get_balance())

amount.set_balance(-200)        #When amount goes negative value

#Creating a clculator with method overloading

class calculator:
    def multiply(self,a,b,c=1):
        print(a*b*c)

multi = calculator()
multi.multiply(2,3)
multi.multiply(2,2,2)

#Method overridding
class shape:
    def draw(self):
        print("Drawing the shape!")
    
class circle(shape):
    def draw(self):
        print("Drawing the circle.")

class square(shape):
    def draw(self):
        print("drawing the square.")

d = shape()
print(d.draw())
cir = circle()
print(cir.draw())
sqr = square()
print(sqr.draw())

#Abstract method

from abc import ABC,abstractmethod
class employee(ABC):
    @abstractmethod
    def calculate_salary():
        pass

class manager(employee):
    def __init__(self,working_hour,rate_per_hour):
        self.working_hour = working_hour
        self.rate_per_hour = rate_per_hour

    def calculate_salary(self):
        print("The total salary is:4000")

employee1 = manager("8 hours","500")
print("Worked for >>>",employee1.working_hour)
print("Rate per hour work is >>>",employee1.rate_per_hour)
print("Total salary >>>",employee1.calculate_salary())
