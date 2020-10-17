#These are the imports in teh game. First system is
#imported then ptgame is imported, then the Invade class
#is imprted folled by the missile class. Finally
#pygame.locals import * imports all the modules.
import sys
import pygame
import Invader
import Missile
from pygame.locals import *

#This is the game class called SpaceInvaders
class SpaceInvaders:

    # Constructor of the basic game class.
    # This constructor calls initialize and main_loop method.
    def __init__(self):
        self.initialize()
        self.main_loop()

    # This is the initialise method. It lets the
    #game initialise lots of different parameters
    #and load needed assets before the game starts
    #The pygame.key.set_re[eat controls how the held
    #keys can be repeated.
    def initialize(self):
        pygame.init()
        pygame.key.set_repeat(1, 1)
        
        #the width and height of the game screen
        self.width = 1024
        self.height = 768
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        #The name that will be displayed on the game window
        self.caption = "Space Invader!!"
        pygame.display.set_caption(self.caption)
        
        #the integer 30 is assigned to self.framerate        
        self.framerate = 30
        
        #the pygame.time.clock() method is assigned to
        #self.clock
        self.clock = pygame.time.Clock()
        
        #The gameState is set to 1          
        self.gameState = 1
        
        #the pygame.font.font with the font size is assigned
        #to self.font.
        self.font = pygame.font.Font(None, 40)
        
        #pygame.mixier.sound with the shoot sound file is assigned
        #to self.explosionsound
        self.explosionSound = pygame.mixer.Sound("shoot.wav")
        
        #Pygame.mixer.sound with the sound file fastinvader1
        #is assigned to fastinvader
        self.fastinvader = pygame.mixer.Sound("fastinvader1.wav")
        
        #pygame.mouse.set_visible is set to false so the mouse
        #cursor wont be dusplayed when hovering over the game
        #screen.
        pygame.mouse.set_visible(False)
        
        #This is the self.gameinitializegamevariables method
        self.initializeGameVariables()
        
        #This is the pygame.display.set_mode to the size of the screen
        #and range of 0 to 32 is assigned to self.windowSurface
        self.windowSurface = pygame.display.set_mode((1024, 768), 0, 32) 

 
    def initializeGameVariables(self):
        #All the images that are being used in the game are
        #assigned to different variables to make it more
        #conveniant to access them throught out the code.
        self.spaceImg = pygame.image.load('Space.png')
        self.invaderImg = pygame.image.load('invader.png')
        self.rocketLauncherImg = pygame.image.load('LaserBase.png')        
        self.missileImg = pygame.image.load('bullet.png')
        self.logoImg = pygame.image.load('Space_Invaders_title.png')
        self.helpImg = pygame.image.load('help_menu_title.png')
        self.gameoverImg = pygame.image.load('game_over_title.png')
        
        #These are the colours using the rgb model assigned
        #to name variables to make them esasier to remember and
        #access.
        self.PURPLE = (19,  15,  48)
        self.GREEN = (0, 153, 0)
        self.YELLOW = (255, 255, 0)
        
        #The X and Y position of the rocket launcher
        self.rocketXPos = 512
        self.rocketYPos = 560
        
        #The speed and starting direction of the invaders
        self.alienDirection = -1            
        self.alienSpeed = 20

        self.ticks = 0
        
        #First row of invaders
        #setting the X and Y positions of the invaders on the screen
        #adding 11 invaders and setting them an invader width apart
        self.invaders = []
        xPos = 512
        for i in range(11):
            invader = Invader.Invader()
            invader.setPosX(xPos)
            invader.setPosY(100)
            self.invaders.append(invader)            
            xPos += 32

        #second, third, fourth and fith rows of invaders chaning the Y position so invaders dont overlap
        #other part of the code similar to first row
        self.invaders2 = []
        xPos = 512
        for j in range(11):
            invader = Invader.Invader()
            invader.setPosX(xPos)
            invader.setPosY(150)
            self.invaders2.append(invader)            
            xPos += 32

        self.invaders3 = []
        xPos = 512
        for q in range(11):
            invader = Invader.Invader()
            invader.setPosX(xPos)
            invader.setPosY(200)
            self.invaders3.append(invader)            
            xPos += 32

        self.invaders4 = []
        xPos = 512
        for w in range(11):
            invader = Invader.Invader()
            invader.setPosX(xPos)
            invader.setPosY(250)
            self.invaders4.append(invader)            
            xPos += 32

        self.invaders5 = []
        xPos = 512
        for e in range(11):
            invader = Invader.Invader()
            invader.setPosX(xPos)
            invader.setPosY(300)
            self.invaders5.append(invader)            
            xPos += 32

        self.missileFired = None

        #setting player score varibale
        self.playerScore = 0

        #this is where teh totalscore variable is set
        self.totalscore = 0


        
 
    #this the main loop methid and is the method that keeps the game going
    #keeps on calling the draw and updae methods to keep the game constantly working
    def main_loop(self):
        self.clock = pygame.time.Clock()
        while True:
            gametime = self.clock.get_time()
            self.update(gametime)
            self.draw(gametime)
            self.clock.tick(self.framerate)
            
    #This is the update sttarted method and in here are the envents
    #that are used for the start menu of the game
    def updateStarted(self, gametime):
        events = pygame.event.get()
        
        #Two events are on the start nmenu
        #First one is when the Return(Enter) key is pressed the game starts
        #the secdond is pressing h from the start menu will take you to the
        #help menu screen and finally when the x key is pressed the game closes.
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.gameState = 2
                elif event.key == pygame.K_h:
                    self.gameState = 4
                elif event.key == pygame.K_x:
                     pygame.quit()
                     sys.exit()     
                
    #This is the update help function were events that are run
    #when specific keys are pressed on that menu
    def updateHelp(self, gametime):
        events = pygame.event.get()
        
        #this event is when the Return(Enter)key is pressed the game starts
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.gameState = 2
                    break
                
    #This is the update playing function and is the main section of the game.
    #This is where events that are happening during gameplay are controlled
    def updatePlaying(self, gametime):
        events = pygame.event.get()
        
    #These are the key events that the user will use to control the game when
    #they are playing it.

    #The first key evebt is the escape key and when it is pressed the gane
    #reverts back to the start menu and turn everything back to default.
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.initializeGameVariables()
                    self.gameState = 1

    #This event is used when the user presses the red cross on the game
    #game window and this shuts down the game.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    #This event check if the right key is being pressed by the user
    #and if it is moves teh rocketlauncher to teh right.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                      self.rocketXPos = self.rocketXPos + 4 

    #This event checks if  the left key is being pressed by the user
    #and if it is moves the rocketlauncher to the left.
                elif event.key == pygame.K_LEFT:
                      self.rocketXPos = self.rocketXPos - 4 

    #This event checks if the spacebar is being pressed and if it is
    #then makes an instance of the missile shotting from the rocketlauncher
    #using its X and Y positiobs.
                elif event.key == pygame.K_SPACE:
                    self.missileFired = Missile.Missile(self.rocketXPos, self.rocketYPos)
                    
        # these are the five for loops in the playing update method that constantly check
        #the rows of invaders to see if there are any invazder remaining in any of the 
        #rows and till every incaders is destroyed the isInvaderRemaining is set to true
        isInvaderRemaining = False
        for i in range(11):
            if self.invaders[i] != None:
                isInvaderRemaining = True
                break

        for j in range(11):
            if self.invaders2[j] != None:
                isInvaderRemaining = True
                break

        for q in range(11):
            if self.invaders3[q] != None:
                isInvaderRemaining = True
                break

        for w in range(11):
            if self.invaders4[w] != None:
                isInvaderRemaining = True
                break

        for e in range(11):
            if self.invaders5[e] != None:
                isInvaderRemaining = True
                break

        #This if statement checks if the there are any invadeers reamaing and if there are not
        #the isInvaderRemaining variable is set to false and the game goes to gameState 3 which
        #is the game over menu
        if isInvaderRemaining == False:
            self.gameState = 3
            return

        #This is statement if the missilefired is not equal to None which means if the missile
        #has been fired from the rocketlauncher then exectue the method move which mvoes the
        #missiles Y position
        if self.missileFired != None:
            self.missileFired.move()
            
        #This if statement checks if the rocket launchers position on the X axis is less than
        #100 which means if it close to the left end of the game screen. if it is then the
        #rockets position is set to 100 which will stop it from moving any further left and
        #going off screen.
        if self.rocketXPos < 100:
            self.rocketXPos = 100
            
        #This if sstatement checks if the ricket launchers X axis position is more than 924
        #which means it is near the right end of the game screen. if it is then the rockets
        #position is set to 924 which will stop it from going any further rught and moving
        #off screen.
        if self.rocketXPos > 924:
            self.rocketXPos = 924

        self.ticks = self.ticks + gametime
        
        #These are five for loops for the five invaders rows in teh game and these check
        #if each row of invaders is not equal to None which means if there are still invaders
        #remaining in each of the rows and if there are invaders remaining initializes the
        #moveHorizontal method which adds te alien speed and direction areguments for the rows
        #of invaders
        if self.ticks > 500:
            for i in range(11):
                if self.invaders[i] != None:
                    self.invaders[i].moveHorizontal(self.alienSpeed * self.alienDirection)
                    
        if self.ticks > 500:
            for j in range(11):
                if self.invaders2[j] != None:
                    self.invaders2[j].moveHorizontal(self.alienSpeed * self.alienDirection)
                    
        if self.ticks > 500:
            for q in range(11):
                if self.invaders3[q] != None:
                    self.invaders3[q].moveHorizontal(self.alienSpeed * self.alienDirection)
                    
        if self.ticks > 500:
            for w in range(11):
                if self.invaders4[w] != None:
                    self.invaders4[w].moveHorizontal(self.alienSpeed * self.alienDirection)   

        if self.ticks > 500:
            for e in range(11):
                if self.invaders5[e] != None:
                    self.invaders5[e].moveHorizontal(self.alienSpeed * self.alienDirection)
                    #self.fastinvader.play()
                    
            #These are the left  and right most invader variables and they are all set to None
            leftMostInvader = None
            rightMostInvader = None
            
            leftMostInvader2 = None
            rightMostInvader2 = None
            
            leftMostInvader3 = None
            rightMostInvader3 = None
            
            leftMostInvader4 = None
            rightMostInvader4 = None
            
            leftMostInvader5 = None
            rightMostInvader5 = None
            

            #These are the five for loops for the five rows of invadrs and these loops check
            #if each row of invaders os not equal ro none meaning if there are invaders
            #remamining in each row and if therea re invaders remaining assign the rows of
            #invaders to the leftMostInvader varaibles.
            for i in range(11):
                if self.invaders[i] != None:
                    leftMostInvader = self.invaders[i]
                    break

            for j in range(11):
                if self.invaders2[j] != None:
                    leftMostInvader2 = self.invaders2[j]
                    break

            for q in range(11):
                if self.invaders3[q] != None:
                    leftMostInvader3 = self.invaders3[q]
                    break

            for w in range(11):
                if self.invaders4[w] != None:
                    leftMostInvader4 = self.invaders4[w]
                    break

            for e in range(11):
                if self.invaders5[e] != None:
                    leftMostInvader5 = self.invaders5[e]
                    break
                
            #These five for loops check if the rows of invaders in the self.invaders are
            #not equal to none meanning if there are invaders still remaining in the rows
            #if there are invaders remaining then assign the self.invaders which are the rows
            #to the varaiable rightMostInvader and leftMostInvader[2-5] and at the end of
            #each for loop is a break to end the loop
            for i in range(10, -1, -1):
                if self.invaders[i] != None:
                    rightMostInvader = self.invaders[i]
                    break

            for j in range(10, -1, -1):
                if self.invaders2[j] != None:
                    rightMostInvader2 = self.invaders2[j]
                    break

            for q in range(10, -1, -1):
                if self.invaders3[q] != None:
                    rightMostInvader3 = self.invaders3[q]
                    break

            for w in range(10, -1, -1):
                if self.invaders4[w] != None:
                    rightMostInvader4 = self.invaders4[w]
                    break

            for e in range(10, -1, -1):
                if self.invaders5[e] != None:
                    rightMostInvader5 = self.invaders5[e]
                    break
                
            #This if statement get the X position of the leftMostInvader whcih are
            #assigned the rows of invaders and if te X position is less than 96
            #which is close to the left end of the game screen change the direction
            #of the rows to plus one so they will move right.
            if leftMostInvader.getPosX() < 96:
                self.alienDirection = +1
                
                #First 96 is assigned to the xOos varaible. Then the for loops are
                #started for the five rows of invaders in my game. The if statement
                #in the for loop checks if the self.invaders is not equal to none meaning
                #if there are invaders remaining in the rows the initialise the moververtial
                #method with the argument 4 and then set the position of selfinvaders for
                #each of the for loops to xPos which is 96/Finally assigning the width of the
                #invaderImg to the xPos varaible.
                xPos = 96
                for i in range(11):
                    if self.invaders[i] != None:
                        self.invaders[i].moveVertical(12)
                        self.invaders[i].setPosX(xPos)
                    xPos = xPos + self.invaderImg.get_width()
                    
                xPos = 96
                for j in range(11):
                    if self.invaders2[j] != None:
                        self.invaders2[j].moveVertical(12)
                        self.invaders2[j].setPosX(xPos)
                    xPos = xPos + self.invaderImg.get_width()

                xPos = 96
                for q in range(11):
                    if self.invaders3[q] != None:
                        self.invaders3[q].moveVertical(12)
                        self.invaders3[q].setPosX(xPos)
                    xPos = xPos + self.invaderImg.get_width()
                    
                xPos = 96
                for w in range(11):
                    if self.invaders4[w] != None:
                        self.invaders4[w].moveVertical(12)
                        self.invaders4[w].setPosX(xPos)
                    xPos = xPos + self.invaderImg.get_width()
                    
                xPos = 96
                for e in range(11):
                    if self.invaders5[e] != None:
                        self.invaders5[e].moveVertical(12)
                        self.invaders5[e].setPosX(xPos)
                    xPos = xPos + self.invaderImg.get_width()
                    
            #This if statement gets the X position of the rightMostInvader variable
            #for each of the loops and check if the position is more than 924 which
            #is near the right end of the game screen and if it is more than 924
            #then set self.alienDirection to -1 which will change the direction to
            #left.
            if rightMostInvader.getPosX() > 924 :
                self.alienDirection = -1
                
                #First 924 is minused by the invaderImg width ten times
                #and this is assigned to the varaible xPos. Then the for loops
                #are started for each of the rows of invaders. The if statement
                #checks if the self.invaders which are the rows are not equal
                #to None meaning theat if therea are any invaders remaining in
                #the rows andi fi therea are initialise the moveVertical method
                #and set the argument 12 to it. Then the self.invaders is set a X
                #position of parameter xPos. Finally the invaderImg widht is
                #assigned to the variable xPos.
                xPos = 924 - self.invaderImg.get_width() * 10
                for i in range(11):
                    if self.invaders[i] != None:
                        self.invaders[i].moveVertical(12)
                        self.invaders[i].setPosX(xPos)
                    xPos = xPos + self.invaderImg.get_width()

                xPos = 924 - self.invaderImg.get_width() * 10
                for j in range(11):
                    if self.invaders2[j] != None:
                        self.invaders2[j].moveVertical(12)
                        self.invaders2[j].setPosX(xPos)
                    xPos = xPos + self.invaderImg.get_width()
                    
                xPos = 924 - self.invaderImg.get_width() * 10
                for q in range(11):
                    if self.invaders3[q] != None:
                        self.invaders3[q].moveVertical(12)
                        self.invaders3[q].setPosX(xPos)
                    xPos = xPos + self.invaderImg.get_width()

                xPos = 924 - self.invaderImg.get_width() * 10
                for w in range(11):
                    if self.invaders4[w] != None:
                        self.invaders4[w].moveVertical(12)
                        self.invaders4[w].setPosX(xPos)
                    xPos = xPos + self.invaderImg.get_width()

                xPos = 924 - self.invaderImg.get_width() * 10
                for e in range(11):
                    if self.invaders5[e] != None:
                        self.invaders5[e].moveVertical(12)
                        self.invaders5[e].setPosX(xPos)
                    xPos = xPos + self.invaderImg.get_width()
                    
                    
            self.ticks = 0
            
            #First pygame rect is created for the rocket launcher and the rocketXPos
            #and the rocketYPos, the the rocketLaucher width and height is taken and
            #all of this is assigned to the rectRocketLauncher varaible. Then the for loops
            #for for the five rows of invaders is started and it first if statement in the loop
            #is saying if self.invaders which is the row of invaders is not equal to None. 
            #if it is not equal to None thyen create a rectInvader which has the the X and Y
            #positions of the invaders nad the width and height of the invaderImg, next another
            #if statement is started which checks if there has been a collision between the eectInvader
            #and the rectRocket Launcher and if there has been go to gameState 3 whci is the gameover menu
            rectRocketLauncher = pygame.Rect(self.rocketXPos, self.rocketYPos,
            self.rocketLauncherImg.get_width(), self.rocketLauncherImg.get_height())
            for i in range(11):
                if self.invaders[i] != None:
                    rectInvader = pygame.Rect(self.invaders[i].getPosX(), self.invaders[i].getPosY(), self.invaderImg.get_width(),
                    self.invaderImg.get_height())
                    if rectInvader.colliderect(rectRocketLauncher):
                        self.gameState = 3
                        return

            for j in range(11):
                if self.invaders2[j] != None:
                    rectInvader = pygame.Rect(self.invaders2[j].getPosX(), self.invaders2[j].getPosY(), self.invaderImg.get_width(),
                    self.invaderImg.get_height())
                    if rectInvader.colliderect(rectRocketLauncher):
                        self.gameState = 3
                        return

            for q in range(11):
                if self.invaders3[q] != None:
                    rectInvader = pygame.Rect(self.invaders3[q].getPosX(), self.invaders3[q].getPosY(), self.invaderImg.get_width(),
                    self.invaderImg.get_height())
                    if rectInvader.colliderect(rectRocketLauncher):
                        self.gameState = 3
                        return

            for w in range(11):
                if self.invaders4[w] != None:
                    rectInvader = pygame.Rect(self.invaders4[w].getPosX(), self.invaders4[w].getPosY(), self.invaderImg.get_width(),
                    self.invaderImg.get_height())
                    if rectInvader.colliderect(rectRocketLauncher):
                        self.gameState = 3
                        return

            for e in range(11):
                if self.invaders5[e] != None:
                    rectInvader = pygame.Rect(self.invaders5[e].getPosX(), self.invaders5[e].getPosY(), self.invaderImg.get_width(),
                    self.invaderImg.get_height())
                    if rectInvader.colliderect(rectRocketLauncher):
                        self.gameState = 3
                        return
        #This if statment checks if the variable self.missileFired is not equal to none
        #if it not equal to non the pygame rectangle is created around hte missile using
        #the missiles X and Y positions and getting the width and height of the missileImg
        #and assigning all of this to the variable called rectMissile. 
        if self.missileFired != None:
            rectMissile = pygame.Rect(self.missileFired.getPosX(), self.missileFired.getPosY(),
            self.missileImg.get_width(), self.missileImg.get_height())
            
            #These are the for loops for the five rows of invaders in the game. The if
            #statement checks if teh self.invaders in eachh of the for loops is not
            #equal to none and if it is not equal to none then create a rectangle for
            #the invaders using the invaders X and Y positions and getting the width and
            #height of the invaderImg and assigning all this to the rectInvader variable.
            #The next if statement checks if the rectMissile has collided with rectInvader,
            #if it has then set the missileFired variable to none, then set the self.invaders
            #to none, next play the self.explistion sound and finally add five to self.playerScore
            #and assign that to the variable self.playerScore. 

            for i in range(11):
                if self.invaders[i] != None:
                    rectInvader = pygame.Rect(self.invaders[i].getPosX(), self.invaders[i].getPosY(), self.invaderImg.get_width(),
                    self.invaderImg.get_height())
                    if rectMissile.colliderect(rectInvader):
                        self.missileFired = None
                        self.invaders[i] = None
                        self.explosionSound.play()
                        self.playerScore = self.playerScore + 5
                        break

            for j in range(11):
                if self.invaders2[j] != None:
                    rectInvader = pygame.Rect(self.invaders2[j].getPosX(), self.invaders2[j].getPosY(), self.invaderImg.get_width(),
                    self.invaderImg.get_height())
                    if rectMissile.colliderect(rectInvader):
                        self.missileFired = None
                        self.invaders2[j] = None
                        self.explosionSound.play()
                        self.playerScore = self.playerScore + 5
                        break

            for q in range(11):
                if self.invaders3[q] != None:
                    rectInvader = pygame.Rect(self.invaders3[q].getPosX(), self.invaders3[q].getPosY(), self.invaderImg.get_width(),
                    self.invaderImg.get_height())
                    if rectMissile.colliderect(rectInvader):
                        self.missileFired = None
                        self.invaders3[q] = None
                        self.explosionSound.play()
                        self.playerScore = self.playerScore + 5
                        break

            for w in range(11):
                if self.invaders4[w] != None:
                    rectInvader = pygame.Rect(self.invaders4[w].getPosX(), self.invaders4[w].getPosY(), self.invaderImg.get_width(),
                    self.invaderImg.get_height())
                    if rectMissile.colliderect(rectInvader):
                        self.missileFired = None
                        self.invaders4[w] = None
                        self.explosionSound.play()
                        self.playerScore = self.playerScore + 5
                        break

            for e in range(11):
                if self.invaders5[e] != None:
                    rectInvader = pygame.Rect(self.invaders5[e].getPosX(), self.invaders5[e].getPosY(), self.invaderImg.get_width(),
                    self.invaderImg.get_height())
                    if rectMissile.colliderect(rectInvader):
                        self.missileFired = None
                        self.invaders5[e] = None
                        self.explosionSound.play()
                        self.playerScore = self.playerScore + 5
                        break

            #The self.playerScore is assigned to the variable self.total score
            self.totalscore = self.playerScore

    #This is the updatEnded method and this where the game is always
    #updated for the end menu.
    def updateEnded(self, gametime):
        events = pygame.event.get()

        #This for loops checks if therea are any event in the events
        #if therea are the firs t if statement checks if the event.type
        #equals to pygame.KEYDOWN menaing if a key on the keybaord is
        #being pressed down, the next if statement checks if the key
        #that is being pressedis the x key if it is then the pygame.quit
        #and pygame.exit methods are started which close down the game
        #windows. Next a elif statement is used to check if this part of the
        #code might be used instead and the code checks if the r key is pressed
        #if it is then start te initialisegameVariables method and set the
        #gameState baack to 1 which is the start menu.
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    self.initializeGameVariables()
                    self.gameState = 1
                   
        
        
    # This is the update method and it checks all teh gameStaters..
    def update(self, gametime):

        #The first if statement checks if self.gameState equals 1, if
        #it does the nset self.updatestarted(gametime) so wheenever
        #self.gamestate 1 is used it will use updateStarted. The next
        #is a elif statement checks if self.gameState equals 2 if it does
        #then set it to updateplaying, next anotehr else if and this checks
        #if self.gameState is equal to 4 if it is the set it to updateplaying.
        #Final else if statement checks if teh self.gameState is equal to 4 if
        #it is the set it to updateHelp which is the help menu.
        if self.gameState == 1:
            self.updateStarted(gametime)
        elif self.gameState == 2:
            self.updatePlaying(gametime)
        elif self.gameState == 3:
            self.updateEnded(gametime)
        elif self.gameState == 4:
             self.updateHelp(gametime)

    #This is the the draw started method it draws everything onto the start menu
    #screen. The first thing that is draw is the background colour of the start menu
    #which is purple.
    def drawStarted(self, gametime):
        self.windowSurface.fill(self.PURPLE)
        
        #This is the title image of the space invaders and is being drawn
        #on teh start menu with the X and Y coordinates of its position
        self.screen.blit(self.logoImg, (140,-100))
        
        #First the InvaderOmg is blitted onto the sreen with teh X and Y
        #position. Next the font is added to self.font.size which then is
        #then assigned to width, height. next the text is rendered onto the
        #scfreen with colour and X and Y position.
        self.screen.blit(self.invaderImg, (380,304))
        width, height = self.font.size(" =   5   P O I N T S")
        text = self.font.render(" =   5   P O I N T S", True, (self.YELLOW))
        self.screen.blit(text, (425, 300 ))
        
        #similiar to the last text PRESS H FOR HELP MENU, PRESS ENTER TO START
        #and PRESS X TO EXIT GAME texts are added to the screen with the size
        #colour and X and Y positions.
        width, height = self.font.size("P R E S S   'H'   F O R   H E L P   M E N U")
        text = self.font.render("P R E S S   'H'   F O R   H E L P   M E N U", True, (self.YELLOW))
        xPos = (1024 - width)/2
        self.screen.blit(text, (xPos, 400 ))

        width, height = self.font.size("P R E S S   'E N T E R'   T O   S T A R T")
        text = self.font.render("P R E S S   'E N T E R '   T O   S T A R T", True,(self.YELLOW))
        xPos = (1024 - width)/2
        self.screen.blit(text, (xPos, 500))

        width, height = self.font.size("P R E S S   'X'   T O   E X I T   G A M E")
        text = self.font.render("P R E S S   'X'   T O   E X I T   G A M E", True, (self.YELLOW))
        xPos = (1024 - width)/2
        self.screen.blit(text, (xPos, 600))
        
        #Dinally for the start menu the pygame.display.flip updates the whole display
        #service to the screen.
        pygame.display.flip()

    #This is the drawPlaying function and this is where everything is drawn when gameplay
    #is happening. Firs the game background is set to  spaceImg.
    def drawPlaying(self, gametime):
        self.screen.blit(self.spaceImg, (0,0))
        
        #The score text and the self.playerscore with the colour of the text is assigned to the
        #score_text variable. Then the score_text is blitted to the game screen wit hthe X and Y
        #position.
        score_text = self.font.render("Score : %d" %self.playerScore, True, (self.GREEN))
        self.screen.blit(score_text, (30, 680))
        
        #This code adds a line on the game surce which is green and has the left and
        #right positions for the line and the thickness of the line.
        pygame.draw.line(self.windowSurface, self.GREEN, (0, 620), (1024, 620), 3)
        
        #This code blits the rocketlauncherImg wit the rocket X and Y positions.
        #Next an if statement is started which checks if self.missileFired is not equal
        #to None and if it is not equal to None then blit the missileImg and get the X
        #AMD Y position of self.missileFired and also the widht and height.
        self.screen.blit(self.rocketLauncherImg, (self.rocketXPos, self.rocketYPos))
        if self.missileFired != None:
            self.screen.blit(self.missileImg, (self.missileFired.getPosX(),
            self.missileFired.getPosY() - self.missileImg.get_height()))

        #These are the five for loops for the five rows of invaders. The if statement
        #in the for loops checks if the self.invaders is not equal to None if it is not
        #equal to None then blit the self.invaderImg and getposition of self.invaders
        #which are the X and Y positions of the invaders. Finally at the edd of the
        #last for loop for the last row pygame.display.flip updates the full game
        #surface.
        for i in range(11):
            if self.invaders[i] != None:
                self.screen.blit(self.invaderImg, self.invaders[i].getPosition())
       

        for j in range(11):
            if self.invaders2[j] != None:
                self.screen.blit(self.invaderImg, self.invaders2[j].getPosition())
       
        for q in range(11):
            if self.invaders3[q] != None:
                self.screen.blit(self.invaderImg, self.invaders3[q].getPosition())
        

        for w in range(11):
            if self.invaders4[w] != None:
                self.screen.blit(self.invaderImg, self.invaders4[w].getPosition())
        

        for e in range(11):
            if self.invaders5[e] != None:
                self.screen.blit(self.invaderImg, self.invaders5[e].getPosition())
        pygame.display.flip()

    #This is the drawHelp method and this is where everything for hte
    # help menu is drawn. Then tthe background of the gelp menu is eet to
    #purple.
    def drawHelp(self, gametime):
        self.windowSurface.fill(self.PURPLE)
        
        #This is where the helpimg is blit onto teh screen which is the
        #help menu title with its X and Y positions.
        self.screen.blit(self.helpImg, (140,-100))

        #This part of the code first adds the text to self.font.size and
        #then assigns it to width, height. Next the text is rendered with
        #the colour of the text. Then the 1024 - widht divided by 2 is
        #assigned to xPos and finally the text is blit with the X and Y
        #position and the X position is the variable xPos.
        width, height = self.font.size("LEFT ARROW KEY TO MOVE LEFT")                            
        text = self.font.render("LEFT ARROW KEY TO MOVE LEFT", True, (self.YELLOW))
        xPos = (1024 - width)/2
        self.screen.blit(text, (xPos, 300))
        
        #These next three texts are similiar to the first, they have the size of the
        #text then the fonts are rendered with the colour and next xPos is set and fianlly
        #the the texts are blit with the X position of xPos and Y position.
        width, height = self.font.size("RIGHT ARROW KEY TO MOVE RIGHT")                            
        text = self.font.render("RIGHT ARROW KEY TO MOVE RIGHT", True, (self.YELLOW))
        xPos = (1024 - width)/2
        self.screen.blit(text, (xPos, 400))

        width, height = self.font.size("SPACEBAR TO SHOOT")                            
        text = self.font.render("SPACEBAR TO SHOOT", True, (self.YELLOW))
        xPos = (1024 - width)/2
        self.screen.blit(text, (xPos, 500))

        width, height = self.font.size("P R E S S   'E N T E R'   T O   S T A R T   G A M E")
        text = self.font.render("P R E S S   'E N T E R'   T O   S T A R T   G A M E", True, (self.YELLOW))
        xPos = (1024 - width)/2
        self.screen.blit(text, (xPos, 600 ))

        #finally the whole screen surface is updated with the
        #pygame.display.flip code.
        pygame.display.flip()

        
    # This is the draw method and it draws the different states of the game.
    #The firs gamestate is 1 which is set to drawstarted so anything on
    #drawstarted will be on gamestate 1. Next is gamestate 2 which has
    #drawplaying and everything on drawstarted will be on gamestate 2.
    #Next is gamestate 3 which has drawended so everything on drawended
    #will be on gamestate 3. Finally the last game state is gamestate 4
    #which has drawHelp so everything in drawhelp will be drawn on
    #gamestate 4.
    def draw(self, gametime):              
        if self.gameState == 1:
            self.drawStarted(gametime)
        elif self.gameState == 2:
            self.drawPlaying(gametime)
        elif self.gameState == 3:
            self.drawEnded(gametime)
        elif self.gameState == 4:
            self.drawHelp(gametime)
            
    #Ris is the drawEnded method which draws everything on the end menu.
    #First the surface background is filled with the colour purple.
    def drawEnded(self, gametime):
        self.windowSurface.fill(self.PURPLE)

        #This code blits the gameoverImg which is the game over title to
        #the drawended screen with the X and Y positions.
        self.screen.blit(self.gameoverImg, (120,-100))
        
        #These two texts are on the drawEnded menu. First the text is added to
        #self.font.size, next the text is reneded with colours which is yellow
        #for both these texts. Next 1024 - width divided vy 2 is assigned to the
        #variable xPos. Finally the text is blit with the X and Y positions the X
        #position being xPos and Y position being 425.
        width, height = self.font.size("P R E S S   'R'   T O   R E S T A R T   G A M E")
        text = self.font.render("P R E S S   'R'   T O   R E S T A R T   G A M E", True, (self.YELLOW))
        xPos = (1024 - width)/2
        self.screen.blit(text, (xPos, 425))

        width, height = self.font.size("P R E S S   'X'   T O   E X I T   G A M E")
        text = self.font.render("P R E S S   'X'   T O   E X I T   G A M E", True, (self.YELLOW))
        xPos = (1024 - width)/2
        self.screen.blit(text, (xPos, 525))
        
        #This code draws the total score on the game end menu. The text and the
        #self.totalscore and the colour are added and then all this is assigned
        #to score1_text. fInally score1_text is blit with the X and Y positions.
        score1_text = self.font.render("T o t a l   S c o r e : %d" %self.totalscore, True,(self.GREEN))
        self.screen.blit(score1_text, (360, 325))
        
        #then the game surface is updated using the pygame.display.flip code.
        pygame.display.flip()
    

if __name__ == "__main__":
    game = SpaceInvaders()
