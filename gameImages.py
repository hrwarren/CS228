import pygame
import constants



class PICS:

    def __init__(self):

        # Badges
        self.trophy = pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Trophy.jpg'), (80,80))

        self.practice = [pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\practiceBadge_0.jpg'), (50,50)),
                         pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\practiceBadge_1.jpg'), (50,50)),
                         pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\practiceBadge_2.jpg'), (50,50))]

        self.speed = [pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\speedBadge_0.jpg'), (50,50)),
                      pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\speedBadge_1.jpg'), (50,50)),
                      pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\speedBadge_2.jpg'), (50,50))]

        self.math = [pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\mathBadge_0.jpg'), (50,50)),
                     pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\mathBadge_1.jpg'), (50,50)),
                     pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\mathBadge_2.jpg'), (50,50))]

        self.b = [pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Badge_0.jpg'), (50,50)),
                  pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Badge_1.jpg'), (50,50)),
                  pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Badge_2.jpg'), (50,50))]

        # Centering
        self.initialImage = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\HandOverLeapVisual_cropped.jpg')
        self.moveRight = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\MoveRight.jpg')
        self.moveLeft = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\MoveLeft.jpg')
        self.moveForward = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\MoveForward.jpg')
        self.moveBackward = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\MoveBackward.jpg')


        # Success/Fail
        self.success = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Success.jpg')
        self.fail = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Fail.jpg')

        # Showing numbers to sign
        self.digits = [pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Digit0.jpg'),
                       pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Digit1.jpg'),
                       pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Digit2.jpg'),
                       pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Digit3.jpg'),
                       pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Digit4.jpg'),
                       pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Digit5.jpg'),
                       pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Digit6.jpg'),
                       pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Digit7.jpg'),
                       pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Digit8.jpg'),
                       pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Digit9.jpg')]

        self.numerals = [pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Num0.jpg'),
                         pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Num1.jpg'),
                         pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Num2.jpg'),
                         pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Num3.jpg'),
                         pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Num4.jpg'),
                         pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Num5.jpg'),
                         pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Num6.jpg'),
                         pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Num7.jpg'),
                         pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Num8.jpg'),
                         pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Num9.jpg')]

        # The star for the progress bar
        self.star = pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Star.jpg'), (30,30))

        # Lock and unlock images for login screen and mode screen
        self.lockedImage = pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\locked.jpg'), constants.lockSize)
        self.unlockedImage = pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\unlocked.jpg'), constants.lockSize)
        self.gameTitle = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\gameTitle.jpg')

        # Mode icons for mode selection screen
        self.practiceBox = pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\practiceBox.jpg'), (100,100))
        self.speedBox = pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\speedBox.jpg'), (100,100))
        self.mathBox = pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\mathBox.jpg'), (100,100))

        # Badge label icons
        self.pbTag = pygame.transform.scale(self.practiceBox, (45, 45))
        self.sbTag = pygame.transform.scale(self.speedBox, (45, 45))
        self.mbTag = pygame.transform.scale(self.mathBox, (45, 45))


        # Images for the "time's up" screen at the end of speed mode
        self.clock = pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\clock.jpg'), (120,144))
        self.again = pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Again.png'), (80, 80))

        # The "back" button for all modes
        self.backBtn = pygame.transform.scale(pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\prevBtn.jpg'), (60,30))













