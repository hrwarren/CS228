import numpy as np
import pickle
import sys
import time

sys.path.insert(0, '../..')
import knn
import gestureFilenames

knn = knn.KNN()

# g = gestureFilenames.GESTURES()



def ReshapeData(set0,set1,set2,set3,set4,set5,set6,set7,set8,set9,set10,set11,set12): #set13,set14,set15): #,set3,set4,set5,set6,set7,set8,set9):
    X = np.zeros((13000, 5*2*3), dtype = 'f') # normally 10000
    y = np.zeros((13000, 1), dtype='f')
    for row in range(0,1000):
        y[row, 0] = 0
        y[(row + 1000), 0] = 1
        y[(row + 2000), 0] = 2
        y[(row + 3000), 0] = 2
        y[(row + 4000), 0] = 3
        y[(row + 5000), 0] = 4
        y[(row + 6000), 0] = 5
        y[(row + 7000), 0] = 5
        y[(row + 8000), 0] = 6
        y[(row + 9000), 0] = 6
        y[(row + 10000), 0] = 7
        y[(row + 11000), 0] = 8
        y[(row + 12000), 0] = 9
        # y[(row + 13000), 0] = 8
        # y[(row + 14000), 0] = 9
        # y[(row + 15000), 0] = 9




        # for d in range(0,10): # normally 0:10
        #     y[(row + (d * 1000)), 0] = d

        col = 0
        for finger in range(0,5): #originally j
            for bone in range(0,2): #originally k and 0:4 2
                for coord_ind in range(0,3): #3: #originally m and 0:6 3
                    X[row, col] = set0[finger, bone, coord_ind, row]
                    X[row + 1000, col] = set1[finger, bone, coord_ind, row]
                    X[row + 2000, col] = set2[finger, bone, coord_ind, row]
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
                    # X[row + 13000, col] = set13[finger, bone, coord_ind, row]
                    # X[row + 14000, col] = set14[finger, bone, coord_ind, row]
                    # X[row + 15000, col] = set14[finger, bone, coord_ind, row]

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

def loadFiles(trainFile, testFile):
    pickle_in_train = open(trainFile, 'rb')
    train = pickle.load(pickle_in_train)
    Xtrain = ReduceData(train)
    Xtrain = CenterData(train)

    pickle_in_test = open(testFile, 'rb')
    test = pickle.load(pickle_in_test)
    Xtest = ReduceData(test)
    Xtest = CenterData(test)

    return Xtrain, Xtest

# Clark0, Ward3, Ward4, Livingston5, MacMaster6, MacMaster7, Erickson8, Childs9


# train_0, test_0 = loadFiles('userData\Soccorsi_train0.p', 'userData\Soccorsi_test0.p')
train_0, test_0 = loadFiles('userData\Warren_train0.p', 'userData\Warren_test0.p')


# train_1, test_1 = loadFiles('userData\Grasso_train1.p', 'userData\Grasso_test1.p')
# train_1b, test_1b = loadFiles('userData\Lin_train1.p', 'userData\Lin_test1.p')
train_1, test_1 = loadFiles('userData\Warren_train1.p', 'userData\Warren_test1.p')


train_2b, test_2b = loadFiles('userData\Grasso_train2.p', 'userData\Grasso_test2.p')
train_2, test_2 = loadFiles('userData\Warren_train2.p', 'userData\Warren_test2.p')


# train_3, test_3 = loadFiles('userData\Trinity_train3.p', 'userData\Trinity_test3.p')
# train_3b, test_3b = loadFiles('userData\Ward_train3.p', 'userData\Ward_test3.p')
train_3, test_3 = loadFiles('userData\Warren_train3.p', 'userData\Warren_test3.p')


# train_4, test_4 = loadFiles('userData\Ward_train4.p', 'userData\Ward_test4.p')
train_4, test_4 = loadFiles('userData\Warren_train4.p', 'userData\Warren_test4.p')


# train_5, test_5 = loadFiles('userData\Livingston_train5.p', 'userData\Livingston_test5.p')
train_5b, test_5b = loadFiles('userData\Deluca_train5.p', 'userData\Deluca_test5.p')
train_5, test_5 = loadFiles('userData\Warren_train5.p', 'userData\Warren_test5.p')


train_6c, test_6c = loadFiles('userData\Picard_train6.p', 'userData\Picard_test6.p')
train_6b, test_6b = loadFiles('userData\Deso_train6.p', 'userData\Deso_test6.p')
train_6, test_6 = loadFiles('userData\MacMaster_train6.p', 'userData\MacMaster_test6.p')

# :( MacMaster bad in classifier; Deso good in classifier bad in life, Picard good in classifier bad in life
# :/ Boland good in classifier and in life, but a lefty; Warren terrible in classifier but okay in life;
#       Peck good in classifier and okay in life, but you have to point fingers straight down

# train_7, test_7 = loadFiles('userData\Erickson_train7.p', 'userData\Erickson_test7.p')
# train_7b, test_7b = loadFiles('userData\Yeung_train7.p', 'userData\Yeung_test7.p')
train_7, test_7 = loadFiles('userData\Warren_train7.p', 'userData\Warren_test7.p')


# :( MacMaster bad in classifier bad in life; Mardis good in classifier bad in life;
#       Burleson good in classifier bad in life; Picard terrible in classifier bad in life
#       Huang good in classifier bad in life; Warren good in classifier terrible in life;
#       Enzmann good in classifier terrible in life;
# :/ Zhang good in classifier okay in life, but a lefty; Erickson terrible in classifier and okay in life

train_8, test_8 = loadFiles('userData\Zonay_train8.p', 'userData\Zonay_test8.p')
train_8b, test_8b = loadFiles('userData\Zhang_train8.p', 'userData\Zhang_test8.p')

# Erickson made a lot of confusion with 9

# train_9, test_9 = loadFiles('userData\Childs_train9.p', 'userData\Childs_test9.p')
# train_9b, test_9b = loadFiles('userData\Zonay_train9.p', 'userData\Zonay_test9.p')
train_9, test_9 = loadFiles('userData\Warren_train9.p', 'userData\Warren_test9.p')



# these are currently missing all trainX_c
trainX, trainy = ReshapeData(train_0,
                             train_1,
                             train_2, train_2b,
                             train_3, #train_3b,
                             train_4,
                             train_5, train_5b,
                             train_6, train_6b,
                             train_7, #train_7b,
                             train_8, #train_8b,
                             train_9) #train_9b) #, train_7b) #, train2_a, train3_a, train4_a, train5_a, train6_a, train7_a, train8_a, train9_a)
testX, testy = ReshapeData(test_0,
                           test_1,
                           test_2, test_2b,
                           test_3, #test_3b,
                           test_4,
                           test_5, test_5b,
                           test_6, test_6b,
                           test_7, #test_7b,
                           test_8, #test_8b,
                           test_9) #test_9b) #, test_7b) #test2_a, train3_a, test4_a, test5_a, test6_a, test7_a, test8_a, test9_a)




# for when each digit has 3 sets
# trainX, trainy = ReshapeData(train0_a, train0_b, train0_c, train1_a, train1_b, train1_c, train2_a, train2_b, train2_c, train3_a, train3_b, train3_c, train4_a, train4_b, train4_c, train5_a, train5_b, train5_c, train6_a, train6_b, train6_c, train7_a, train7_b, train7_c, train8_a, train8_b, train8_c, train9_a, train9_b, train9_c)
# testX, testy = ReshapeData(test0_a, test0_b, test0_c, test1_a, test1_b, test1_c, test2_a, test2_b, test2_c, test3_a, test3_b, test3_c, test4_a, test4_b, test4_c, test5_a, test5_b, test5_c, test6_a, test6_b, test6_c, test7_a, test7_b, test7_c, test8_a, test8_b, test8_c, test9_a, test9_b, test9_c)

knn.Use_K_Of(100) # originally 15
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


for row in range(0,13000): # normally 0:20000
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

print(testX)
print(testy)
print(testX.shape, testy.shape)

# Saving the classifier
userDataDir = 'userData\classifier_0123456789_k100.p'
pickle_out = open(userDataDir, 'wb')
pickle.dump(knn, open(userDataDir, 'wb'))
pickle_out.close()




