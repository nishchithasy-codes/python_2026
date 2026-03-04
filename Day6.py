#Lists in python
Programming_languages = ["Python", "Ruby", "C++", "JAVA"]

print(Programming_languages[1])
print(Programming_languages[0])     #Accessing lists
print(Programming_languages[3])
print(Programming_languages[2])

Programming_languages.append("Javascript")  #add Javascript to th python_programming list 
print(Programming_languages)
Programming_languages.insert(1,"C#")        #at the 1st index add c#
print(Programming_languages)
Programming_languages.remove("Ruby")        #remove ruby from the list
print(Programming_languages)

Programming_languages.pop()         #(Modifying lists) remove last element
print(Programming_languages)        
Programming_languages.pop(0)        #remove first element that is at the element 0th index
print(Programming_languages)

#List functions and methods
#common functions 
len(Programming_languages)

num = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(len(num))                         #length of the list
print(sorted(num))                      #correct ordered list
print(sum(num))                         #sum of the list

#Common methods
print(num.index(3))       #print the number at the index 3 here it is 7
print(num.count(2))                       #count how many times the number 2 is repeated
num.reverse()                             #reverses the list
print(num)
print(num[::-1])                          #this also reverse the list


#Nested list          #matrix form
matrix = [
            [1, 2, 3],        #coma should be there after one list in a nested list
            [4, 5, 6],
            [7, 8, 9]
          ]
print(matrix[0])                        #print 0th index row
print(matrix[0][2])                     #print the num at the 0th row and 2nd index, here it is 3 

list = [[1, 2], [2, 3]]                 #nested list
print(list)
print(type(list))                       #nested list


#Slicing the string

l = ("S", "O", "F", "T", "W", "A", "R", "E")
print(l[0:4])     #string from 0th index to 4th position
print(l[4:8])   #string fron 4th index to 8th position
print(l[0::])       #print start to end
print(l[:8])        #print till end here end is in 8th position
print(l[0::2])      #It will skip one element
print(l[1:])        #skip the element behind entered index value
