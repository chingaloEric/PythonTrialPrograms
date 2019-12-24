prompt = 'I am a number between 7 and 20 that is a multiple of 7.'
prompt += '\nGuess who i am: '
number = input(prompt)

number = int(number)
if number % 7 == 0: 
    if number > 7 and number <= 20: 
        print('You got me')
    else:
        print('Dummy! You are out of range')
else:
    print('You lost')