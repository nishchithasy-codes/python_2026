#Education system



def display():
    print(f"\nRoll number {roll_no} and the student is {name}, scored {marks}.")

name = ""
roll_no = 0
marks = 0
data_entered = False 

def details():
        global name,roll_no,marks,data_entered
        name = input(("Enter student name:"))
        roll_no = (input(("Enter student roll number: ")))
        marks = (input(("Enter student marks: ")))
        data_entered = True

while True:
    print("1. Add student details.")
    print("2. Display student details.")
    print("3. Exit.")
    choice = (input("Enter your choice:"))
    if choice == '1':
        details()
    elif choice == '2':
        if not data_entered:
             print("Enter the details first!")
             details()
             print("Student details is: ")
             display()
        else:
             display()
    elif choice == '3':
        print('You given for exit,"Thank you"!.')
        break
    else:
        print("Enter choice from the given!")

