import pickle

start = 0

# The vector of dictionary keys:
digitsAttempted = ['digit0attempted',
                   'digit1attempted',
                   'digit2attempted',
                   'digit3attempted',
                   'digit4attempted',
                   'digit5attempted',
                   'digit6attempted',
                   'digit7attempted',
                   'digit8attempted',
                   'digit9attempted']

digitsSucceeded = ['digit0succeeded',
                   'digit1succeeded',
                   'digit2succeeded',
                   'digit3succeeded',
                   'digit4succeeded',
                   'digit5succeeded',
                   'digit6succeeded',
                   'digit7succeeded',
                   'digit8succeeded',
                   'digit9succeeded']


# The empty vector of times things have been drawn
times = []


# Getting username and info
database = pickle.load(open('userData/database.p','rb'))
username = raw_input('Please enter your name: ')
if username not in database:
    for i in range(0,10):
        database[username] = {'logins': 1,
                              digitsAttempted[0]: 0,
                              digitsSucceeded[0]: 3,

                              digitsAttempted[1]: 0,
                              digitsSucceeded[1]: 1,

                              digitsAttempted[2]: 0,
                              digitsSucceeded[2]: 1,

                              digitsAttempted[3]: 0,
                              digitsSucceeded[3]: 1,

                              digitsAttempted[4]: 0,
                              digitsSucceeded[4]: 0,

                              digitsAttempted[5]: 0,
                              digitsSucceeded[5]: 0,

                              digitsAttempted[6]: 0,
                              digitsSucceeded[6]: 0,

                              digitsAttempted[7]: 0,
                              digitsSucceeded[7]: 0,

                              digitsAttempted[8]: 0,
                              digitsSucceeded[8]: 0,

                              digitsAttempted[9]: 0,
                              digitsSucceeded[9]: 0,
                              }

    print('welcome ' + username + '.')
    print database[username]

else:
    database[username]['logins'] = database[username]['logins'] + 1

    print('welcome back ' + username + '. \n You have logged in {} times.'.format(database[username]['logins'] ))

pickle.dump(database,open('userData/database.p', 'wb'))

userRecord = database[username]

for i in range(0, 10):
    if userRecord[digitsSucceeded[i]] != 3:
        start = start + 1
    if start == 10:
        numToSign = 0
    elif start == 9:
        numToSign = 1
    elif start == 8:
        numToSign = 2
    elif start == 7:
        numToSign = 3
    elif start == 6:
        numToSign = 4
    elif start == 5:
        numToSign = 5
    elif start == 4:
        numToSign = 6
    elif start == 3:
        numToSign = 7
    elif start == 2:
        numToSign = 8
    elif start == 1:
        numToSign = 9

print numToSign

