class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print("Bork")

class Cat(Dog):
    def __init__(self, name, age, fur):
        # super() is the one that inherits all the attributes of the Dog class into the Cat class
        super().__init__(name, age)
        self.fur = fur

    def talk(self):
        print("mew")

garfield = Cat("garfield",3,"orange")
garfield.talk()