num1 = int(input("Enter a first number:"))
num2 = int(input("Enter a second number:"))

print("1. Add")
print("2. Subtract")
print("3. Divide")
print("4. Multiply")

choice = input("Enter your choice:")

if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1-num2)
elif choice == 3:
    if num2 != 0:
        print(num1/num2)
    else:
        print("Invalid input!")
else:
    print(num1*num2)
