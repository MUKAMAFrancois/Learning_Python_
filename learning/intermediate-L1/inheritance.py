#parent class
class Animal(object):

    def eat(self):
        print("I can Eat")
    def reproduce(self):
        print("I reproduce")
    
    # child

class Human(Animal):
    
    def __init__(self,name,salary,occupation):
        self.name=name
        self.occupation=occupation
        self.salary=salary

    def introduce(self):
        print(f"I am {self.name},working as {self.occupation} getting ${self.salary}K")

class Lion(Animal):

    def eat(self):
        super().eat() # method from super class
        print("I am Lion, I like to eat meats")


    
#instance
person1=Human("Francois",450,"Data Scientist")
lion=Lion()


#accessing parent methods
person1.eat()
person1.reproduce()
person1.introduce()

print("\n")

lion.eat()
#If two methods exists in child class and superclass,
# the method in child overrides the one in superclass

# Howerver if we want to access method from super clas we use
#super


"""
There are 5 different types of inheritance in Python. They are as follows:

Single inheritance: When a child class inherits from only one parent class, 
it is called single inheritance. We saw an example above.
Multiple inheritances: When a child class inherits from multiple parent classes, 
Multilevel inheritance: When we have a child and grandchild relationship
Hierarchical inheritance More than one derived class can be created from a single base.
Hybrid inheritance: This form combines more than one form of inheritance. 
Basically, it is a blend of more than one type of inheritance.
"""
#Unlike Java, python shows multiple inheritances.

#2. Multiple Inheritance

class Mammal():
    def breast(self):
        print("I have Breasts")

class Movement():
    def move(self):
        print("I can move")

class Human(Mammal,Movement):
    pass

human1=Human()
human1.breast()
human1.move()

#3. Multilevel Inheritance

class Person:
    def live(self):
        print("I live in the world")

class Driver(Person):
    def occupation(self):
        print("I work for to live")

class Employee(Driver,Person):
    pass

emp1=Employee()
emp1.live()
emp1.occupation()