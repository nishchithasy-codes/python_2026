#Inheritance

class vehicle:
    def start(self):
        print("Vehicle is starting")

class bike(vehicle):
    def __init__(self,name):
        self.name = name
    def ride(self):
        print("It was ridding now!")

b = bike("Royal Enfield")
b.start()
b.ride()

class shape:
    def calc_area(self):
        print("The are of:")

class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    
    def calc_area(self):
        print(f"Circle is: {22/7*self.radius*self.radius}")

class rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def calc_area(self):
        print(f"Rectangle is: {self.l*self.b}")

c = circle(5)
c.calc_area()
R = rectangle(2,2)
R.calc_area()

class phone:
    def take_picture(self):
        #Call os api to open camera
        #wait for users click
        #process the image
        #store image
        #return preview
        print("picture was taken")
p =phone()
p.take_picture()
