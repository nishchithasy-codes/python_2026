from datetime import date

person_name = input("Enter your name:")
birth_year = int(input("Enter your birth year:"))

current_year = date.today().year
print("Current year is:",current_year)
age = current_year - birth_year

if age > 60:
    print(f"{person_name} is a senior citizen, because the age is {age}")
else:
    print(f"{person_name} is not a senior citizen, because the age is {age}")
