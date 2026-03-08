print("Namaste, nanna hesaru Nishchitha S Y")
#arithmatic operations
a = 1
b= 2
print(a+b)
print(a-b)
print(a/b)
print(a*b)

#Swapping two numbers
a = 5
b = 10
print("Before swapping")
print(a)
print(b)
c = a
a = b
b = c
print("After swapping")
print(a)
print(b)
a,b = 3,6
print("Before swapping")
print(a)
print(b)
(a,b) = (b,a)
print("After swapping")
print(a)
print(b)
a,b = 10,20
print(f"a: {a},b: {b}")
a = a^b
b = a^b
a = a^b
print(f"a: {a},b: {b}")

#Greeting program
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name},your age is {age}")

#String manipulation
string = input("Enter any sentence: ")
print(f"The string you entered is: {string}")
print(string.upper())
print(string.lower())
print(string.replace(" ","__"))             #tempororily replacing method. For permanent replaced string -> s = s.replace(" ","__") print(s)
print(string.strip())                       #removes left and right side spaces       

s = input("String: ")
print(s)
print(f"Length of a string ={len(s)}")
print(f"length of a string without space counting={len(s.replace(" ",""))}")
print("hello\n\tworld\nThis is a backslash: \\")        #escape sequ

a = input("Enter a number: ")
b = input("Enter a number: ")
print(int(a>10 and b>10))
print(int(a>10 or b>10))
print("In the above output either of two numbers one is >10")
print(not(a>0)) #print false bcz a is >0 

age = int(input("Enter your age: "))
if age>18:
    print(f"You are adult")
elif age>60:
    print("Your age is 60")
else:
    print("You are not an adult")

#Checking the presence
s = input("Enter a string: ")
print("n" in s)     #print true if n is in the string otherwise false
print("Python" not in s)    ##print true if python  is in the string otherwise false
a,b = 5,6
print(a&b)      #bitwise & operator

#lists
l = [1, "a",True,2,100]
l.append("bye")
l.insert(1,"Inserted succesfully")
print(l)
del l[2]
print(l)
l[2]
print(l)
l.remove(l[2])      #removes 2nd index value

#sorting the list

l = [1,2,3,4,5]
print(l)
l.sort()        #ascending order
print(l)
l.sort(reverse = True)   #l[::-1]also reverses the list    #decending order
print(l)

t1 = (1,2,3,4,5)
print(t1[1:3])
t2 = (6,7,8,9,10)
t = t1 + t2
print(t)
my_fav = {"Apple","orange"}
Frnd_fav = {"Butterfruit","Papaya"}
fav_fruits = my_fav | Frnd_fav   #union -> combine all elements and remove duplicates
print(fav_fruits)
fav_fruits = my_fav & Frnd_fav  #intersection -> Returns elements that common in both the sets
print(fav_fruits)
diff_fruits = my_fav - Frnd_fav     #difference -> in first set if any element matches with 2nd set, it will remove it
print(diff_fruits)
my_fav.add("Butter fruit")
print(my_fav)       #set is not ordered
l = [1,22,33,4,55,66]
set = set(l)
tuple = tuple(l)
print(set,tuple)
set.add(77)
print(set,tuple)