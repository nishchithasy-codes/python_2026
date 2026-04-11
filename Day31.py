#Dependency Inversion principle

class InputDevice:
    def Input(self):
        pass
class Keyboard:
    def Input(self):
        print("User typing>")
class Mouse:
    def Input(self):
        print("mouse clicked.")

class Computer:
    def __init__(self,device: InputDevice):
        self.device = device
    def get_input(self):
        return self.device.Input()
        
type = Keyboard()
click = Mouse()

type.Input()
click.Input()

code = Computer(type)
#code = Computer(click)
code.get_input()
