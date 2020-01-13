import pickle
import operator


def Reset():
    dictionary = {}
    pickle.dump(dictionary, open('userData/database.p', 'wb'))


Reset()

database = pickle.load(open('userData/database.p','rb'))



#

#     username : {
#         logins : 0}
#     }
# }

totalSucceeded = 0

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
#
database['user1'] = {'logins': 10,

                      'digitsAttempted': {
                          digitsAttempted[0]: 0,
                          digitsAttempted[1]: 0,
                          digitsAttempted[2]: 0,
                          digitsAttempted[3]: 0,
                          digitsAttempted[4]: 0,
                          digitsAttempted[5]: 0,
                          digitsAttempted[6]: 0,
                          digitsAttempted[7]: 0,
                          digitsAttempted[8]: 0,
                          digitsAttempted[9]: 0,
                      },

                      'digitsSucceeded': {
                          digitsSucceeded[0]: 3,
                          digitsSucceeded[1]: 3,
                          digitsSucceeded[2]: 3,
                          digitsSucceeded[3]: 3,
                          digitsSucceeded[4]: 3,
                          digitsSucceeded[5]: 3,
                          digitsSucceeded[6]: 3,
                          digitsSucceeded[7]: 3,
                          digitsSucceeded[8]: 3,
                          digitsSucceeded[9]: 3,

                      },

                      'rank': 30,

                      'runScore': {
                          'previous': 0,
                          'highest': 10
                      },

                      'mathScore': {
                          'total': 10,
                          '+': 0,
                          '-': 0,
                          '/': 0,
                          '*': 0
                      }

                }

database['user2'] = {'logins': 1,

                      'digitsAttempted': {
                          digitsAttempted[0]: 0,
                          digitsAttempted[1]: 0,
                          digitsAttempted[2]: 0,
                          digitsAttempted[3]: 0,
                          digitsAttempted[4]: 0,
                          digitsAttempted[5]: 0,
                          digitsAttempted[6]: 0,
                          digitsAttempted[7]: 0,
                          digitsAttempted[8]: 0,
                          digitsAttempted[9]: 0,
                      },

                      'digitsSucceeded': {
                          digitsSucceeded[0]: 3,
                          digitsSucceeded[1]: 3,
                          digitsSucceeded[2]: 3,
                          digitsSucceeded[3]: 3,
                          digitsSucceeded[4]: 0,
                          digitsSucceeded[5]: 0,
                          digitsSucceeded[6]: 0,
                          digitsSucceeded[7]: 0,
                          digitsSucceeded[8]: 0,
                          digitsSucceeded[9]: 0,

                      },

                      'rank': 12,

                      'runScore': {
                          'previous': 0,
                          'highest': 0
                      },

                      'mathScore': {
                          'total': 0,
                          '+': 0,
                          '-': 0,
                          '/': 0,
                          '*': 0
                      }

                      }



# database['user3'] = {'logins': 1,
#
#                       'digitsAttempted': {
#                           digitsAttempted[0]: 0,
#                           digitsAttempted[1]: 0,
#                           digitsAttempted[2]: 0,
#                           digitsAttempted[3]: 0,
#                           digitsAttempted[4]: 0,
#                           digitsAttempted[5]: 0,
#                           digitsAttempted[6]: 0,
#                           digitsAttempted[7]: 0,
#                           digitsAttempted[8]: 0,
#                           digitsAttempted[9]: 0,
#                       },
#
#                       'digitsSucceeded': {
#                           digitsSucceeded[0]: 0,
#                           digitsSucceeded[1]: 0,
#                           digitsSucceeded[2]: 0,
#                           digitsSucceeded[3]: 0,
#                           digitsSucceeded[4]: 0,
#                           digitsSucceeded[5]: 0,
#                           digitsSucceeded[6]: 0,
#                           digitsSucceeded[7]: 3,
#                           digitsSucceeded[8]: 3,
#                           digitsSucceeded[9]: 3,
#
#                       },
#
#                       'rank': 30,
#
#                       'runScore': {
#                           'previous': 0,
#                           'highest': 0
#                       },
#
#                       'mathScore': {
#                           'total': 0,
#                           '+': 0,
#                           '-': 0,
#                           '/': 0,
#                           '*': 0
#                       }
#
#                       }

# dictionary = {'logins': 1,
#               'Attempted': {
#                   'digit0': 0,
#                   'digit1': 0,
#                   'digit2': 0
#                },
#               'Succeeded': {
#                   'digit0': 0,
#                   'digit1': 0,
#                   'digit2': 0
#               }
#               }
#
# for digit in dictionary['Attempted']:
#     print dictionary['Attempted'][digit]


# rankings = {}
#
# for user in database:
#     for digit in database[user]['digitsSucceeded']:
#         if database[user]['digitsSucceeded'][digit] != 0:
#             totalSucceeded = totalSucceeded + 1
#     database[user]['rank'] = database[user].get('rank') + totalSucceeded
#     rank = database[user]['rank']
#     rankings[user] = rank
#     totalSucceeded = 0
#     print user, database[user]['rank']
#
# res = sorted(rankings.items(), key = operator.itemgetter(1), reverse=True)
#
# for i in range (0,2):
#     print res[i][0]
#
# winner = max(rankings.values())
# winnerkey = [k for k, v in rankings.items() if v == winner]
#
#
#
# print(winner, str(winnerkey[0]))
#
#


# #############
Reset()
# #############
print database
pickle.dump(database,open('userData/database.p', 'wb'))
#
# blah = ['0', '2', '3']
#
# username = raw_input('Please enter your name: ')
# if username not in database:
#     database[username] = {'logins': 1}
#     print('welcome ' + username + '.')
#
# else:
#     database[username]['logins'] = database[username].get('logins') + 1
#
#     # database[username] = {'logins': database[username].get('logins') + 1}
#     print('welcome back ' + username + '.')
#
# print(database)
#
# print database[username].get('logins')
#
