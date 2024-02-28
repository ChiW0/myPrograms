class myClass:
    def __init__(self, name, cat):
        self.name = name
        self.cat = cat
    
    def greet(self):
        print(f"Hello {self.name} and {self.cat}, and welcome to paradise.")
    

myObject = myClass(input("what's your name?: "), input("what's your cat's name?: "))

myObject.greet()