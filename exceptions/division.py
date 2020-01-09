'''

When an exception is not handled, a trace back is created

'''
# try-catch block
try:
    print(5/0)
# if exception error is not specified, python checks all exceptions
except ZeroDivisionError:
    print('Fool! You cant devide by zero')
