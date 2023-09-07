
# 1. Initialize

class Employee():
    
    #attributes
    def __init__(self,name,occupation,wage):
        self.name=name
        self.occupation=occupation
        self.wage=wage
    
    #methods

    def role(self):
        print(f" I am {self.name} My role: {self.occupation}")
    
    def salary(self):
        print(f"I earn ${self.wage}K")

# instance
emp1=Employee(name="John",occupation="ML engineer",wage=450)
#accessing methods
emp1.role()
emp1.salary() # Notice, never have method having same name with attribute


#2. Initialize (2)
# you can even do it as

class Parrot:
    # class attributes
    name=""
    age=1

#object 1
parrot1=Parrot()
parrot1.name="Joshuah"
parrot1.age=980

#access attributes
print(f"{parrot1.name} Parrot has {parrot1.age}")
