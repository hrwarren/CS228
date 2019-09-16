import numpy
import pickle

class READER:
    def __init__(self):
        self.pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\userData\gesture2.p', 'rb')
        self.gestureData = pickle.load(self.pickle_in)
