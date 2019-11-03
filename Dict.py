import pickle

def Reset():
    dictionary = {}
    pickle.dump(dictionary, open('userData/database.p', 'wb'))

database = pickle.load(open('userData/database.p','rb'))
#
# databse = {
#     username : {
#         logins : 0}
#     }
# }


for user in database:
    for digitsSucceeded in database[user]:
        print database[user][digitsSucceeded]
        if database[user][digitsSucceeded] != 0:
            database[user]['rank'] =


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