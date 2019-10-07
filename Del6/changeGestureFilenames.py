import pickle
import os

class FILE_NAMES:
    def __init__(self,path):
        self.path = 'C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData'

    def Rename_Files(self,path):
        names = os.listdir(self.path)
        for name in names: #length of file directory
            trid = 0  # how many files have already been renamed for digit d?
            teid = 0  # how many test files have already been renamed for digit d?
            print(name)
            for d in range(0,10):
                train = 'train' in name
                test = 'test' in name
                num = str(d) in name
                if (train == True) & (num == True): # if the file name has both 'train' and num in it

                    oldname = (str(self.path) + '\{}'.format(name))
                    workaround = 'train'    # This is how we get around the fact that Python hates \t
                    newname = str(self.path) + '\{}'.format(workaround) + str(d) + '_{}.p'.format(trid)
                    os.rename(oldname,newname)
                    print('rename successful')
                    trid = trid + 1

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
