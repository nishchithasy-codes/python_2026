s = input("Enter a string: ")

if s == s[::-1]:
    print("PALINDROME")
else:
    print("Not a palindrome!")


s = input("Enter a string: ")
chr = input("Enter a character: ")

if chr in s:
    print("The character ",chr," is present in ",s)
else:
    print("The character ",chr," is not present in ",s)

str = input("Enter a string: ")
sub_str = input("Enter a sub-string: ")
print("Substring is present at the index: ",str.find(sub_str))

string = input("Enter a string: ")
count = 0
str=[]
for letter in string:
    if letter in str:
        count = count + 1
        print("The character ",letter,"occurs ",count,"times")
    else:
        count=1
        print("The character ",letter,"occurs ",count,"times")