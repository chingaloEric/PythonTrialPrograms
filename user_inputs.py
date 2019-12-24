# simple user input
name = input('Enter your name: ')
print('Hola! '+ name.title())

# handle int
age = input('Enter your age: ')
# python takes all user inputs as string
age = int(age)
if age >= 18:
    print('Welcome to vote')
else:
    print('Oups ' + name.title() + '! You\'re too young')