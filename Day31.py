a = int(input("Enter a number: "))
b = int(input("Enter anumber:"))

try:
    print(a/b)
except Exception as e:
    print(f"Error occur -> {e}")
else:
    print("No error came,**Congrats**.")
finally:
    print("Program ended here.")
    
try:
    boy = input("Whom do you want to marry:")
    if boy.lower() != "chandan":
        raise Exception("You can only choose Chandan,select him.")
except Exception as e:
    print(f"Error is {e}.") 
else:
    print("Yes, Chandan is ready.Have nice journey!")

