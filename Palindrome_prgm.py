#Checking the palindrome condition

num=int(input("Enter the numbers:"))
temp=num
rev=0

while temp!=0:
    digit=temp%10
    rev=digit+(rev*10)
    num=num/10
if num==temp:
    print("It is a palindrome.")
else:
    print("Not a palindrome.")

