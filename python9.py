s = input("Enter a string: ")
ch = input("Enter a character: ")
c = s.count(ch)
print(f"The character '{ch}' occours '{c}' times in a string '{s}'.")

string = input("Enter a string: ")
count = 0
ch = input("Enter a character: ")
for c in string:
    if ch == c:
        count+=1
print("The character ",ch,"occurs ",count,"times")


string = input("Enter a string: ")
for ch in string:
    if "aeiou" == ch.lower():
        print("The vowel is ",ch,"in a string ",string)

string = input("Enter a string: ")
count = 0
for ch in string.lower():
    if ch.isalpha() and ch not in "aeiou":
        count += 1
print("Consonants: ",count)

for ch in string.lower():
    if ch in "aeiou":
        count += 1
        print("Vowel: ",ch)
print("The count of vowels= ",count)