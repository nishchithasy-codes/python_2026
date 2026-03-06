#NEVER GIVE UP go ahead
#while loop -> executes when the conditions are true

'''is_failed=True
i=1
while is_failed and i<=10:
    print(f"Try again {i}")
    i+=1'''

'''pin = 9988
trails=1
while trails <= 3:
    input_pin=input(f"Trail:{trails} | password>> ")
    trails+=1
    if int(input_pin)==pin:                     #Very very imp string of input_pin should be convrt to integer then only it will work
       print(f"Correct password GOOD!")
       break
    else:
        print(f"Incorrect password\n")'''

i=0
while i<=10:
    x=0
    while x<i:
        print("Vamshi",end="-")
        x+=1
    print(" ")
    i+=1
        
is_failed=True
i=1
while is_failed:
    print(f"Try again{i}")
    if i%2!=0:
        i=i+1
        continue
    print(f"Attempt{i}")
    i=i+1
    if i>10:
        break