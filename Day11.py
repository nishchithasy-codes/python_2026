#LOOPS      (for loop -> used when the number of iterations are known)
#syntax -> for item in range (start,stop,step)

'''cities = ["bengaluru","mandya","Mysuru","Raichur"]
print("The cities are:")
for city in cities:
    #print(city)
    print(city, end=" ")

print("\n")

cities = ["bengaluru","mandya","Mysuru","Raichur"]
print("The index values are:")                          #To print the index value use enumerate
for city_index, city in enumerate(cities):
    print(f"{city} at the index of {city_index}.")

print("\n")

cities = ["Bengaluru","Mandya","Mysuru","Raichur"]
print("The positions values are:")
for city_index, city in enumerate(cities):
    print(f"{city} at the position of {city_index+1}")

print("\n")

cities = ["Bengaluru","Mandya","Mysuru","Raichur"]
for city in cities:
    if city=="Mandya":
        print(f"Hey! your native city {city} was also in the list.")
        continue
    print(city)

print("\n")

print(f"Numbers from one to ten:")
for i in range(1,11):
    #print(i)
    print(i,end=" ")

print("\n")

print(f"Odd numbers from one to hundered are:")
for i in range (1,101,2):
    print(i,end=" ")

print("\n")

#dictionary -> a key value pair is called dictionary
dic={"key1": "value1",
     "key2": "value2",
     "key": "value"
    }
print(dic)

details={"Name": "Vamshi S Y",
         "Age": 16,
         "Qualification": "Student",
        }
print(details)
print("\n")
for key,value in details.items():               #details.items() -> convert dic to tuple
    print(key," ",value)

#Multiplication table'''


'''for i in range(1,11):
    print(f"{2}x{i} = {2*i}")           #This is for a specific number'''
for i in range (1,11):
    for j in range(1,11):
        print(f"{i}x{j} = {i*j}")          #print tables from 1 to 10
        


