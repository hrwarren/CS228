import pickle

# 2 and 6 became Left

# 1 clark
# 2


class GESTURES:
    def __init__(self):
        # LOADING IN THE TRAINING SETS

        #WARREN DATASETS

        #0
        set_name = 'Warren_train0'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train0_a = pickle.load(pickle_in)

        set_name = 'Warren_test0'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test0_a = pickle.load(pickle_in)

        #1
        # set_name = 'Warren_train1'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train1_a = pickle.load(pickle_in)
        #
        # set_name = 'Warren_test1'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.test1_a = pickle.load(pickle_in)

        set_name = 'Genovese_train1'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train1_a = pickle.load(pickle_in)

        set_name = 'Genovese_test1'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test1_a = pickle.load(pickle_in)

        #2
        set_name = 'Warren_train2'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train2_a = pickle.load(pickle_in)

        set_name = 'Warren_test2'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test2_a = pickle.load(pickle_in)

        #3
        set_name = 'Warren_train3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train3_a = pickle.load(pickle_in)

        set_name = 'Warren_test3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test3_a = pickle.load(pickle_in)

        #4
        set_name = 'Warren_train4'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train4_a = pickle.load(pickle_in)

        set_name = 'Warren_test4'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test4_a = pickle.load(pickle_in)

        #5
        set_name = 'Warren_train5'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train5_a = pickle.load(pickle_in)

        set_name = 'Warren_test5'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test5_a = pickle.load(pickle_in)


        #6
        set_name = 'Warren_train6'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train6_a = pickle.load(pickle_in)

        set_name = 'Warren_test6'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test6_a = pickle.load(pickle_in)

        # set_name = 'Deso_train6'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train6_a = pickle.load(pickle_in)
        #
        # set_name = 'Deso_test6'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.test6_a = pickle.load(pickle_in)

        #7
        set_name = 'Warren_train7'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train7_a = pickle.load(pickle_in)

        set_name = 'Warren_test7'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test7_a = pickle.load(pickle_in)

        #8
        set_name = 'Warren_train8'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train8_a = pickle.load(pickle_in)

        set_name = 'Warren_test8'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test8_a = pickle.load(pickle_in)

        #9
        set_name = 'Warren_train9'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train9_a = pickle.load(pickle_in)

        set_name = 'Warren_test9'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test9_a = pickle.load(pickle_in)







        # # 0         #Tried Genovese, Lee
        # set_name = 'Childs_train0'      #seems really rough
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train0_a = pickle.load(pickle_in)
        #
        set_name = 'Genovese_train0'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train0_a = pickle.load(pickle_in)
        set_name = 'Genovese_test0'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test0_a = pickle.load(pickle_in)

        set_name = 'Soccorsi_train0'    #seems very successful
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train0_b = pickle.load(pickle_in)
        set_name = 'Soccorsi_test0'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test0_b = pickle.load(pickle_in)

        set_name = 'Warren_train0'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train0_c = pickle.load(pickle_in)
        set_name = 'Warren_test0'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test0_c = pickle.load(pickle_in)
        #
        # # 0 test sets
        # set_name = 'Childs_test0'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.test0_a = pickle.load(pickle_in)


        #
        #
        #
        # # 1
        # # Tried and failed - Giroux, Newton, Thissell
        # # Tried and did ok - Lin,  Genovese
        # set_name = 'Newton_train1' #REALLY BAD ON 1
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train1_a = pickle.load(pickle_in)
        #
        # set_name = 'Thissell_train1' #PRETTY BAD ON 1
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train1_b = pickle.load(pickle_in)
        #
        # # 1 test sets
        # set_name = 'Newton_test1' #REALLY BAD ON 1
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.test1_a = pickle.load(pickle_in)
        #
        # set_name = 'Thissell_test1'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.test1_b = pickle.load(pickle_in)
        #
        # # high success alternates
        set_name = 'Genovese_train1'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train1_a = pickle.load(pickle_in)
        set_name = 'Genovese_test1'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test1_a = pickle.load(pickle_in)

        set_name = 'Warren_train1'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train1_b = pickle.load(pickle_in)
        set_name = 'Warren_test1'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test1_b = pickle.load(pickle_in)

        set_name = 'Lin_train1'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train1_c = pickle.load(pickle_in)
        set_name = 'Lin_test1'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test1_c = pickle.load(pickle_in)
        #
        #
        #
        # 2
        # Tried and did ok - Newton, Apple, Thissell
        set_name = 'Newton_train2'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train2_a = pickle.load(pickle_in)
        set_name = 'Newton_test2'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test2_a = pickle.load(pickle_in)

        set_name = 'Apple_train2'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train2_b = pickle.load(pickle_in)
        set_name = 'Apple_test2'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test2_b = pickle.load(pickle_in)

        set_name = 'Warren_train2'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train2_c = pickle.load(pickle_in)
        set_name = 'Warren_test2'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test2_c = pickle.load(pickle_in)




        # # 3     No one seems to have very good data on this one
        # # Tried and failed - Apple, Liu, Gordon, Ward, Beatty
        # # Tried and did okay - Warren, Trinity, Ogilvie
        #
        # set_name = 'Liu_train3'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train3_a = pickle.load(pickle_in)
        #
        # set_name = 'Ward_train3'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train3_b = pickle.load(pickle_in)
        #
        #
        # set_name = 'Liu_test3'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.test3_a = pickle.load(pickle_in)
        #
        # set_name = 'Ward_test3'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.test3_b = pickle.load(pickle_in)
        #
        # # high success alternates
        set_name = 'Trinity_train3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train3_a = pickle.load(pickle_in)
        set_name = 'Trinity_test3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test3_a = pickle.load(pickle_in)

        set_name = 'Ogilvie_train3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train3_b = pickle.load(pickle_in)
        set_name = 'Ogilvie_test3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test3_b = pickle.load(pickle_in)

        set_name = 'Warren_train3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train3_c = pickle.load(pickle_in)
        set_name = 'Warren_test3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test3_c = pickle.load(pickle_in)
        #
        #
        #
        # # 4     #Tried Beatty, Ortigara (best?), Deluca, Ogilvie(best?)
        # set_name = 'Warren_train4'  #Lefty
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train4_a = pickle.load(pickle_in)
        #
        # set_name = 'Beaulieu_train4'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train4_b = pickle.load(pickle_in)
        #
        # # 4 Test
        # set_name = 'Warren_test4'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.test4_a = pickle.load(pickle_in)
        #
        # set_name = 'Beaulieu_test4'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.test4_b = pickle.load(pickle_in)
        #
        # # Alternatives
        set_name = 'Ogilvie_train4'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train4_a = pickle.load(pickle_in)
        set_name = 'Ogilvie_test4'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test4_a = pickle.load(pickle_in)

        set_name = 'Ortigara_train4'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train4_b = pickle.load(pickle_in)
        set_name = 'Ortigara_test4'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test4_b = pickle.load(pickle_in)

        set_name = 'Warren_train4'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train4_c = pickle.load(pickle_in)
        set_name = 'Warren_test4'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test4_c = pickle.load(pickle_in)




        #
        #
        #
        #
        # # 5     #Tried Warren, Deluca
        # set_name = 'Beaulieu_train5'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train5_a = pickle.load(pickle_in)
        #
        # set_name = 'Peck_train5'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train5_b = pickle.load(pickle_in)
        #
        # # 5 Test
        # set_name = 'Beaulieu_test5'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.test5_a = pickle.load(pickle_in)
        #
        # set_name = 'Peck_test5'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.test5_b = pickle.load(pickle_in)
        #
        #Alternatives
        set_name = 'Livingston_train5'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train5_a = pickle.load(pickle_in)
        set_name = 'Livingston_test5'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test5_a = pickle.load(pickle_in)

        set_name = 'Ortigara_train5'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train5_b = pickle.load(pickle_in)
        set_name = 'Ortigara_train5'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test5_b = pickle.load(pickle_in)

        set_name = 'Warren_train5'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train5_c = pickle.load(pickle_in)
        set_name = 'Warren_test5'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test5_c = pickle.load(pickle_in)

        #
        #
        #
        # 6        # Tried Picard, Boland, Yeung, Deso, Wu
        set_name = 'Deso_train6'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train6_a = pickle.load(pickle_in)
        set_name = 'Deso_test6'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test6_a = pickle.load(pickle_in)

        set_name = 'Boland_train6'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train6_b = pickle.load(pickle_in)
        set_name = 'Boland_test6'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test6_b = pickle.load(pickle_in)

        set_name = 'Warren_train6'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train6_c = pickle.load(pickle_in)
        set_name = 'Warren_test6'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test6_c = pickle.load(pickle_in)






        # 7     #Tried Picard, Mardis, MacMaster, all did ok    #Krystal used Burleson, Rubin
        set_name = 'Rubin_train7'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train7_a = pickle.load(pickle_in)
        set_name = 'Rubin_test7'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test7_a = pickle.load(pickle_in)

        set_name = 'Mardis_train7'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train7_b = pickle.load(pickle_in)
        set_name = 'Mardis_test7'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test7_b = pickle.load(pickle_in)

        set_name = 'Warren_train7'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train7_c = pickle.load(pickle_in)
        set_name = 'Warren_test7'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test7_c = pickle.load(pickle_in)





        # 8     # Burleson, Rubin did well; Zonay was ehh
        set_name = 'Mardis_train8'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train8_a = pickle.load(pickle_in)
        set_name = 'Mardis_test8'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test8_a = pickle.load(pickle_in)

        set_name = 'Burleson_train8'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train8_b = pickle.load(pickle_in)
        set_name = 'Burleson_test8'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test8_b = pickle.load(pickle_in)

        set_name = 'Warren_train8'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train8_c = pickle.load(pickle_in)
        set_name = 'Warren_test8'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test8_c = pickle.load(pickle_in)






        # 9     #Tried Zonay, Lee
        set_name = 'Childs_train9'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train9_a = pickle.load(pickle_in)
        set_name = 'Childs_test9'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test9_a = pickle.load(pickle_in)

        set_name = 'Lee_train9'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train9_b = pickle.load(pickle_in)
        set_name = 'Lee_test9'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test9_b = pickle.load(pickle_in)

        set_name = 'Warren_train9'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train9_c = pickle.load(pickle_in)
        set_name = 'Warren_test9'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test9_c = pickle.load(pickle_in)

