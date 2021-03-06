import pickle
import os

# what if we just put everything in a loop? just add every file's contents to the data one by one?
# and we didn't care what it was called?


class FILE_NAMES:
    def __init__(self,path):
        self.path = 'C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData'

    def Rename_Files(self,path):
        names = os.listdir(self.path)
        for name in names: #length of file directory
            trid0 = 0  # how many files have already been renamed for digit d?
            teid0 = 0  # how many test files have already been renamed for digit d?

            trid1 = 0
            teid1 = 0

            trid2 = 0
            teid2 = 0

            trid3 = 0
            teid3 = 0

            trid4 = 0
            teid4 = 0

            trid5 = 0
            teid5 = 0

            trid6 = 0
            teid6 = 0

            trid7 = 0
            teid7 = 0

            trid8 = 0
            teid8 = 0

            trid9 = 0
            teid9 = 0

            for d in range(0,10):
                train = 'train' in name
                test = 'test' in name
                num = str(d) in name
                if (train == True) & (num == True): # if the file name has both 'train' and num in it
                    if d == 0:
                        oldname = (str(self.path) + '\{}'.format(name))
                        workaround = 'train'  # This is how we get around the fact that Python hates \t
                        newname = str(self.path) + '\{}'.format(workaround) + str(d) + '_{}.p'.format(trid0)
                        os.rename(oldname, newname)
                        print('rename successful')
                        trid0 = trid0 + 1

                    if d == 1:
                        oldname = (str(self.path) + '\{}'.format(name))
                        workaround = 'train'  # This is how we get around the fact that Python hates \t
                        newname = str(self.path) + '\{}'.format(workaround) + str(d) + '_{}.p'.format(trid1)
                        os.rename(oldname, newname)
                        print('rename successful')
                        trid1 = trid1 + 1

                    if d == 2:
                        oldname = (str(self.path) + '\{}'.format(name))
                        workaround = 'train'  # This is how we get around the fact that Python hates \t
                        newname = str(self.path) + '\{}'.format(workaround) + str(d) + '_{}.p'.format(trid2)
                        os.rename(oldname, newname)
                        print('rename successful')
                        trid2 = trid2 + 1

                    if d == 3:
                        oldname = (str(self.path) + '\{}'.format(name))
                        workaround = 'train'  # This is how we get around the fact that Python hates \t
                        newname = str(self.path) + '\{}'.format(workaround) + str(d) + '_{}.p'.format(trid3)
                        os.rename(oldname, newname)
                        print('rename successful')
                        trid3 = trid3 + 1

                    oldname = (str(self.path) + '\{}'.format(name))
                    workaround = 'train'    # This is how we get around the fact that Python hates \t
                    newname = str(self.path) + '\{}'.format(workaround) + str(d) + '_{}.p'.format(trid)
                    os.rename(oldname,newname)
                    print('rename successful')
                    trid = trid + 1

                if (train == True) & (num == True) & (d == 0):
                    oldname = (str(self.path) + '\{}'.format(name))
                    workaround = 'train'  # This is how we get around the fact that Python hates \t
                    newname = str(self.path) + '\{}'.format(workaround) + str(d) + '_{}.p'.format(trid0)
                    os.rename(oldname, newname)
                    print('rename successful')
                    trid = trid + 1

                    trid0 = trid0 + 1

                    #save it as 'train (number d) _(number f).p' in a different directory
                if (test == True) & (num == True):

                    oldname = (str(self.path)+'\{}'.format(name))
                    workaround = 'test'
                    newname = str(self.path) + '\{}'.format(workaround) + str(d) + '_{}.p'.format(teid)
                    os.rename(oldname, newname)
                    print('rename successful')
                    teid = teid + 1
                    #string includes number d & string includes 'test'
                    #pickle in the file and
                    # save it as 'test (number d) _(number f).p' in a different directory

#i could make a dictionary, load the names into a dictionary then pull them out of the dictionary to run in the main script I have?

    def Make_Gesture_Dictionary(self,path):
        names = os.listdir(self.path)
        gestureDictionary = dict()
        i = 0
        for name in names:
            fileID = str(self.path)+'\{}'.format(name)
            avoidClf = 'classifier' in fileID
            if avoidClf == False:
                pickle_in = open(fileID)
                gestureDictionary[i] = {
                    '{}'.format(name) : pickle.load(pickle_in)
                }
            i = i+1

        return gestureDictionary


#every formatted name in the dictionary = the corresponding file from the directory

#
# set_name = 'Genovese_train0'
# pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
# train0 = pickle.load(pickle_in)
#
# set_name = 'Genovese_test0'
# pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
# test0 = pickle.load(pickle_in)
#
# set_name = 'train4'
# pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\userData\{}.dat'.format(set_name), 'rb')
# train4 = pickle.load(pickle_in)
#
# set_name = 'train5'
# pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\userData\{}.dat'.format(set_name), 'rb')
# train5 = pickle.load(pickle_in)
#
# set_name = 'test4'
# pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\userData\{}.dat'.format(set_name), 'rb')
# test4 = pickle.load(pickle_in)
#
# set_name = 'test5'
# pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\userData\{}.dat'.format(set_name), 'rb')
# test5 = pickle.load(pickle_in)
#
# train_names = [train0a, train0b, train1a, train1b, train2a, train2b, train3a, train3b, train4a, train4b,]
