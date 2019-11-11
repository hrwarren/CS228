import pickle
import operator


def Reset():
    dictionary = {}
    pickle.dump(dictionary, open('userData/database.p', 'wb'))

database = pickle.load(open('userData/database.p','rb'))
#

#     username : {
#         logins : 0}
#     }
# }

totalSucceeded = 0

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


#############
Reset()
#############
print database

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
# pickle.dump(database,open('userData/database.p', 'wb'))