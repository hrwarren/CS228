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
        self.train0_c = pickle.load(pickle_in)

        set_name = 'Soccorsi_train0'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train0_b = pickle.load(pickle_in)



        # 1
        # set_name = 'Giroux_train1' #PRETTY BAD ON 1
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train1_e = pickle.load(pickle_in) #ORIGINALLY _a
        #
        # set_name = 'Newton_train1'  #REALLY BAD ON 1
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train1_d = pickle.load(pickle_in)

        set_name = 'Thissell_train1' #PRETTY BAD ON 1
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train1_c = pickle.load(pickle_in) #ORIGINALLY _c

        set_name = 'Lin_train1' #Acceptable
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train1_b = pickle.load(pickle_in)

        set_name = 'Genovese_train1' #SOLID
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train1_a = pickle.load(pickle_in) #ORIGINALLY did not exist


        # 2
        set_name = 'Newton_train2'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train2_a = pickle.load(pickle_in)

        set_name = 'Apple_train2'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train2_b = pickle.load(pickle_in)

        set_name = 'Thissell_train2'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train2_c = pickle.load(pickle_in)

        # 3
        set_name = 'Apple_train3' #REALLY BAD ON 3
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train3_f = pickle.load(pickle_in) #ORIGINALLY _a

        set_name = 'Ward_train3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train3_e = pickle.load(pickle_in) #ORIGINALLY_b

        set_name = 'Liu_train3' #maybe not great for 3?
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train3_c = pickle.load(pickle_in) #ORIGINALLY _c

        set_name = 'Trinity_train3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train3_a = pickle.load(pickle_in) #ORIGINALLY _c

        set_name = 'Warren_train3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train3_b = pickle.load(pickle_in) #ORIGINALLY _c

        # set_name = 'Gordon_train3'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train3_d = pickle.load(pickle_in) #ORIGINALLY _c

        set_name = 'Ogilvie_train3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train3_b = pickle.load(pickle_in) #ORIGINALLY _c


        # 4
        set_name = 'Warren_train4'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train4_a = pickle.load(pickle_in)

        # set_name = 'Beatty_train4' #POSSIBLY TERRIBLE?
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train4_d = pickle.load(pickle_in)

        # set_name = 'Ortigara_train4'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train4_d = pickle.load(pickle_in)

        # set_name = 'Deluca_train4' #EVEN WORSE
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train4_e = pickle.load(pickle_in)

        set_name = 'Livingston_train4' #currently least terrible b option
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train4_c = pickle.load(pickle_in)

        set_name = 'Ogilvie_train4' #BEST B OPTION
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train4_b = pickle.load(pickle_in)

        # 5
        set_name = 'Warren_train5' #acceptable for now
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train5_a = pickle.load(pickle_in)

        set_name = 'Deluca_train5'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train5_c = pickle.load(pickle_in)

        set_name = 'Peck_train5' #acceptable options for now
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train5_b = pickle.load(pickle_in)

        # 6
        # set_name = 'Picard_train6'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train6_d = pickle.load(pickle_in) #ORIGINALLY _a

        set_name = 'Boland_train6'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train6_c = pickle.load(pickle_in) #ORIGINALLY _b

        # set_name = 'Yeung_train6'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.train6_e = pickle.load(pickle_in) #ORIGINALLY _c

        set_name = 'Deso_train6'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train6_a = pickle.load(pickle_in)

        set_name = 'Wu_train6'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train6_b = pickle.load(pickle_in)

        # 7
        set_name = 'Picard_train7'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train7_b = pickle.load(pickle_in) #ORIGINALLY _a

        set_name = 'Mardis_train7'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train7_a = pickle.load(pickle_in) #ORIGINALLY _b

        set_name = 'MacMaster_train7'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train7_c = pickle.load(pickle_in)

        # 8
        set_name = 'Zonay_train8'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train8_c = pickle.load(pickle_in)

        set_name = 'Rubin_train8' #BEAUTIFUL
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train8_b = pickle.load(pickle_in)

        set_name = 'Burleson_train8' #BEAUTIFUL
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train8_a = pickle.load(pickle_in)

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

        set_name = 'Lee_train9'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.train9_c = pickle.load(pickle_in)




# class TEST_GESTURES:
#         # LOADING IN THE TESTING SETS
#     def __init__(self):

        # 0
        set_name = 'Genovese_test0'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test0_a = pickle.load(pickle_in)

        set_name = 'Lee_test0'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test0_c = pickle.load(pickle_in)

        set_name = 'Soccorsi_test0'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test0_b = pickle.load(pickle_in)

        # 1
        # set_name = 'Giroux_test1'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.test1_e = pickle.load(pickle_in) #ORIGINALLY _a

        # set_name = 'Newton_test1' #REALLY BAD ON 1
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.test1_d = pickle.load(pickle_in) #ORIGINALLY _b

        set_name = 'Thissell_test1'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test1_c = pickle.load(pickle_in) #ORIGINALLY _c

        set_name = 'Lin_test1' #Acceptable
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test1_b = pickle.load(pickle_in)

        set_name = 'Genovese_test1'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test1_a = pickle.load(pickle_in) #ORIGINALLY _did not exist

        # 2
        set_name = 'Newton_test2'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test2_a = pickle.load(pickle_in)

        set_name = 'Apple_test2'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test2_b = pickle.load(pickle_in)

        set_name = 'Thissell_test2'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test2_c = pickle.load(pickle_in)

        # 3
        set_name = 'Apple_test3' #REALLY BAD ON 3
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test3_f = pickle.load(pickle_in) #ORIGINALLY _a

        set_name = 'Ward_test3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test3_d = pickle.load(pickle_in) #ORIGINALLY _b

        set_name = 'Liu_test3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test3_c = pickle.load(pickle_in) #ORIGINALLY _c

        set_name = 'Trinity_test3' #REALLY GOOD FOR 3
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test3_a = pickle.load(pickle_in) #ORIGINALLY _c

        set_name = 'Warren_test3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test3_b = pickle.load(pickle_in) #ORIGINALLY _c

        set_name = 'Gordon_test3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test3_e = pickle.load(pickle_in) #ORIGINALLY _c

        set_name = 'Ogilvie_test3'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test3_b = pickle.load(pickle_in) #ORIGINALLY _c

        # 4
        set_name = 'Warren_test4'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test4_a = pickle.load(pickle_in)

        # set_name = 'Beatty_test4' #POSSIBLY TERRIBLE?
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.test4_d = pickle.load(pickle_in)

        # set_name = 'Ortigara_test4'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.test4_d = pickle.load(pickle_in)

        # set_name = 'Deluca_test4'
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.test4_e = pickle.load(pickle_in)

        set_name = 'Livingston_test4' #currently least terrible of b options
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test4_c = pickle.load(pickle_in)

        set_name = 'Ogilvie_test4' #BEST B OPTION
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test4_b = pickle.load(pickle_in)

        # 5
        set_name = 'Warren_test5' #acceptable for now
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test5_a = pickle.load(pickle_in)

        set_name = 'Deluca_test5'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test5_c = pickle.load(pickle_in)

        set_name = 'Peck_test5' #acceptable for now
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test5_b = pickle.load(pickle_in)

        # 6
        set_name = 'Picard_test6' #Probably bad
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test6_d = pickle.load(pickle_in) #ORIGINALLY _a

        set_name = 'Boland_test6'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test6_c = pickle.load(pickle_in) #ORIGINALLY _b

        # set_name = 'Yeung_test6' #BAD
        # pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        # self.test6_d = pickle.load(pickle_in) #ORIGINALLY _c

        set_name = 'Deso_test6' #BEST OPTION
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test6_a = pickle.load(pickle_in)

        set_name = 'Wu_test6' # BEST OPTION
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test6_b = pickle.load(pickle_in)



        # 7
        set_name = 'Picard_test7'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test7_b = pickle.load(pickle_in) #ORIGINALLY _a

        set_name = 'Mardis_test7'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test7_a = pickle.load(pickle_in) #ORIGINALLY _b

        set_name = 'MacMaster_test7'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test7_c = pickle.load(pickle_in)

        # 8
        set_name = 'Zonay_test8'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test8_c = pickle.load(pickle_in)

        set_name = 'Rubin_test8' #BEAUTIFUL
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test8_b = pickle.load(pickle_in)

        set_name = 'Burleson_test8' #BEAUTIFUL
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test8_a = pickle.load(pickle_in)

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

        set_name = 'Lee_test9'
        pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\{}.p'.format(set_name), 'rb')
        self.test9_c = pickle.load(pickle_in)

#pickle_in = open(directory,'rb')

