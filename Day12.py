#List and dictionaries with for loops 
#List comprehension
#Looping through list
list_of_num = [10, 20, 30, 40, 50]
final_list = []
for num in list_of_num:
    final_list.append(num*2)
    print(final_list)

food_list = ["idli", "Dosa", "palav", "Upma", "Chapathi"]
for food in food_list:
    print(f"I like {food} ")

#Sum of list numbers
l = [1,2,3,4,5]
total = 0
print(f"Initially total = {total}")
for num in l:
    total+=num
    print(total)


#looping through dictionaries -> use loops to iterate over dictionaries 
dic = {"Anand": 95,
       "Ravi": 89,
       "Akshay": 35,
       "Ram": 28}

print("Keys of dic:")
for student in dic:
    print(student)

print("Values of dic:")
for student in dic.values():
    print(student)

print("List of tuples from dic:")
print("type1")
for student_marks in dic.items():               #print list of tupples
    print(student_marks)
#for student,marks in dic.items():          #same as like above dic.items()
   # print(f"{student} - {marks}")

print("type2")
for key,value in dic.items():
    print(f"{key} - {value}")
print("\n")


#Creating dic from lists
students = ["Akshay", "Raksha", "Vamshi", "Siddhesh"]
marks = [90, 92, 78, 66]
student_marks = {}
for index,student in enumerate(students):
    student_marks[student]=marks[index]
print(student_marks)

#another type
students = ["Akshay", "Raksha", "Vamshi", "Siddhesh"]
marks = [90, 92, 78, 66]
student_marks = {}
for i in range(len(students)):
    student_marks[students[i]]=marks[0]
print(student_marks)
print("\n")
#List comprehension -> concised way of lists
#syntax -> new_list = [expression for item in iteration(the_concising) if condition]
l = [1,2,3,4,5,6,7,8,9,10]
dl = [items*2 for items in l]
print(dl)
dl = [items*2 for items in l if items%2==0]
print(dl)
dl = [items for items in l if items<=6]
print(dl)

x = [num for num in range(1,11)]
print("Squaring of numbers from 1 to 10")
dx = [num**2 for num in x]
print(dx)

#for only squaring of even numbers
numbers  = [num for num in range(1,11)]
even_num_sqr = [num**2 for num in numbers if num%2==0]
print("Squaring of only even numbers from 1 to 10")
print(even_num_sqr)
print("\n")

names = ["Amith shah", "Shahjhan", "Dulquer Salman", "Hardik Pandey", "Virat Kohli"]
fam_actors = [name for name in names]
print(fam_actors)
fam_actors = [name[0] for name in names]
print(fam_actors)
print("\n")
#Dictionary comprehensions -> concised way of dictionaries
cities_population = {"Bengaluru":100,
                     "Mandya":59,
                     "Mysuru":35,
                     "Goa":10,
                     "Pondichery":9,
                     "Assam":5}
print(cities_population)
print(cities_population.items()) #print like list of tuples in tuples
print("\n")
large_cities = {large_city for large_city in cities_population}
print("The keys are printed not in ordered way bcz dic are unindexed")
print(large_cities)            #print only the key values
print("\n")
large_cities = {large_city for large_city in cities_population.values()}
print("The values are printed not in ordered way bcz dic are unindexed")
print(large_cities)
print("\n")
large_citieses = {large_city:population for large_city,population in cities_population.items() if population >10}
print("Cities with population > 10")
print(large_citieses)
print('\n')
large_citieses = {small_city:population for small_city,population in cities_population.items() if population <=10}
print("Cities with population <= 10")
print(large_citieses)
print('\n')

#Spliting strings to create list
list = "Hello-Everyone how-are-you all"
splitted_list = list.split()            #split() -> says that when space comes split that string
print("Initia string")
print(f"{list}")
print("\n")
print("Splitted string which is in a list")
print(f"{splitted_list}")
print("\n")
new_list = list.split("-")
print("Split the string whenever - this comes")
print(new_list)
print("\n")

#user input of list
list = input("Enter a list of numbers you want:")
print(list)
list = list.split()
print("output was list in string form")
print(list)
list = [int(num) for num in list]       
print("Output was list in integer form ")
#list=[int(num) for num in input("Enter a list of numbers you want:").split()]          -> concised form of above list syntax
print(list)