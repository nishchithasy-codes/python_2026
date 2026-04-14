from datetime import date
current_year = date.today().year

try:
    age = int(input("Enter your age: "))
    century = 100 - age
    cen_year = current_year + century
    print(f"You will complete 100 years after {century} years!")
    if age <= 0:
        raise Exception("Age should be an integer and greater than zero!")
except Exception as e:
    print(f"'Error' {e}.")
else:
    print(f"Now you are in the year of {current_year} by {cen_year} year, you are going to complete 100 years of your life jouney!.")
finally:
    print("Thank you.")

