num = int(input("Enter a number:"))

fib1 = 0
fib2 = 1

print("The fibonacci series is:")
for i in range(num):
    print(fib1,end = "")
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
