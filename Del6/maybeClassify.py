import numpy as np
import pickle
import sys
import time

sys.path.insert(0, '../..')
import knn
import gestureFilenames

knn = knn.KNN()

g = gestureFilenames.GESTURES()

def ReshapeData(set0,set1,set2,set3,set4,set5,set6,set7,set8,set9):
    X = np.zeros((10000, 5*2*3), dtype = 'f') # normally 10000
    y = np.zeros((10000, 1), dtype = 'f')
    for row in range(0,1000):
        y[row, 0] = 0
        y[(row + 1000), 0] = 1
        y[(row + 2000), 0] = 2
        y[(row + 3000), 0] = 3
        y[(row + 4000), 0] = 4
        y[(row + 5000), 0] = 5
        y[(row + 6000), 0] = 6
        y[(row + 7000), 0] = 7
        y[(row + 8000), 0] = 8
        y[(row + 9000), 0] = 9



        # for d in range(0,10): # normally 0:10
        #     y[(row + (d * 1000)), 0] = d

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

                    col = col + 1

                    # for each X[row + (1000*d), col] =
    return X, y

# originally shaped 5,4,6,2000

def ReduceData(X):
    X = np.delete(X,1,1)
    X = np.delete(X,1,1)
    X = np.delete(X,0,2)
    X = np.delete(X,0,2)
    X = np.delete(X,0,2)
    return X

def CenterData(X):
    allXCoords = X[:,:,0,:]
    meanValue = allXCoords.mean()
    X[:,:,0,:] = allXCoords - meanValue

    allXCoords = X[:,:,1,:]
    meanValue = allXCoords.mean()
    X[:,:,1,:] = allXCoords - meanValue

    allXCoords = X[:,:,2,:]
    meanValue = allXCoords.mean()
    X[:,:,2,:] = allXCoords - meanValue

    # for s in range(0,3):
    #     allXCoords = X[:,:,s,:]
    #     meanValue = allXCoords.mean()
    #     X[:,:,s,:] = allXCoords - meanValue

    return X


# Cutting out unnecessary features
train0_a = ReduceData(g.train0_a)
train1_a = ReduceData(g.train1_a)
train2_a = ReduceData(g.train2_a)
train3_a = ReduceData(g.train3_a)
train4_a = ReduceData(g.train4_a)
train5_a = ReduceData(g.train5_a)
train6_a = ReduceData(g.train6_a)
train7_a = ReduceData(g.train7_a)
train8_a = ReduceData(g.train8_a)
train9_a = ReduceData(g.train9_a)


test0_a = ReduceData(g.test0_a)
test1_a = ReduceData(g.test1_a)
test2_a = ReduceData(g.test2_a)
test3_a = ReduceData(g.test3_a)
test4_a = ReduceData(g.test4_a)
test5_a = ReduceData(g.test5_a)
test6_a = ReduceData(g.test6_a)
test7_a = ReduceData(g.test7_a)
test8_a = ReduceData(g.test8_a)
test9_a = ReduceData(g.test9_a)


# Normalizing the data's coordinates
train0_a = CenterData(g.train0_a)
train1_a = CenterData(g.train1_a)
train2_a = CenterData(g.train2_a)
train3_a = CenterData(g.train3_a)
train4_a = CenterData(g.train4_a)
train5_a = CenterData(g.train5_a)
train6_a = CenterData(g.train6_a)
train7_a = CenterData(g.train7_a)
train8_a = CenterData(g.train8_a)
train9_a = CenterData(g.train9_a)

test0_a = CenterData(g.test0_a)
test1_a = CenterData(g.test1_a)
test2_a = CenterData(g.test2_a)
test3_a = CenterData(g.test3_a)
test4_a = CenterData(g.test4_a)
test5_a = CenterData(g.test5_a)
test6_a = CenterData(g.test6_a)
test7_a = CenterData(g.test7_a)
test8_a = CenterData(g.test8_a)
test9_a = CenterData(g.test9_a)


# these are currently missing all trainX_c
trainX, trainy = ReshapeData(train0_a, train1_a, train2_a, train3_a, train4_a, train5_a, train6_a, train7_a, train8_a, train9_a)
testX, testy = ReshapeData(test0_a, test1_a, test2_a, train3_a, test4_a, test5_a, test6_a, test7_a, test8_a, test9_a)




# for when each digit has 3 sets
# trainX, trainy = ReshapeData(train0_a, train0_b, train0_c, train1_a, train1_b, train1_c, train2_a, train2_b, train2_c, train3_a, train3_b, train3_c, train4_a, train4_b, train4_c, train5_a, train5_b, train5_c, train6_a, train6_b, train6_c, train7_a, train7_b, train7_c, train8_a, train8_b, train8_c, train9_a, train9_b, train9_c)
# testX, testy = ReshapeData(test0_a, test0_b, test0_c, test1_a, test1_b, test1_c, test2_a, test2_b, test2_c, test3_a, test3_b, test3_c, test4_a, test4_b, test4_c, test5_a, test5_b, test5_c, test6_a, test6_b, test6_c, test7_a, test7_b, test7_c, test8_a, test8_b, test8_c, test9_a, test9_b, test9_c)

knn.Use_K_Of(15) # originally 15
knn.Fit(trainX, trainy)
counter = 0

print(testX)
print(testy)
print(testX.shape, testy.shape)

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


for row in range(0,10000): # normally 0:20000
    itemClass = int(testy[row])
    prediction = int(knn.Predict(testX[row,:]))
    actualClass = testy[row]
    print(prediction, itemClass)
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

print(testX)
print(testy)
print(testX.shape, testy.shape)

# Saving the classifier
userDataDir = 'C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\classifier.p'
pickle_out = open(userDataDir, 'wb')
pickle.dump(knn, open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\classifier.p', 'wb'))
pickle_out.close()


#Did not like 3, 6, or 7



