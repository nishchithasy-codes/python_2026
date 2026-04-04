import math

a = float(input("Enter the coefficient of A:"))
b = float(input("Enter the coefficient of B:"))
c = float(input("Enter the coefficient of C:"))

if a == 0:
    print("Not a quadratic equation!")
    breakpoint

d = b*b*-4*a*c  #discriminant

if d > 0:
    root1 = (-b+math.sqrt(d))/(2*a)
    root2 = (-b-math.sqrt(d))/(2*a)
    print("Roots are real distinct.")
    print("Root 1 = ",root1)
    print("Root 2 = ",root2)

elif d == 0:
    r = -b/(2*a)
    print("Roots are real and equal.")
    print("Roots = ",r)

else:
    real = -b/(2*a)
    imag = math.sqrt(-d)/(2*a)
    print("Roots are real complex.")
    print("Root1 = ",real,"+",imag,"i")
    print("Root2 = ",real,"-",imag,"i")