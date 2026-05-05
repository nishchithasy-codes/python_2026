s1 = input("Enter a string: ")
print("The reverse of string ",s1,"is ",s1[::-1])

s2 = input("Enter a string: ")
rev = ""
for letter in s2:
    rev = letter + rev
print("Reversed: ",rev)

s3 = input("Enter a string: ")
words = s3.split()
count = 0
for word in words:
    count +=1
print(f"The count of words in a string '{s3}' is = {count}")

print(s3.split())
print(s3.replace(" ","*"))

s4 = input("Enter a string: ")
result = ""
for ch in s4:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch)-32)
    else:
        result += ch
print(result)

s5 = input("Enter a string: ")
digits = 0
alphabets = 0
for ch in s5:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        alphabets +=1
print("The number of digits = ",digits)
print("The count of alphabets = ",alphabets)