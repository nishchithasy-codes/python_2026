#bank menu driven prgm

def bank_balance():
    print("----------Bank Account----------")
    print("1. balance\n2. deposite\n3. withdraw\n4. exit")

balance = 0

while True:
    bank_balance()
    choice = int(input("Enter your choice:"))
    #if choice in {1,2,3}:
    if choice == 1:
        print("Balance is:",balance)
    elif choice==2:
        amount = int(input(("Enter the depositing amount:")))
        balance += amount
    elif choice==3:
        amount = int(input(("Enter the withdrawing amount:")))
        balance -= amount
    else:
        print("Thank you!")
        break
       



