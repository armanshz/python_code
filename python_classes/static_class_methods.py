class Dog:
    # dogs is a class variable
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)
# This is a decorator. Decorator basically denotes if a method is a class or static method
# Class methods allow you to do things to the entire class itself without passing in the name of the object in the class itself.
# Class methods pass its own class.
# Return the number of objects in the Dog class by referencing the dogs list variable
    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)
# This is a decorator
# static methods are just functions within classes
    @staticmethod
    def bark(n):
        """ barks n times """
        for _ in range(n):
            print("Bark!")

tim, jim = Dog("Tim"), Dog("Jim")

print(Dog.num_dogs())
tim.bark(5)
jim.bark(5)