class Person:
    def set_name(obj, name, age):
        obj.name = name
        obj.age = age
    
    def get_name(obj):
        return obj.name
    
    def get_age(obj):
        return obj.age

p = Person()
p.set_name(input("what is your name: "), input("how old are you: "))

print(p.get_name())

print(p.get_age())