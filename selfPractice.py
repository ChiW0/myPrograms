class Person(object):
    def description(self, name: str, age: int):
        self.name = name
        self.age = age

    
p = Person()
p.description("malychi", 20)

print(p.name)