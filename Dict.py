import pickle

def Reset():
    dictionary = {}
    pickle.dump(dictionary, open('userData/database.p', 'wb'))

database = pickle.load(open('userData/database.p','rb'))
logins = {}

username = raw_input('Please enter your name: ')
if username in database:
    database[username] = 
    print('welcome back ' + username + '.')

else:
    database[username] = {logins}
    print('welcome ' + username + '.')



print(database)

pickle.dump(database,open('userData/database.p', 'wb'))