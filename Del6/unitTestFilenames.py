import gestureDataFilenames

path = 'C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData'

filenames = gestureDataFilenames.FILE_NAMES(path)

filenames.Rename_Files(path)

gestureDictionary = filenames.Make_Gesture_Dictionary(path)

print(len(gestureDictionary))