class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say_hello(self):
        print(f"Hello, my name is {self.name} and my age is {self.age}")
# creating my object
person1=Person("kae",10)
person1.say_hello()
person2=Person("vicky",13)
person2.say_hello()
person3=Person("Kel",12)
person3.say_hello()
# create a class called cars with the following attributes/properties
# make,model,year then create a function that prints,make ,mode and year
# then create three objects
class Cars:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def say_car(self):
        print(f"my cars make is {self.make} and the model is {self.model} which was developed in  {self.year}")
magari=Cars("Toyota","wish",2020)
magari.say_car()
class Fruits:
