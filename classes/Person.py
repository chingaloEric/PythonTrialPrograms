class Person():
    # __init__() is the constructor method
    # the self parameter must be the first
    # self is the reference to the class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print('Hello. I am ' + self.name.title())

person_1 = Person('Eric', 22)
person_1.say_hello()