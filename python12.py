n = int(input("Enter how many elements: "))
num = []
flag = True
print("Enter",n,"elements: ")
for i in range(n):
    val = int(input())
    num.append(val)
for number in num:
    if number<=1:
        print(number,"not a prime.")
    else:
        flag = True
        for i in range(2,number):
            if number%i==0:
                flag = False
                break
        if flag:
            print(number," is prime")
        else:
            print(number,"is not a prime.")

n = int(input("Enter how many elements: "))
num = []
sum=0
print("Enter",n,"elements:")
for i in range(n):
    val =int(input())
    num.append(val)
for number in num:
    sum = sum+ number
print("The sum of list numbers is= ",sum)

n = int(input("Enter how many elements: "))
num = []
print("Enter",n,"elements:")
for i in range(n):
    val =int(input())
    num.append(val)
max=num[0]
for number in num:
    if max<number:
        max=number
print("The largest element in the list is: ",max)


n = int(input("Enter how many elements: "))
num = []
numbers=[]
print("Enter",n,"elements:")
for i in range(n):
    val =int(input())
    num.append(val)
for number in num:
    if number not in numbers:
        numbers.append(number)
print("List without duplicate elements:",numbers)

#   MATRIX
rows = int(input("Enter number of row: "))
cols = int(input("Enter number of columns: "))
A=[]
B=[]
result=[]
print("Enter matrix 'A' elements: ")
for i in range(rows):
    row=[]
    for j in range(cols):
        val=int(input())
        row.append(val)
    A.append(row)
print("Enter matrix 'B' elements: ")
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input())
        row.append(val)
    B.append(row)

print("Matrix 'A': ")
for row in A:
    print(row)
print("Matrix 'B': ")
for row in B:
    print(row)

for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(A[i][j]+B[i][j])
    result.append(row)
print("The result of addition matrix is: ")
for row in result:
    print(row)