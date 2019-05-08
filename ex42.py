## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

    def noise(self):
        print "WOOF"

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name
    
    def noise2(self):
        print "WOOF"

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

        ## Person has-a intro function
    def intro(self):
        print self.name

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## sata nis-a Cat
satan = Cat("satan")

## mary is a Person
mary = Person("Mary")

## mary has-a pet which is satan
mary.pet = satan 

## Frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet which is rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()