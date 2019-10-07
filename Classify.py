import numpy as np
import pickle
import knn

knn = knn.KNN()

#Importing all the testing and training sets. I feel like this is a very inelegant way to go about it, but here we are
set_name = 'train4'
pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\userData\{}.dat'.format(set_name), 'rb')
train4 = pickle.load(pickle_in)

set_name = 'train5'
pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\userData\{}.dat'.format(set_name), 'rb')
train5 = pickle.load(pickle_in)

set_name = 'test4'
pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\userData\{}.dat'.format(set_name), 'rb')
test4 = pickle.load(pickle_in)

set_name = 'test5'
pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\userData\{}.dat'.format(set_name), 'rb')
test5 = pickle.load(pickle_in)

def ReshapeData(set1,set2):
    X = np.zeros((2000, 5*2*3), dtype = 'f') #originally 5*2*3
    y = np.zeros((2000, 1), dtype = 'f')
    for row in range(0,1000):
        y[row] = 4
        y[row+1000] = 5
        col = 0
        for finger in range(0,5): #originally j
            for bone in range(0,2): #originally k and 0:4 2
                for coord_ind in range(0,3): #3: #originally m and 0:6 3
                    X[row, col] = set1[finger, bone, coord_ind, row]
                    X[row+1000,col] = set2[finger, bone, coord_ind, row]
                    col = col + 1
                    #Some entries are identical in groups of five???
    return X, y

#originally shaped 5,4,6,2000

def ReduceData(X):
    X = np.delete(X,1,1)
    X = np.delete(X,1,1)
    X = np.delete(X,0,2)
    X = np.delete(X,0,2)
    X = np.delete(X,0,2)
    return X

def CenterData(X):
    for s in range(0,3):
        allXCoords = X[:,:,s,:]
        meanValue = allXCoords.mean()
        X[:,:,s,:] = allXCoords - meanValue
    return X

train4 = ReduceData(train4)
train5 = ReduceData(train5)
test4 = ReduceData(test4)
test5 = ReduceData(test5)

train4 = CenterData(train4)
train5 = CenterData(train5)
test4 = CenterData(test4)
test5 = CenterData(test5)


trainX, trainy = ReshapeData(train4,train5)
testX, testy = ReshapeData(test4,test5)

knn.Use_K_Of(15)
knn.Fit(trainX, trainy)
counter = 0

print(testX.shape)
print(testX[:,0])

for row in range(0,2000):
    itemClass = int(testy[row])
    # This works when using the old knn, but fails with Sida's code:
    prediction = int(knn.Predict(testX[row,:]))
    actualClass = testy[row]
    if actualClass == prediction:
        counter += 1

counter = float(counter)
accuracy = (counter / len(testy))*100
print(accuracy)
# I got 71.9% initially, 95.7% with data reduction, 100% with centering

# print(testX)
# print  (testy)
# print(testX.shape, testy.shape)




