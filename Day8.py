#Dictionaries  ->collection of key value pair
'''dic = {"Name": "Appu",
       "Age": 16,
       "Class": 11,
      }
x = dic.pop("Age")
print(x)
print(dic["Name"])
#print(dic["Age"])
print(dic["Class"])
print(dic.get("Chandan","Not found"))       #program won't crash 
dic["Ammu"] = "23rd,march"
dic.pop("Class")       #removes class key
dic["Appu"] = "11th,sep"
print(dic)'''

'''famous_things = {"mandya": "sugar cane",
          "bengaluru": "traffic",
          "maddur": "maddur vada",
          "raichur": "roti"
         }
print(famous_things)
print(famous_things.keys())
print(famous_things.values())
print(famous_things.items())          #it will print dic in the form of list
print(famous_things.clear())          #Clear everything in the dic
new_one = {"mysuru":"mysur pak"}
famous_things.update(new_one)
print(famous_things)'''

class_10th = {"name":"nishchitha s y",
              "total marks": 590,
              "grade": "distinction",
              "percentage": 94.3
              }
print(class_10th)

class_12th = {"name": "Nishchitha s y",
              "total marks": 563,
              "percentage": 93.8,
              "grade": "Distinction"
              }
print(class_12th)

main_classes = [class_10th,class_12th]
print(main_classes)
print(f"Marks in 10th and 12th are {class_10th["total marks"]} and {class_12th["total marks"]} respectively")
print("Congrats!!!Dear your hard work.\n")

item1 = {"product": "sugar",
         "weight": 3,
         "price": 50
         }
item2 = {"product": "Corn flour",
         "weight": 2,
          "price": 45
        }
total_items = [item1,item2]
print(total_items)
print(f"\nThe products are {item1["product"]} and {item2["product"]}.\n")
print(f"The weight of all the products was {item1["weight"]+item2["weight"]}.\n")
print(f"The total price is {item1["price"]+item2["price"]}.\n")
