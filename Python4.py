class ATM:      
    def __init__(self,balance):
        self.balance = balance          #Public

Appu = ATM(1000)
print(Appu.balance)
print("\n")
class ATM:
    def __init__(self,balance):
        self.__balance = balance            #private

    def check_balance(self):
        print(self.__balance)

Appu = ATM(1000)
