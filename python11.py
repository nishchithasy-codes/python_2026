sentence = input("Write any sentence here: ")
words = sentence.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print(f"The longest word in a sentence '{sentence}' is: {longest}")

s7 = input("Enter a string: ")
result = ""
for ch in s7:
    if ch not in result:
        result += ch
    else:
        result= result+"*"
print("After removing the duplicate characters: ",result)

s8 = input("Enter a string: ")
count = 0
for ch in s8:
    if not ch.isalpha() and not ch.isdigit():
        count = count+1
print("The count of special characters is = ",count)    #Space will aslo get counted

#TUPLE
students_record = []
n = int(input("Enter number of students: "))
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    age = int(input(f"Enter age os student {i+1}: "))
    students_record.append(name)
    students_record.append(age)
print(students_record)


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
def calc(a,b):
    sum = a+b
    difference = abs(a-b)
    multiply = a*b
    return sum,difference,multiply
sum,difference,multiply = calc(a,b)
print("The sum,difference and multiplication of those two numbers is: ")
print("Sum=",sum,"\nDifference=",difference,"\nMultiply=",multiply)

num = []
n = int(input("enter how many elements: "))
print(f"Enter {n} elements: ")
for i in range(n):
    val = int(input())
    num.append(val)
for number in num:
    if number%2==0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

num = []
n = int(input("enter how many elements: "))
print(f"Enter {n} elements: ")
for i in range(n):
    val = int(input())
    num.append(val)
double=[]
for number in num:
    sqr = number**2
    double.append(sqr)
print("The square of all the elements in a list is: ",double)