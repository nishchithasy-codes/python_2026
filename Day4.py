#String manipulation

Message = " Python Developer\n "
print(Message.upper())
print(Message.lower())
print(Message.strip())
print(Message.replace("Developer","World"))
print(Message.upper()*10)
print(len(Message))
position = Message.find("Python")
print(position)
print(Message.startswith(" Python "))       #True
print(Message.endswith("Nothing"))          #false because it ends with the word developer 
print(Message.count("Developer"))           #number of times that particular word repeat here it is 1

text = ' I am a "tech pythonist" '      #For double codes inside a string
print(text)

conversation = '''
                    Vamshi said: "Hi, Akshay!".\n            
                    Akshay replied: "Hello,vamshi!".\n
                    vamshi asked: Are learning "Python?".\n
                    Akshay replied: Yes!! I am.\n
                    Vamshi told: Ohh it's good! all the best, be a ***Best Coder***.\n
                    Akshay replied: Thank you!!\n
                '''                                 #for multi line string statements use triple codes
print(conversation)

#Accessing string character(Python uses zero based indexing)
content_creater = "Python full course teaching"
print(content_creater[0])           #o/p is P bcz we are giving the index 0(Index=position-1)
print(content_creater[1])
print(content_creater[2])
print(content_creater[3])
print(content_creater[4])
print(content_creater[5])
print(content_creater[7:18])    #string slicing(starting word index value:ending word position value)

#If we give position values
print(content_creater[:7])      #word upto 7th position
print(content_creater[7:])      #word after 7th position
print(content_creater[::2])     #skip one letter and print the word, if we give [::3] it will skip 2 letters

#Escape sequences
"""
\n  New line
\t  Tab space
\\  Backslash
"""