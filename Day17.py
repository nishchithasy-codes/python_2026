#Advanced concepts of functions
#Variable length arguments
#Using args with one *      args -> collects numbers into a tuple

def total_sum(*numbers):
    result=0
    for num in numbers:
        result=result+num
    return result



def add(*numbers):
    return sum(numbers)

print(add(101,1,1))

#using kwargs with two **           kwargs -> collects a key,value pair of data
def student_info(**details):
    for key,value in details.items():
        print(f"{key}:{value}")

student_info()
student_info(name="Anand",age="22",course="Python")
student_info(name="Anjali",section="C",age="17")


print(total_sum(1,2,3,4,5))     #comand click on funtion call will take to the function code

#LAMBDA FUNCTIONS   -> small func take any number of arguments but only one expression should be

#Normal func
def add(num1,num2):
    return int(num1+num2)

print(add(2,3))
print(add(3,4))

#Lambda function, syntax -> 

add = lambda a,b: a+b
print(add(2,1)) #o/p -> 3

sub = lambda a,b: a-b
print(sub(1,1))

students = [{"name":"Vamshi","course":"python","marks":80},
            {"name":"Akshay","course":"Java","marks":95},
            {"name":"Raksha","course":"C++","marks":35}]

students.sort(key = lambda x: x["marks"])      # ->Asscending order 
print(students)
students.sort(key = lambda x: x["marks"],reverse=True)      #-> Decending order
print(students)

#Recurssion     -> Occurs when function calls itself againa and again 

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print("Factorial of 3 is",end=" ")
print(factorial(3))
print("Factorial of 5 is",end=" ")
print(factorial(5))

#Nested functions   ->Function inside a another function

def calculate(a,b):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def multiple():
        print(a*b)
    add()
    sub()
    multiple()

calculate(10,20)

