class account:
    def __init__(self, id, holder_name):
        self.id = id
        self.holder_name = holder_name
        self._balance = 0

    def check_balance(self):
        print(f"Balance: {self._balance}")

    def deposit(self,amount):
        self._balance += amount
        print(f"Amount deposited successfully. Updated balance = {self._balance}")
    
    def withdraw(self,amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Amount withdrawned successfully. Updated balance = {self._balance}")
        else:
            print("Balance is less than ask!!!")

class SavingsAccount(account):
    def calculate_interest(self):
        INTEREST_RATE = 0.04
        interest = self._balance * INTEREST_RATE
        print(f"Interest = {interest}")
class CurrentAccount(account):
    def withdraw(self,amount):
        OVERDRAFT_LIMIT = 1000
        if self._balance + OVERDRAFT_LIMIT >= amount:
            self._balance -= amount
            print(f"Amount withdrawned successfully. Updated balance = {self._balance}")
        else:
            print("Balance is less than ask!!!")

class Bank:
    def __init__(self, name,city):
        self.name = name 
        self.city = city
        self.__accounts = {}

    def create_account(self,id,holder_name, type):
        if type=="SavingsAccount":
            new_account = SavingsAccount(id,holder_name)
        elif type=="CurrentAccount":
            new_account = CurrentAccount(id,holder_name)
        else:
            print("Invalid account type.")
            return None
        self.__accounts[id] = new_account
        print("Account creation is get success.")
        return new_account

    def get_account(self,id):
        if id not in self.__accounts:
            print("\nAccount not found!")
            return None
        else:
            account = self.__accounts[id]
            print(f"\nID= {account.id}\nHolder name: {account.holder_name}")
            return account

cbk = Bank("Chandan bank of karnataka","Mysore")
s1 = cbk.create_account("1.","Chandan","SavingsAccount")
c1 = cbk.create_account("2.","Virat","CurrentAccount")

s1.deposit(1000)
c1.deposit(10)

s1.withdraw(2000)
c1.withdraw(20)

s1.calculate_interest()

