'''

When an exception is not handled, a trace back is created

'''
# try-catch block
try:
    print(5/1)
# if exception error is not specified, python checks all exceptions
except ZeroDivisionError:
    print('Fool! You cant devide by zero')
# else block works when there is no exception on the try block
else: 
    print('Well done!')