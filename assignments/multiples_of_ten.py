prompt = 'I am a number that is a multiple of 10.'
prompt += '\nGuess who i am: '
number = input(prompt)

number = int(number)
if number % 10 == 0 : 
    print('Luck you that ' + str(number) + ' is a multiple of 10')
else:
    print('You lost')