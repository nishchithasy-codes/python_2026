#dictionaries
dishes = {"Mandya": "Chicken sambar",
              "Raichur": "Roti and dal",
              "Mangalore": "Neer dosa",
              "Mysuru": "Mysur paak sweet0",
              "Bengaluru": "Bisi bele baath"}
print(dishes)
dishes["Davanagere"] = "Benne dosa"  #add
print(dishes)
dishes["Bengaluru"] = "Pizza"       #update
print(dishes)
del dishes["Raichur"]       #remove
print(dishes)
print(dishes.keys())
print(dishes.values())
print("\n")
d = {"frnd1": {"name": "appu",
               "fav_sub": "maths",
               "fav_food": "Egg rice"},
    "frnd2": {"name":"siddu",
              "fav_sub": "English",
              "fav_food": "Dosa"}
    }
print(d)
print("Fav_food of frnd1 is",end=" ")
print(d["frnd1"]["fav_food"])  
print("\n")
#f = d["frnd1"]
#print(f["fav_food"])
#conditional statements
age = int(input("enter your age: "))
if age<=5:
    print("Bus pass is free")
elif age>=60:
    print("You got a senior citizen discount")
else:
    print("You have to pay the full price")
print("\n")
#to know what the time +2 for 10 with that time and to add  the time -2 for 10 with that time

import time

i=10
while i>=0:
    print(i)
    time.sleep(1)       #wait for entered integer seconds
    i=i-1
print("Hello! everyone 😁 happy to see ❤️")


i=3
j=1
for j in range(1,11):
    print(f"{i}x{j}={i*j}")
    j=j+1
i=1
sum=0
for i in range(1,11):       #Formula= 10*11/2
    sum=sum+i

print("Sum=",sum)
str = input("Enter your name: ")
length=0
length = len(str)
for index,letter in enumerate(str):
    print(letter)
    print(length)

name = input("Enter your name: ")
for letter in name:
    print(letter)

vowels = "aeiouAEIOU"
name = input("Enter your name:")
for letter in name:
    if letter in vowels:
        print(letter)

foods = ["idli", "dosa", "poori","Palav"]
print(foods)
u_foods = [item.upper() for item in foods]
print(u_foods)

#dic comperhrensions
products = {"Sugar":45,
       "Corn flour": 30,
        "Mngoes": 100,
         "Reva": 25,
          "green gram": 55
      }
print(products)
total=0
print("TOtal price of all items is ")
for _, price in products.items():       #_ indicates keys are not using
    total=total+price
print(total)
print(sum(list(products.values())))
print("\n")
l = [1,2,3,4,5,6,7,8,9,10]
dl = [item**2 for item in range(1,11)]
print(dl)
print("\n")
students =[{"name": "vamshi",
            "age": 16,
            "marks": 100},
            {"name":"Akshay",
            "age": 10,
            "marks": 92},
            {"name":"Raksha",
            "age":12,
            "marks": 97}]
for student in students:
    #print(student)
    print(student["name"], "and scored",student["marks"],"marks")
print("\n")

rows = int(input("Enter the number of rows:"))
matrix = []
for i in range(rows,rows+1):
    row = [int(num) for num in input(f"Enter row {i+1}:").split()]
    matrix.append(row)
print(matrix)

rows = int(input("Enter number of rows:"))
columns = int(input("Enter number of columns:"))
matrix =[]
for i in range(rows):
    row = []
    for j in range(columns):
        x = int(input("Enter the element:"))
        row.append(x)
    matrix.append(row)
print(matrix)