#First, you need to learn two catch phrases "is-a" and "has-a." You use the phrase is-a when you talk about objects and classes being related to each other by a class relationship. You use has-a when you talk about objects and classes that are related only because they reference each other.

#Animal is-a object
class Animal(object):
    pass
    #pass is used when a statement is required syntactically but you don't want any code or command to execute it. it is a null operation, also usefull when you want to put in code later

#Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        #Dog has-a name
        self.name = name

#Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        #Cat has-a name
        self.name = name

#Person is-a object
class Person(object):
    def __init__(self, name):
        #person has-a name
        self.name = name
        #person has a pet of some kind
        self.pet = None

class Employee(Person):

    def __init__(self, name, salary):
        #super() lets you avoid referring to the base class excplicitly and can be used with multiple inheritance
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

#rover is-a Dog
rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

#Mary has-a pet named satan
may.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish

crouse = Salmon()

harry = Halibut()
