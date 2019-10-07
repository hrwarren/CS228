import numpy as np
import pickle
import sys

sys.path.insert(0, '../..')
import knn
import gestureFilenames

knn = knn.KNN()

g = gestureFilenames.GESTURES()

#Importing all the testing and training sets. I feel like this is a very inelegant way to go about it, but here we are
# set_name = 'Genovese_train0'
# pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
# train0_a = pickle.load(pickle_in)
#
# set_name = 'Lee_train0'
# pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
# train0_b = pickle.load(pickle_in)
#
#
# set_name = 'Warren_train4'
# pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
# train4_a = pickle.load(pickle_in)
#
# set_name = 'Beatty_train4'
# pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
# train4_b = pickle.load(pickle_in)
#
#
# set_name = 'Warren_train5'
# pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
# train5_a = pickle.load(pickle_in)
#
# set_name = 'Deluca_train5'
# pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
# train5_b = pickle.load(pickle_in)
#
#
#
# # Loading in the testing sets
# set_name = 'Genovese_test0'
# pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
# test0_a = pickle.load(pickle_in)
#
# set_name = 'Lee_test0'
# pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
# test0_b = pickle.load(pickle_in)
#
#
# set_name = 'Warren_test4'
# pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
# test4_a = pickle.load(pickle_in)
#
# set_name = 'Beatty_test4'
# pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
# test4_b = pickle.load(pickle_in)
#
#
#
# set_name = 'Warren_test5'
# pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
# test5_a = pickle.load(pickle_in)
#
# set_name = 'Deluca_test5'
# pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
# test5_b = pickle.load(pickle_in)

trainnames = ['train0_a', 'train0_b', 'train4_a', 'train4_b', 'train5_a', 'train5_b']
testnames = ['test0_a', 'test0_b', 'test4_a', 'test4_b', 'test5_a', 'test5_b']

def ReshapeData(set0, set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19):
    X = np.zeros((20000, 5*2*3), dtype = 'f') #originally 5*2*3
    y = np.zeros((20000, 1), dtype = 'f')
    for row in range(0,1000):
        for d in range(0,10):
            if (d+1) < 20:
                y[row + (1000*d)] = d
                y[row + (1000*(d+1))] = d
        # y[row] = 0  # eventually, make a loop for these?
        # y[row+1000] = 0
        # y[row+2000] = 4
        # y[row+3000] = 4
        # y[row + 4000] = 5
        # y[row + 5000] = 5
        col = 0
        for finger in range(0,5): #originally j
            for bone in range(0,2): #originally k and 0:4 2
                for coord_ind in range(0,3): #3: #originally m and 0:6 3
                    X[row, col] = set0[finger, bone, coord_ind, row]
                    X[row + 1000,col] = set1[finger, bone, coord_ind, row]
                    X[row + 2000,col] = set2[finger, bone, coord_ind, row]
                    X[row + 3000, col] = set3[finger, bone, coord_ind, row]
                    X[row + 4000, col] = set4[finger, bone, coord_ind, row]
                    X[row + 5000, col] = set5[finger, bone, coord_ind, row]
                    X[row + 6000, col] = set6[finger, bone, coord_ind, row]
                    X[row + 7000, col] = set7[finger, bone, coord_ind, row]
                    X[row + 8000, col] = set8[finger, bone, coord_ind, row]
                    X[row + 9000, col] = set9[finger, bone, coord_ind, row]
                    X[row + 10000, col] = set10[finger, bone, coord_ind, row]
                    X[row + 11000, col] = set11[finger, bone, coord_ind, row]
                    X[row + 12000, col] = set12[finger, bone, coord_ind, row]
                    X[row + 13000, col] = set13[finger, bone, coord_ind, row]
                    X[row + 14000, col] = set14[finger, bone, coord_ind, row]
                    X[row + 15000, col] = set15[finger, bone, coord_ind, row]
                    X[row + 16000, col] = set16[finger, bone, coord_ind, row]
                    X[row + 17000, col] = set17[finger, bone, coord_ind, row]
                    X[row + 18000, col] = set18[finger, bone, coord_ind, row]
                    X[row + 19000, col] = set19[finger, bone, coord_ind, row]

                    col = col + 1

                    # for each X[row + (1000*d), col] =
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


# Cutting out unnecessary features
train0_a = ReduceData(g.train0_a)
train0_b = ReduceData(g.train0_b)
train1_a = ReduceData(g.train1_a)
train1_b = ReduceData(g.train1_b)
train2_a = ReduceData(g.train2_a)
train2_b = ReduceData(g.train2_b)
train3_a = ReduceData(g.train3_a)
train3_b = ReduceData(g.train3_b)
train4_a = ReduceData(g.train4_a)
train4_b = ReduceData(g.train4_b)
train5_a = ReduceData(g.train5_a)
train5_b = ReduceData(g.train5_b)
train6_a = ReduceData(g.train6_a)
train6_b = ReduceData(g.train6_b)
train7_a = ReduceData(g.train7_a)
train7_b = ReduceData(g.train7_b)
train8_a = ReduceData(g.train8_a)
train8_b = ReduceData(g.train8_b)
train9_a = ReduceData(g.train9_a)
train9_b = ReduceData(g.train9_b)

test0_a = ReduceData(g.test0_a)
test0_b = ReduceData(g.test0_b)
test1_a = ReduceData(g.test1_a)
test1_b = ReduceData(g.test1_b)
test2_a = ReduceData(g.test2_a)
test2_b = ReduceData(g.test2_b)
test3_a = ReduceData(g.test3_a)
test3_b = ReduceData(g.test3_b)
test4_a = ReduceData(g.test4_a)
test4_b = ReduceData(g.test4_b)
test5_a = ReduceData(g.test5_a)
test5_b = ReduceData(g.test5_b)
test6_a = ReduceData(g.test6_a)
test6_b = ReduceData(g.test6_b)
test7_a = ReduceData(g.test7_a)
test7_b = ReduceData(g.test7_b)
test8_a = ReduceData(g.test8_a)
test8_b = ReduceData(g.test8_b)
test9_a = ReduceData(g.test9_a)
test9_b = ReduceData(g.test9_b)


# Normalizing the data's coordinates
train0_a = CenterData(g.train0_a)
train0_b = CenterData(g.train0_b)
train1_a = CenterData(g.train1_a)
train1_b = CenterData(g.train1_b)
train2_a = CenterData(g.train2_a)
train2_b = CenterData(g.train2_b)
train3_a = CenterData(g.train3_a)
train3_b = CenterData(g.train3_b)
train4_a = CenterData(g.train4_a)
train4_b = CenterData(g.train4_b)
train5_a = CenterData(g.train5_a)
train5_b = CenterData(g.train5_b)
train6_a = CenterData(g.train6_a)
train6_b = CenterData(g.train6_b)
train7_a = CenterData(g.train7_a)
train7_b = CenterData(g.train7_b)
train8_a = CenterData(g.train8_a)
train8_b = CenterData(g.train8_b)
train9_a = CenterData(g.train9_a)
train9_b = CenterData(g.train9_b)

test0_a = CenterData(g.test0_a)
test0_b = CenterData(g.test0_b)
test1_a = CenterData(g.test1_a)
test1_b = CenterData(g.test1_b)
test2_a = CenterData(g.test2_a)
test2_b = CenterData(g.test2_b)
test3_a = CenterData(g.test3_a)
test3_b = CenterData(g.test3_b)
test4_a = CenterData(g.test4_a)
test4_b = CenterData(g.test4_b)
test5_a = CenterData(g.test5_a)
test5_b = CenterData(g.test5_b)
test6_a = CenterData(g.test6_a)
test6_b = CenterData(g.test6_b)
test7_a = CenterData(g.test7_a)
test7_b = CenterData(g.test7_b)
test8_a = CenterData(g.test8_a)
test8_b = CenterData(g.test8_b)
test9_a = CenterData(g.test9_a)
test9_b = CenterData(g.test9_b)


trainX, trainy = ReshapeData(train0_a, train0_b, train1_a, train1_b, train2_a, train2_b, train3_a, train3_b, train4_a, train4_b, train5_a, train5_b, train6_a, train6_b, train7_a, train7_b, train8_a, train8_b, train9_a, train9_b)
testX, testy = ReshapeData(test0_a, test0_b, test1_a, test1_b, test2_a, test2_b, test3_a, test3_b, test4_a, test4_b, test5_a, test5_b, test6_a, test6_b, test7_a, test7_b, test8_a, test8_b, test9_a, test9_b)

knn.Use_K_Of(15)
knn.Fit(trainX, trainy)
counter = 0

print(testX.shape)
print(testX[:,0])

for row in range(0,20000):
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

print(testX)
print(testy)
print(testX.shape, testy.shape)

# Saving the classifier
userDataDir = 'C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\classifier.p'
pickle_out = open(userDataDir, 'wb')
pickle.dump(knn, open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\classifier.p', 'wb'))
pickle_out.close()



