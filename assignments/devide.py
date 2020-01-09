'''
A simple dividing application with exception handling
'''

print('Enter two numbers to dividend and divisor')
print('Once done, type q')

while True:
    first_number = input('Enter dividend: ')
    if first_number == 'q':
        break

    second_number = input('Enter divisor: ')
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    
    except ZeroDivisionError:
        print('Can\'t divide by zero')
    else:
        print(first_number + '/' + second_number + ' = ' + str(answer))