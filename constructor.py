class mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    
    def display(self):
        print(f"{self.brand} coasts around {self.price}")

m1 = mobile("Nokia",10000)
m2 = mobile("iphone",70000)
m1.display()
m2.display()