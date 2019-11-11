import threading
import time
import random

count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
points = 0

adZ = 0
suZ = 0
diZ = 0
muZ = 0

def chooseMathNum():
    global adZ
    global suZ
    global diZ
    global muZ



    c = random.randint(0, 9)
    d = random.randint(0, 9)

    op = random.randint(0, 3)

    if op == 0:
        mathNum = c + d

        while mathNum > 9:
            d = random.randint(0, 9)
            mathNum = c + d

        if mathNum == 0:
            adZ = adZ + 1

        # if mathNum > 9:
        #     d = random.randint(0,9)
        #     mathNum = c + d

    elif op == 1:
        mathNum = c - d
        while mathNum < 0:  # if??
            if c == 0:
                c = random.randint(0, 9)
            d = random.randint(0, 9)
            mathNum = c - d
        if mathNum == 0:
            suZ = suZ + 1

    elif op == 2:
        d = random.randint(1, 9)/1.0
        mathNum = c / d

        intVal = False
        while intVal == False:
            if mathNum%2 == 0 or (mathNum+1)%2 == 0:
                intVal = True
                mathNum = int(mathNum)
                d = int(d)
            else:
                d = random.randint(1,9)/1.0
                mathNum = c/d

        #
        # while isinstance(mathNum, int) == False:
        #     d = random.randint(1,9)
        #     mathNum = c/d

        # if c != 0:
        #     while c < d:
        #         d = random.randint(1, 9)
        # else:
        #     d = d

        # if c < d, change d until it's smaller than c
        # if c == 0, escape

        if mathNum == 0:
            diZ = diZ + 1

    elif op == 3:
        mathNum = c * d
        while mathNum > 9:
            d = random.randint(0, 9)
            mathNum = c * d
        if mathNum == 0:
            muZ = muZ + 1

    eqn = str(c) + ' {} '.format(opvec[op]) + str(d) + ' = ' + str(mathNum)

    # print 'c', c, ';', 'd', d, ';', op

    return mathNum, c, d, op, eqn

opvec = ['+', '-', '/', '*']

while True:
    mathNum, c, d, op, eqn = chooseMathNum()

    if mathNum == 0:
        limit0 = random.randint(0, 10)
        if limit0 > 2:
            while mathNum == 0:
                mathNum, c, d, op, eqn = chooseMathNum()

    elif mathNum == 1:
        limit1 = random.randint(0, 10)
        if limit1 > 2:
            while mathNum == 1:
                mathNum, c, d, op, eqn = chooseMathNum()

    print eqn




    if mathNum == 0:
        count0 = count0 + 1
    if mathNum == 1:
        count1 = count1 + 1
    if mathNum == 2:
        count2 = count2 + 1
    if mathNum == 3:
        count3 = count3 + 1
    if mathNum == 4:
        count4 = count4 + 1
    if mathNum == 5:
        count5 = count5 + 1
    if mathNum == 6:
        count6 = count6 + 1
    if mathNum == 7:
        count7 = count7 + 1
    if mathNum == 8:
        count8 = count8 + 1
    if mathNum == 9:
        count9 = count9 + 1

    # print mathNum


print 'done'

# import pickle
#
# start = 0
#
# # The vector of dictionary keys:
# digitsAttempted = ['digit0attempted',
#                    'digit1attempted',
#                    'digit2attempted',
#                    'digit3attempted',
#                    'digit4attempted',
#                    'digit5attempted',
#                    'digit6attempted',
#                    'digit7attempted',
#                    'digit8attempted',
#                    'digit9attempted']
#
# digitsSucceeded = ['digit0succeeded',
#                    'digit1succeeded',
#                    'digit2succeeded',
#                    'digit3succeeded',
#                    'digit4succeeded',
#                    'digit5succeeded',
#                    'digit6succeeded',
#                    'digit7succeeded',
#                    'digit8succeeded',
#                    'digit9succeeded']
#
#
# # The empty vector of times things have been drawn
# times = []
#
#
# # Getting username and info
# database = pickle.load(open('userData/database.p','rb'))
# username = raw_input('Please enter your name: ')
# if username not in database:
#     for i in range(0,10):
#         database[username] = {'logins': 1,
#                               digitsAttempted[0]: 0,
#                               digitsSucceeded[0]: 3,
#
#                               digitsAttempted[1]: 0,
#                               digitsSucceeded[1]: 1,
#
#                               digitsAttempted[2]: 0,
#                               digitsSucceeded[2]: 1,
#
#                               digitsAttempted[3]: 0,
#                               digitsSucceeded[3]: 1,
#
#                               digitsAttempted[4]: 0,
#                               digitsSucceeded[4]: 0,
#
#                               digitsAttempted[5]: 0,
#                               digitsSucceeded[5]: 0,
#
#                               digitsAttempted[6]: 0,
#                               digitsSucceeded[6]: 0,
#
#                               digitsAttempted[7]: 0,
#                               digitsSucceeded[7]: 0,
#
#                               digitsAttempted[8]: 0,
#                               digitsSucceeded[8]: 0,
#
#                               digitsAttempted[9]: 0,
#                               digitsSucceeded[9]: 0,
#                               }
#
#     print('welcome ' + username + '.')
#     print database[username]
#
# else:
#     database[username]['logins'] = database[username]['logins'] + 1
#
#     print('welcome back ' + username + '. \n You have logged in {} times.'.format(database[username]['logins'] ))
#
# pickle.dump(database,open('userData/database.p', 'wb'))
#
# userRecord = database[username]
#
# for i in range(0, 10):
#     if userRecord[digitsSucceeded[i]] != 3:
#         start = start + 1
#     if start == 10:
#         numToSign = 0
#     elif start == 9:
#         numToSign = 1
#     elif start == 8:
#         numToSign = 2
#     elif start == 7:
#         numToSign = 3
#     elif start == 6:
#         numToSign = 4
#     elif start == 5:
#         numToSign = 5
#     elif start == 4:
#         numToSign = 6
#     elif start == 3:
#         numToSign = 7
#     elif start == 2:
#         numToSign = 8
#     elif start == 1:
#         numToSign = 9
#
# print numToSign
#
