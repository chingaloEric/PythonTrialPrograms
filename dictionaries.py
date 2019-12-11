# dictionaries in python are collections of key value pairs.
student1 = {'name': 'Eric', 'gender': 'M', 'age': 21}
student2 = {'name': 'Lisa', 'gender': 'F', 'age': 22}
students = [student1, student2]

# deleting a key-value
del student2['age']

def add_blood_group(student):
    if student['name'].lower() == 'eric':
        updated_student = {**student, 'blood_group': 'A+'}
    elif student['name'].lower() == 'lisa':
        updated_student = {**student, 'blood_group': 'B+'}
    else:
        updated_student = student
    return updated_student

count = 0
for student in students:
    students[count] = add_blood_group(student)
    # to remove a key-value pair
    # del students[count]['blood_group']
    count =+ 1
print(students)


# looping a dictionary
fav_languages = {
    'eric': 'js',
    'lisa': 'java',
    'miguel': 'python'
}
# on looping, python doesnt care about the order
for key, value in fav_languages.items():
    print(key.title() + ' codes in ' + value.upper())

# looping keys of dictionary:
parents = ['eric', 'lisa']
for name in fav_languages.keys():
    if name in parents:
        print('Hello ' + name.title() + ', its awesome that you code in ' + fav_languages[name].upper())

# looping through values of dictionary
for language in fav_languages.values():
    print(language.title())

# list in a dictionary:
pizza = {
    'name': 'local',
    'size': 'small',
    'toppings': ['extra cheese', 'papperoni']
}

print(pizza['size'].title() + ' ' + pizza['name'] + ' pizza has the following toppings:')
for topping in pizza['toppings']:
    print('\t' + topping)

# dictionary in a dictionary:
users = {
    'chingaloEric': {
        'firstname': 'eric',
        'lastname': 'chingalo'
    },
    'tibs': {
        'firstname': 'lisa',
        'lastname': 'tibenda'
    }
}

for user_name, user_info in users.items():
    full_name = user_info['firstname'] + ' ' + user_info['lastname']
    print('Hola! ' + user_name.title())
    print('Welcome ' + full_name.title()) 
    