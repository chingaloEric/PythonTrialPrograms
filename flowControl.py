# while loop in python
count = 0
string = 'Eric'
while count < len(string):
    print(string[count]),
    count = count + 1
print('ended the loop')
    
# if statement
if len(string) < 3: 
    print(string + ' is a Weak name')
else:
    print(string + ' is a Strong name')

# for --- in loop
names = ['Mirabelle', 'Miguel', 'Lisa', 'Eric']
for name in names:
    print(name)

# range() fucntion
for i in range(len(names)):
    print(names[i])