class Person():
    # __init__() is the constructor method
    # the self parameter must be the first
    # self is the reference to the class
    def __init__(self, name, age, height = 0):
        self.name = name
        self.age = age
        self.height = height

    def say_hello(self):
        print('Hello. I am ' + self.name.title())
    
    def set_height(self, height):
        self.height = height

person_1 = Person('Eric', 22, 90)
person_1.say_hello()
print(person_1.name.title() + '\'s height is: ' + str(person_1.height) + ' feet')

# update height
person_1.set_height(100)
print(person_1.name.title() + '\'s new height is: ' + str(person_1.height) + ' feet')