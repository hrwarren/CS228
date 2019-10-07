import pickle

class GESTURES:
    def __init__(self):
        # LOADING IN THE TRAINING SETS

        # 0
        set_name = 'Genovese_train0'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train0_a = pickle.load(pickle_in)

        set_name = 'Lee_train0'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train0_b = pickle.load(pickle_in)

        # 1
        set_name = 'Giroux_train1'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train1_a = pickle.load(pickle_in)

        set_name = 'Newton_train1'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train1_b = pickle.load(pickle_in)

        # 2
        set_name = 'Newton_train2'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train2_a = pickle.load(pickle_in)

        set_name = 'Apple_train2'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train2_b = pickle.load(pickle_in)

        # 3
        set_name = 'Apple_train3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train3_a = pickle.load(pickle_in)

        set_name = 'Ward_train3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train3_b = pickle.load(pickle_in)

        # 4
        set_name = 'Warren_train4'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train4_a = pickle.load(pickle_in)

        set_name = 'Beatty_train4'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train4_b = pickle.load(pickle_in)

        # 5
        set_name = 'Warren_train5'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train5_a = pickle.load(pickle_in)

        set_name = 'Deluca_train5'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train5_b = pickle.load(pickle_in)

        # 6
        set_name = 'Picard_train6'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train6_a = pickle.load(pickle_in)

        set_name = 'Boland_train6'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train6_b = pickle.load(pickle_in)

        # 7
        set_name = 'Picard_train7'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train7_a = pickle.load(pickle_in)

        set_name = 'Mardis_train7'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train7_b = pickle.load(pickle_in)

        # 8
        set_name = 'Zonay_train8'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train8_a = pickle.load(pickle_in)

        set_name = 'Rubin_train8'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train8_b = pickle.load(pickle_in)

        # 9
        # set_name = 'Fath_train9'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train9_a = pickle.load(pickle_in)
        set_name = 'Childs_train9'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train9_a = pickle.load(pickle_in)

        set_name = 'Zonay_train9'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train9_b = pickle.load(pickle_in)



        # LOADING IN THE TESTING SETS

        # 0
        set_name = 'Genovese_test0'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test0_a = pickle.load(pickle_in)

        set_name = 'Lee_test0'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test0_b = pickle.load(pickle_in)

        # 1
        set_name = 'Giroux_test1'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test1_a = pickle.load(pickle_in)

        set_name = 'Newton_test1'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test1_b = pickle.load(pickle_in)

        # 2
        set_name = 'Newton_test2'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test2_a = pickle.load(pickle_in)

        set_name = 'Apple_test2'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test2_b = pickle.load(pickle_in)

        # 3
        set_name = 'Apple_test3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test3_a = pickle.load(pickle_in)

        set_name = 'Ward_test3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test3_b = pickle.load(pickle_in)

        # 4
        set_name = 'Warren_test4'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test4_a = pickle.load(pickle_in)

        set_name = 'Beatty_test4'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test4_b = pickle.load(pickle_in)

        # 5
        set_name = 'Warren_test5'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test5_a = pickle.load(pickle_in)

        set_name = 'Deluca_test5'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test5_b = pickle.load(pickle_in)

        # 6
        set_name = 'Picard_test6'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test6_a = pickle.load(pickle_in)

        set_name = 'Boland_test6'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test6_b = pickle.load(pickle_in)

        # 7
        set_name = 'Picard_test7'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test7_a = pickle.load(pickle_in)

        set_name = 'Mardis_test7'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test7_b = pickle.load(pickle_in)

        # 8
        set_name = 'Zonay_test8'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test8_a = pickle.load(pickle_in)

        set_name = 'Rubin_test8'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test8_b = pickle.load(pickle_in)

        # 9
        # set_name = 'Fath_test9'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.test9_a = pickle.load(pickle_in)
        set_name = 'Childs_test9'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test9_a = pickle.load(pickle_in)

        set_name = 'Zonay_test9'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test9_b = pickle.load(pickle_in)
