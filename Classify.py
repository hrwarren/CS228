import numpy as np
import pickle
import knn

knn = knn.KNN()

# 0 works!

#Importing all the testing and training sets. I feel like this is a very inelegant way to go about it, but here we are
set_name = 'Genovese_train0'
pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\UserData\{}.p'.format(set_name), 'rb')
train0_a = pickle.load(pickle_in)
set_name = 'Genovese_test0'
pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\UserData\{}.p'.format(set_name), 'rb')
test0_a = pickle.load(pickle_in)

set_name = 'Soccorsi_train0'
pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\UserData\{}.p'.format(set_name), 'rb')
train0_b = pickle.load(pickle_in)
set_name = 'Soccorsi_test0'
pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\UserData\{}.p'.format(set_name), 'rb')
test0_b = pickle.load(pickle_in)

set_name = 'Warren_train0'
pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\UserData\{}.p'.format(set_name), 'rb')
train0_c = pickle.load(pickle_in)
set_name = 'Warren_test0'
pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\UserData\{}.p'.format(set_name), 'rb')
test0_c = pickle.load(pickle_in)




set_name = 'Liu_train2'
pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\UserData\{}.p'.format(set_name), 'rb')
train1 = pickle.load(pickle_in)
set_name = 'Liu_test2'
pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\UserData\{}.p'.format(set_name), 'rb')
test1 = pickle.load(pickle_in)

set_name = 'Deso_train5'
pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\UserData\{}.p'.format(set_name), 'rb')
train5_a = pickle.load(pickle_in)
set_name = 'Deso_test5'
pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\UserData\{}.p'.format(set_name), 'rb')
test5_a = pickle.load(pickle_in)

set_name = 'Livingston_train5'
pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\UserData\{}.p'.format(set_name), 'rb')
train5_b = pickle.load(pickle_in)
set_name = 'Livingston_test5'
pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\UserData\{}.p'.format(set_name), 'rb')
test5_b = pickle.load(pickle_in)


# to flip
# invert everyone's raw X coords
# copy data to two files with the same "target number"


def ReshapeData(set0,set1,set2,set3,set4,set5):
    X = np.zeros((5000, 5*2*3), dtype = 'f') #originally 5*2*3
    y = np.zeros((5000, 1), dtype = 'f')
    for row in range(0,1000):
        y[row] = 0
        y[row+1000] = 0
        y[row+2000] = 0
        y[row+3000] = 1
        y[row+4000] = 5
        y[row + 5000] = 5

        col = 0
        for finger in range(0,5): #originally j
            for bone in range(0,2): #originally k and 0:4 2
                for coord_ind in range(0,3): #3: #originally m and 0:6 3
                    X[row, col] = set0[finger, bone, coord_ind, row]
                    X[row + 1000,col] = set1[finger, bone, coord_ind, row]
                    X[row + 2000, col] = set2[finger, bone, coord_ind, row]
                    X[row + 3000, col] = set3[finger, bone, coord_ind, row]
                    X[row + 4000, col] = set4[finger, bone, coord_ind, row]
                    X[row + 5000, col] = set5[finger, bone, coord_ind, row]
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
    print(X)

    allXCoordinates = X[:, :, 0, :]
    meanXValue = allXCoordinates.mean()
    X[:, :, 0, :] = allXCoordinates - meanXValue

    allYCoordinates = X[:, :, 1, :]
    meanYValue = allYCoordinates.mean()
    X[:, :, 1, :] = allYCoordinates - meanYValue

    allZCoordinates = X[:, :, 2, :]
    meanZValue = allZCoordinates.mean()
    X[:, :, 2, :] = allZCoordinates - meanZValue

    # for s in range(0,3):
    #     allXCoords = X[:,:,s,:]
    #     meanValue = allXCoords.mean()
    #     X[:,:,s,:] = allXCoords - meanValue
    print(X)
    return X

# Removing irrelevant coordinates
train0_a = ReduceData(train0_a)
test0_a = ReduceData(test0_a)
train0_b = ReduceData(train0_b)
test0_b = ReduceData(test0_b)
train0_c = ReduceData(train0_c)
test0_c = ReduceData(train0_c)

train1 = ReduceData(train1)
test1 = ReduceData(test1)

train5_a = ReduceData(train5_a)
test5_a = ReduceData(test5_a)
train5_b = ReduceData(train5_b)
test5_b = ReduceData(test5_b)

# Centering remaining coordinates
train0_a = CenterData(train0_a)
test0_a = CenterData(test0_a)
train0_b = CenterData(train0_b)
test0_b = CenterData(test0_b)
train0_c = CenterData(train0_c)
test0_c = CenterData(train0_c)

train1 = CenterData(train1)
test1 = CenterData(test1)

train5_a = CenterData(train5_a)
test5_a = CenterData(test5_a)
train5_b = CenterData(train5_b)
test5_b = CenterData(test5_b)





trainX, trainy = ReshapeData(train0_a, train0_b, train0_c, train1, train5_a, train5_b)
testX, testy = ReshapeData(test0_a, test0_b, test0_c, test1, test5_a, test5_b)

knn.Use_K_Of(15)
knn.Fit(trainX, trainy)
counter = 0

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

for row in range(0,6000):
    itemClass = int(testy[row])
    # This works when using the old knn, but fails with Sida's code:
    prediction = int(knn.Predict(testX[row,:]))
    actualClass = testy[row]
    if actualClass == prediction:
        counter += 1
        if actualClass == 0:
            count0 = count0 + 1
        if actualClass == 1:
            count1 = count1 + 1
        if actualClass == 2:
            count2 = count2 + 1
        if actualClass == 3:
            count3 = count3 + 1
        if actualClass == 4:
            count4 = count4 + 1
        if actualClass == 5:
            count5 = count5 + 1
        if actualClass == 6:
            count6 = count6 + 1
        if actualClass == 7:
            count7 = count7 + 1
        if actualClass == 8:
            count8 = count8 + 1
        if actualClass == 9:
            count9 = count9 + 1

counter = float(counter)
accuracy = (counter / len(testy))*100
print(accuracy)
# I got 71.9% initially, 95.7% with data reduction, 100% with centering

# print(testX)
# print  (testy)
# print(testX.shape, testy.shape)

userDataDir = 'C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\Oldclassifier.p'
pickle_out = open(userDataDir, 'wb')
pickle.dump(knn, open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\Oldclassifier.p', 'wb'))
pickle_out.close()




