#Getters, setters
# Method Overloading and method overridding
#super() function and Abstract classes


#Getters ans Setters
class students:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name

    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age > 0 and isinstance(age,int):
            self.__age = age
        else:
            print("Invalid age!")

s1 = students("Chandan",24)

print("Initially the name was:",s1.get_name())
s1.set_name("Darshan")
print("After the use of getters, the name becomes:",s1.get_name())

print("\n")

print("The age at first:",s1.get_age())
s1.set_age(25)
print("After setting the age:",s1.get_age())


#Method overloading can define multiple methods using a same variable name
class calculator:
    def add(self,a,b,c=0):
        print(a+b+c)
sum = calculator()
print("The sum (2,2,2) is:")
sum.add(2,2,2)
print("Now the sum(11,1) is:")
sum.add(11,1)

#Method overridding >>>child class alter or extend the parent class method
class animal:
    def make_sound(self):
        print("That animal is making a sound!")
    

class dog(animal):
    def make_sound(self):
        print("That animal is dog and it is>>> barking!")
class cat(animal):
    def make_sound(self):
        print("The cat making a sound like>>> meow")

a = animal()
a.make_sound()
d = dog()
d.make_sound()
c = cat()
c.make_sound()

#Super()
class food:
    def taste(self):
        print("It's tasting soo good!")

class dosa(food):
    def taste(self):
        print("Super taste!!!")

class biryani(food):
    def taste(self):
        super().taste()
        print("That is biryani is super!!")

#hotel = food()
restuarant1 = biryani()     #parent class method will come here
restuarant1.taste()     #Own class method

restuarant2 = dosa()        #No super(), therefore no parent class methods here, soo it is showing none
restuarant2.taste()

class animal:
    
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} is making a sound.")


class dog(animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        super().sound()
        print(f"{self.name} barks")
        self.sound()


d = dog("Buddy","labrador")
d.sound()


