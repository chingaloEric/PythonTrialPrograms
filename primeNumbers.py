# for testNumber in range(2, 10):
#     for number in (2, testNumber):
#         if testNumber % number == 0:
#             print(testNumber, "is Not prime")
#             break
#     else:
#         print(testNumber, "is prime")

for testNumber in range(2, 10):
    for number in range(2, testNumber):
        if testNumber % number == 0:
            pass
            # print( testNumber, "is NOT prime" )
            # break
    else:
        print(testNumber, 'is prime')