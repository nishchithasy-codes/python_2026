units = int(input("Enter number of units: "))

if units <= 50:
    amount = units*2
elif units<= 100:
    amount = (50*2) + (units-50)*4
elif units <= 50:
    amount = (50*2) + (50*4) + (units-100)*6
else:
    amount = (50*2)+(50*4)+(50*6)+(units-150)*8

print("thec total bill amount is: ",amount)
