with open("notes.txt","r")as file:
    print("reading entire fiel.")
    print(file.read())

print("\n")
file = open("notes.txt","r")
print("Reads only first line of the file.")
print(file.readline())
file.close()
print("\n")
file = open("notes.txt","r")
print("Reading all the lines of the file.")
print(file.readlines())
