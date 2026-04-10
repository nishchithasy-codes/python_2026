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