import numpy as np
import pickle
import sys

sys.path.insert(0, '../..')
import knn
import gestureFilenames

knn = knn.KNN()

g = gestureFilenames.GESTURES()

def ReshapeData(set0, set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19):
                #set20, set21, set22, set23, set24, set25, set26, set27, set28, set29):
    X = np.zeros((20000, 5*2*3), dtype = 'f') # normally 20000
    y = np.zeros((20000, 1), dtype = 'f')
    for row in range(0,1000):
        # for d in range(0,10): # normally 0:10
        #     if (d+1) < 28: # normally < 20
                #y[(row + (1000*d)),0] = d

        # this is about to be disgusting
        # I'll come up with a loop for this when I have more sleep
        # may God have mercy on my soul


        # Assembling the trainy/testy for three sets per digit
        # y[row,          0] = 0
        # y[(row + 1000), 0] = 0
        # y[(row + 2000), 0] = 0
        # y[(row + 3000), 0] = 1
        # y[(row + 4000), 0] = 1
        # y[(row + 5000), 0] = 1
        # y[(row + 6000), 0] = 2
        # y[(row + 7000), 0] = 2
        # y[(row + 8000), 0] = 2
        # y[(row + 9000), 0] = 3
        # y[(row + 10000), 0] = 3
        # y[(row + 11000), 0] = 3
        # y[(row + 12000), 0] = 4
        # y[(row + 13000), 0] = 4
        # y[(row + 14000), 0] = 4
        # y[(row + 15000), 0] = 5
        # y[(row + 16000), 0] = 5
        # y[(row + 17000), 0] = 5
        # y[(row + 18000), 0] = 6
        # y[(row + 19000), 0] = 6
        # y[(row + 20000), 0] = 6
        # y[(row + 21000), 0] = 7
        # y[(row + 22000), 0] = 7
        # y[(row + 23000), 0] = 7
        # y[(row + 24000), 0] = 8
        # y[(row + 25000), 0] = 8
        # y[(row + 26000), 0] = 8
        # y[(row + 27000), 0] = 9
        # y[(row + 28000), 0] = 9
        # y[(row + 29000), 0] = 9

        # Assembling the trainy/testy for 2 sets per digit
        y[row,          0] = 0
        y[(row + 1000), 0] = 0
        y[(row + 2000), 0] = 1
        y[(row + 3000), 0] = 1
        y[(row + 4000), 0] = 2
        y[(row + 5000), 0] = 2
        y[(row + 6000), 0] = 3
        y[(row + 7000), 0] = 3
        y[(row + 8000), 0] = 4
        y[(row + 9000), 0] = 4
        y[(row + 10000), 0] = 5
        y[(row + 11000), 0] = 5
        y[(row + 12000), 0] = 6
        y[(row + 13000), 0] = 6
        y[(row + 14000), 0] = 7
        y[(row + 15000), 0] = 7
        y[(row + 16000), 0] = 8
        y[(row + 17000), 0] = 8
        y[(row + 18000), 0] = 9
        y[(row + 19000), 0] = 9


        # y[(row + (1000*(d+1))),0] = d
        # print(d, max(y),y)

        col = 0
        for finger in range(0,5): #originally j
            for bone in range(0,2): #originally k and 0:4 2
                for coord_ind in range(0,3): #3: #originally m and 0:6 3
                    # X[row, col] = set0[finger, bone, coord_ind, row]
                    # X[row + 1000,col] = set1[finger, bone, coord_ind, row]
                    # X[row + 2000,col] = set2[finger, bone, coord_ind, row]
                    # X[row + 3000, col] = set3[finger, bone, coord_ind, row]
                    # X[row + 4000, col] = set4[finger, bone, coord_ind, row]
                    # X[row + 5000, col] = set5[finger, bone, coord_ind, row]
                    # X[row + 6000, col] = set6[finger, bone, coord_ind, row]
                    # X[row + 7000, col] = set7[finger, bone, coord_ind, row]
                    # X[row + 8000, col] = set8[finger, bone, coord_ind, row]
                    # X[row + 9000, col] = set9[finger, bone, coord_ind, row]
                    # X[row + 10000, col] = set10[finger, bone, coord_ind, row]
                    # X[row + 11000, col] = set11[finger, bone, coord_ind, row]
                    # X[row + 12000, col] = set12[finger, bone, coord_ind, row]
                    # X[row + 13000, col] = set13[finger, bone, coord_ind, row]
                    # X[row + 14000, col] = set14[finger, bone, coord_ind, row]
                    # X[row + 15000, col] = set15[finger, bone, coord_ind, row]
                    # X[row + 16000, col] = set16[finger, bone, coord_ind, row]
                    # X[row + 17000, col] = set17[finger, bone, coord_ind, row]
                    # X[row + 18000, col] = set18[finger, bone, coord_ind, row]
                    # X[row + 19000, col] = set19[finger, bone, coord_ind, row]
                    # X[row + 20000, col] = set20[finger, bone, coord_ind, row]
                    # X[row + 21000, col] = set21[finger, bone, coord_ind, row]
                    # X[row + 22000, col] = set22[finger, bone, coord_ind, row]
                    # X[row + 23000, col] = set23[finger, bone, coord_ind, row]
                    # X[row + 24000, col] = set24[finger, bone, coord_ind, row]
                    # X[row + 25000, col] = set25[finger, bone, coord_ind, row]
                    # X[row + 26000, col] = set26[finger, bone, coord_ind, row]
                    # X[row + 27000, col] = set27[finger, bone, coord_ind, row]
                    # X[row + 28000, col] = set28[finger, bone, coord_ind, row]
                    # X[row + 29000, col] = set29[finger, bone, coord_ind, row]
                    #

                    # For when there's only 2 sets per digit
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

# originally shaped 5,4,6,2000

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
train1_a = ReduceData(g.train1_a)
train2_a = ReduceData(g.train2_a)
train3_a = ReduceData(g.train3_a)
train4_a = ReduceData(g.train4_a)
train5_a = ReduceData(g.train5_a)
train6_a = ReduceData(g.train6_a)
train7_a = ReduceData(g.train7_a)
train8_a = ReduceData(g.train8_a)
train9_a = ReduceData(g.train9_a)

train0_b = ReduceData(g.train0_b)
train1_b = ReduceData(g.train1_b)
train2_b = ReduceData(g.train2_b)
train3_b = ReduceData(g.train3_b)
train4_b = ReduceData(g.train4_b)
train5_b = ReduceData(g.train5_b)
train6_b = ReduceData(g.train6_b)
train7_b = ReduceData(g.train7_b)
train8_b = ReduceData(g.train8_b)
train9_b = ReduceData(g.train9_b)

train0_c = ReduceData(g.train0_c)
train1_c = ReduceData(g.train1_c)
train2_c = ReduceData(g.train2_c)
train3_c = ReduceData(g.train3_c)
train4_c = ReduceData(g.train4_c)
train5_c = ReduceData(g.train5_c)
train6_c = ReduceData(g.train6_c)
train7_c = ReduceData(g.train7_c)
train8_c = ReduceData(g.train8_c)
train9_c = ReduceData(g.train9_c)


test0_a = ReduceData(g.test0_a)
test0_b = ReduceData(g.test0_b)
test0_c = ReduceData(g.test0_c)
test1_a = ReduceData(g.test1_a)
test1_b = ReduceData(g.test1_b)
test1_c = ReduceData(g.test1_c)
test2_a = ReduceData(g.test2_a)
test2_b = ReduceData(g.test2_b)
test2_c = ReduceData(g.test2_c)
test3_a = ReduceData(g.test3_a)
test3_b = ReduceData(g.test3_b)
test3_c = ReduceData(g.test3_c)
test4_a = ReduceData(g.test4_a)
test4_b = ReduceData(g.test4_b)
test4_c = ReduceData(g.test4_c)
test5_a = ReduceData(g.test5_a)
test5_b = ReduceData(g.test5_b)
test5_c = ReduceData(g.test5_c)
test6_a = ReduceData(g.test6_a)
test6_b = ReduceData(g.test6_b)
test6_c = ReduceData(g.test6_c)
test7_a = ReduceData(g.test7_a)
test7_b = ReduceData(g.test7_b)
test7_c = ReduceData(g.test7_c)
test8_a = ReduceData(g.test8_a)
test8_b = ReduceData(g.test8_b)
test8_c = ReduceData(g.test8_c)
test9_a = ReduceData(g.test9_a)
test9_b = ReduceData(g.test9_b)
test9_c = ReduceData(g.test9_c)


# Normalizing the data's coordinates
train0_a = CenterData(g.train0_a)
train0_b = CenterData(g.train0_b)
train0_c = CenterData(g.train0_c)
train1_a = CenterData(g.train1_a)
train1_b = CenterData(g.train1_b)
train1_c = CenterData(g.train1_c)
train2_a = CenterData(g.train2_a)
train2_b = CenterData(g.train2_b)
train2_c = CenterData(g.train2_c)
train3_a = CenterData(g.train3_a)
train3_b = CenterData(g.train3_b)
train3_c = CenterData(g.train3_c)
train4_a = CenterData(g.train4_a)
train4_b = CenterData(g.train4_b)
train4_c = CenterData(g.train4_c)
train5_a = CenterData(g.train5_a)
train5_b = CenterData(g.train5_b)
train5_c = CenterData(g.train5_c)
train6_a = CenterData(g.train6_a)
train6_b = CenterData(g.train6_b)
train6_c = CenterData(g.train6_c)
train7_a = CenterData(g.train7_a)
train7_b = CenterData(g.train7_b)
train7_c = CenterData(g.train7_c)
train8_a = CenterData(g.train8_a)
train8_b = CenterData(g.train8_b)
train8_c = CenterData(g.train8_c)
train9_a = CenterData(g.train9_a)
train9_b = CenterData(g.train9_b)
train9_c = CenterData(g.train9_c)

test0_a = CenterData(g.test0_a)
test0_b = CenterData(g.test0_b)
test0_c = CenterData(g.test0_c)
test1_a = CenterData(g.test1_a)
test1_b = CenterData(g.test1_b)
test1_c = CenterData(g.test1_c)
test2_a = CenterData(g.test2_a)
test2_b = CenterData(g.test2_b)
test2_c = CenterData(g.test2_c)
test3_a = CenterData(g.test3_a)
test3_b = CenterData(g.test3_b)
test3_c = CenterData(g.test3_c)
test4_a = CenterData(g.test4_a)
test4_b = CenterData(g.test4_b)
test4_c = CenterData(g.test4_c)
test5_a = CenterData(g.test5_a)
test5_b = CenterData(g.test5_b)
test5_c = CenterData(g.test5_c)
test6_a = CenterData(g.test6_a)
test6_b = CenterData(g.test6_b)
test6_c = CenterData(g.test6_c)
test7_a = CenterData(g.test7_a)
test7_b = CenterData(g.test7_b)
test7_c = CenterData(g.test7_c)
test8_a = CenterData(g.test8_a)
test8_b = CenterData(g.test8_b)
test8_c = CenterData(g.test8_c)
test9_a = CenterData(g.test9_a)
test9_b = CenterData(g.test9_b)
test9_c = CenterData(g.test9_c)


# these are currently missing all trainX_c
trainX, trainy = ReshapeData(train0_a, train0_b, train1_a, train1_b, train2_a, train2_b, train3_a, train3_b, train4_a, train4_b, train5_a, train5_b, train6_a, train6_b, train7_a, train7_b, train8_a, train8_b, train9_a, train9_b)
testX, testy = ReshapeData(test0_a, test0_b, test1_a, test1_b, test2_a, test2_b, test3_a, test3_b, test4_a, test4_b, test5_a, test5_b, test6_a, test6_b, test7_a, test7_b, test8_a, test8_b, test9_a, test9_b)


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


for row in range(0,20000): # normally 0:20000
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



