##Animal is-a object 
class Animal(object):
	def shout(self):
		print "Animal Shout"

## Dog is-a animal
class Dog(Animal):
	def __init__(self, name):
		## Dog has-a name
		self.name = name
	def shout(self):
		print "Dog shout"

##Cat is-a animal
class Cat(Animal):
	def __init__(self, name):
		##cat has-a name
		self.name = name

## Person is a object
class Person(object):
	def __init__(self, name):
		##
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is a Person
class Employee(Person):
	def __init__(self, name, salary):
		##super
		super(Employee, self).__init__(name)
		##
		self.salary = salary

## fish is-a object
class Fish(object):
	pass

## Salmon is-a fish
class Salmon(Fish):
	pass

## Halibut Is-A Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## Mary's pet is satan
mary.pet = satan

## frank is an employee
frank = Employee("Frank", 120000)

##franks pet is rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()


animal = Animal()
animal.shout()
dog = Dog(animal)
dog.shout()









