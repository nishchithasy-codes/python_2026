marks = []

print("Enter marks of 6 subjects:")
for i in range(6):
    mark = int(input(f"Enter marks for subject{i+1}: "))
    marks.append(mark)

n = len(marks)

for i in range(n-1):
    for j in range(n-i-1):
        if marks[j] < marks[j+1]:
            marks[j],marks[j+1]=marks[j+1],marks[j]
print("The marks of 6 subjects from highest to lowest is:")
for mark in marks:
    print(mark)
    