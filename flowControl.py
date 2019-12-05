# while loop in python
count = 0
str = 'Eric'
while count < len(str):
    print(str[count]),
    count = count + 1
print('ended the loop')
    
# if statement
if len(str) < 3: 
    print(str + ' is a Weak name')
else:
    print(str + ' is a Strong name')

# for --- in loop
names = ['Mirabelle', 'Miguel', 'Lisa', 'Eric']
for name in names:
    print(name)

# range() fucntion
for i in range(len(names)):
    print(names[i])
