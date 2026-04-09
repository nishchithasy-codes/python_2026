#Liskov substitution principle - sub classes should be able replace their parent class without breaking the program

class birds:
    def move(self):
        pass
class sparrow:
    def move(self):
        print("The sparrrow is flying there!")
class penguin:
    def move(self):
        print("The penguin is swimming there!")

b = birds()
b.move()

s = sparrow()
s.move()

p = penguin()
p.move()

print("\n")
#Interface segragation principle

class work:
    def workable(self):
        pass
class eat:
    def eatable(self):
        pass

class human(work,eat):
    def work(self):
        print("Humans can do the works.")
    def eat(self):
        print("Humans should eat properly.")

class robot(work):
    def work(self):
        print("Robots will replace some works of humans and they can't eat!")
    
man = human()
sofia = robot()

man.work()
man.eat()

sofia.work()
print("\n")
