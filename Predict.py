import matplotlib.pyplot as plt
import numpy as np
from knn import KNN

knn = KNN()

knn.Load_Dataset('iris.csv')

colors = np.zeros((3,3), dtype='f')
colors[0,:] = [1,0.5,0.5]
colors[1,:] = [0.5,1,0.5]
colors[2,:] = [0.5,0.5,1]

x = knn.data[:, 0]
y = knn.data[:, 1]

trainX = knn.data[::2, 0:3]    #capital X means trainX stores a matrix
trainy = knn.target[::2]       #lowercase y means trainy stores a vector

testX = knn.data[1::2, 0:3]
testy = knn.target[1::2]


knn.Use_K_Of(15)
knn.Fit(trainX, trainy)

# actualClass = testy[63]
# prediction = knn.Predict(testX[63, 0:2])
# print(actualClass, prediction)


# for j in range(0, len(testy)):
#     actualClass = testy[j]
#     prediction = int(knn.Predict(testX[j, :]))
#     print(actualClass,prediction)

plt.figure() #everything up to step 42 is fine?!?!?!?!!!

[numItems, numFeatures] = knn.data.shape
for i in range(0, numItems/2):
    itemClass = int(trainy[i])
    currColor = colors[itemClass, :]
    plt.scatter(trainX[i,0], trainX[i,1], facecolor=currColor, edgecolor=[0,0,0], s=50, lw=2)

[numItems, numFeatures] = knn.data.shape
counter = 0
for i in range(0, numItems/2):
    itemClass = int(testy[i])
    currColor = colors[itemClass, :]
    prediction = int(knn.Predict(testX[i,:]))
    actualClass = testy[i]
    if actualClass == prediction:
        counter +=1
    edgeColor = colors[prediction,:]
    plt.scatter(testX[i,0], testX[i,1], facecolor=currColor, edgecolor=edgeColor, s=50, lw=2)

counter = float(counter)
accuracy = (counter / len(testy))*100

print('Algorithm is {}% accurate'.format(accuracy))

# plt.scatter(trainX[:,0], trainX[:,1], c=trainy)
# plt.scatter(testX[:,0], testX[:,1], c=testy)
# plt.scatter(x,y,c=knn.target)
plt.show()


#print(knn.data[:, 0:2])
#print(knn.target)

