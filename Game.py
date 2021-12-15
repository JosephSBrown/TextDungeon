##Importing standard modules
import time
import random

##importing classes for game purposes
from Player import Player
import NPC

#--Game Class-----------------------------------------------------------------------------------------------
class Game():

##Lists relevant to class
    Username = [] #List for Username from Login
    Room1Item = ['Coins', 'Iron Helmet'] #List with Items in Room1
    Room2Item = ['Iron Sword'] #List with items in Room2

##Constructor for intialising game
    def __init__(self):
        self.GameStart()

##scene setting game start
    def GameStart(self):
        print("Welcome to Text Dungeon!\nThanks For Playing!") #Start Text
        time.sleep(2) #sleep to wait and space out code
        print("To Complete the Game Please Answer the Questions\nMake Sure This is With Valid Choices!") #Instruction
        time.sleep(2) #sleep to wait and space out code
        print("Your Choices Will Appear Like This: [Yes] or [No]") #Instructions 2
        time.sleep(2) #sleep to wait and space out code
        AskName = input('Would You Like to Use ' + Game.Username[0] + ' As Your Adventuring Name?\n[Yes] or [No]\n> ') #Username Asking
        if AskName in Player.Yes: #if player answers yes
            self.PlayerName = Game.Username[0] #set username to login
        elif AskName in Player.No: #if player answers no
            self.PlayerName = input('Would You Mind Giving Us Your Name For the Adventure?\n[This Can Be Any Name/Word!]\n> ') #set username to answer to this input
        else: #if neither
            print('It Was a Yes or No Answer, So I assume that\'s a No...') #informs player using login
            self.PlayerName = Game.Username[0] #set playername to login
            return #return out of else
        time.sleep(1) #sleep to wait and space out code
        print('Well...' + self.PlayerName + '! That\'s a Wonderful Name... Let\'s Begin...') #warm welcome
        time.sleep(2) #sleep to wait and space out code
        self.SceneSetting() #start next scene

##setting the scene of the game, backstory
    def SceneSetting(self): 
        print("You Awaken in a Small Forest Without Much to See Around You...") #Scenery
        time.sleep(2) #sleep to wait and space out code
        print("The Only Thing Clear to You for Miles Around is a Small Dungeon Ahead...") #First mention of dungeon
        time.sleep(2) #sleep to wait and space out code
        self.DungeonEntrance() #next function

##entering the dungeon
    def DungeonEntrance(self):
        def Entrance(): #nested function for entrance choice         
            EntranceQ = input("The Time Comes...\nDo You Dare Enter?\n[Yes] or [No]\n> ") #game start question
            if EntranceQ in Player.Yes: #if player answers yes
                self.Room1() #go to room 1
            elif EntranceQ in Player.No: #if player answers no
                self.GameEnd() #end the game
            else: #if neither
                print('Please Choose a Valid Option...') #inform the player of invalid choice
                time.sleep(2) #wait 2 seconds
                Entrance() #Run Question again

        print("The Dungeon Looks Untouched but You Hear Hallowed Voices From Inside...\nYou Wonder If You Dare to Enter...") #Spooky
        time.sleep(2) #sleep to wait and space out code
        Entrance() #Run Entrance Question

##Centre of Room1
    def Room1(self):
        def RoomChoice(): #nested function for room choice
            Room1FirstChoice = input("What Would You Like to Do?\n[Look] or [Move] or [Bag] or [Statistics]\n> ") #player input choice
            if Room1FirstChoice in Player.Move: #if player choice in move
                Room1DirectionChoice() #go to direction choice
            elif Room1FirstChoice in Player.Look: #if player choice in look
                print("You Look Around...\nYou See the Following Items...") #set the scene around the room
                print(Game.Room1Item) #show items currently in the room
                time.sleep(2) #sleep to wait and space out code
                ItemChoice = input('What Would You Like to Do?\n[Collect] or [Return]\n> ') #ask if they want the items
                if ItemChoice in Player.Collect: #if player chooses to collect
                    Item = input('What Would You Like to Collect?\n[Coins] or [Armour]\n> ') #which item will they collect
                    if Item in Player.CoinsChoice: #if coins
                        if 'Coins' in Game.Room1Item: #if coins are still in the room list
                            Game.Room1Item.remove('Coins') #remove the coins
                            Player.CoinCollect(random.randrange(0, 100)) #add a random selection of coins to the inventory
                        else: #if it isn't
                            print('Please Choose a Valid Option...') #inform of invalid option
                            RoomChoice() #run the choice function again
                    elif Item in Player.ArmourChoice: #if choice is for the armour
                        if 'Iron Helmet' in Game.Room1Item: #and the armour is still in the list
                            Game.Room1Item.remove('Iron Helmet') #remove the armour from the room
                            Player.ArmourCollect('Iron Helmet', 10) #put the armour on the player
                    else: #if neither
                        print('Please Choose a Valid Option...') #inform of invalid choice
                        RoomChoice() #run the choice again
                elif ItemChoice in Player.Return: #if player chooses to retunr
                    print('You Chose to Return...') #inform of their choice
                    time.sleep(2) #sleep to wait and space out code
                    RoomChoice() #start player choice again
                else: #if neither
                    print('Please Choose a Valid Option...') #inform of invalid choice
                    RoomChoice() #run choice again
                time.sleep(2) #sleep to wait and space out code
                RoomChoice() #run the nested function
            elif Room1FirstChoice in Player.Bag: #if the choice is to view inventory
                Player.PlayerBag() #display the inventory using player bag function
                RoomChoice() #start choice again
            elif Room1FirstChoice in Player.Statistics: #if the player chooses statistics
                Player.TotalStatistics() #display current player statistics function
                RoomChoice() #run the choice again
            else: #if none
                print('Please Choose a Valid Option...') #inform of invalid choice
                RoomChoice() #run the choice again

        def Room1DirectionChoice(): ##nested direction choice function
            Room1Choice = input("Which Direction Would You Like to Move?\n[North] or [South] or [West]\n> ") #what direction does the player want to move in
            if Room1Choice in Player.West: #if choice is west
                self.Room1_West() #go to the western room function
            elif Room1Choice in Player.North: #if choice is North
                self.Room1_North() #go to the northern room function
            elif Room1Choice in Player.South: #if the choice is south
                self.Room1_South() #go to the southern room function
            else: #if none of these
                print("Please Choose a Valid Option...") #inform of poor choice
                Room1DirectionChoice() #run the choice again
        
        print("You are Greeted by a Room...") #setting the room scene
        time.sleep(2) #sleep to wait and space out code
        print("The Room is Tiled with 2 Doors...") #more room detail
        time.sleep(2) #sleep to wait and space out code
        print("Walking to the North takes you to a Door...") #informs of directions possible
        time.sleep(2) #sleep to wait and space out code
        print("Heading West Takes You to Another Door...") #informs of directions possible
        time.sleep(2) #sleep to wait and space out code
        print("And Heading South Takes You Back Out the Dungeon...") #informs of directions possible
        time.sleep(2) #sleep to wait and space out code
        RoomChoice() #runs the choices within the room

##Northern Direction of Room 1
    def Room1_North(self):
        def Room1NorthChoice(): #nested player choice function
            NorthDoorChoice = input('What Would You Like to Do?\n[Use] or [Return]\n> ') #player choice
            if NorthDoorChoice in Player.Use: #if player choice is in use
                print('You Chose to Use...') #inform player of option
                time.sleep(2) #sleep to wait and space out code
                print('Your Bag Currently Contains:\n' + Player.PlayerBag()) #Display current bag
                NorthDoorUse = input('What Would You Like to Use?\n> ') #ask what in inventory to use
                if NorthDoorUse in Player.Key: #if choice is key
                    if 'Key' in Player.Inventory: #if key is in inventory
                        Player.Inventory.remove('Key') #remove key from inventory
                        print("You Used the Key!") #inform of choice made
                        time.sleep(2) #sleep to wait and space out code
                        Player.PlayerBag() #display player bag
                        time.sleep(2) #sleep to wait and space out code
                        self.Room3() #open third room
                    elif 'Key' not in Player.Inventory: #if key is not in the inventory
                        print('You Do Not Have The Key and Must Find It First...\n') #inform player of what they need to do
                        time.sleep(2) #sleep to wait and space out code
                        print('You Return to the Centre of the Room...') #inform player of movement
                        self.Room1() #call room centre function
            elif NorthDoorChoice in Player.Return: #if player chooses to return
                self.Room1() #go back to the centre of the room
            else: #if neither
                print('Please Choose a Valid Option...') #inform of poor choice
                Room1NorthChoice() #run options again

        print('You Approach the Northern Door...') #inform player of movement
        time.sleep(2) #sleep to wait and space out code
        Room1NorthChoice() #run the door options

##Western Direction of Room1
    def Room1_West(self):
        def Room1DoorChoice(): #nested choice function
            DoorChoice = input("What Would You Like to Do?\n[Use] or [Return]\n> ") #player choice
            if DoorChoice in Player.Use: #if player choice is in use
                print('You Look in Your Bag... \n') #inform of actions
                Player.PlayerBag() #display player bag
                input('What Would You Like to Use?\n> ') #fake input, no input required
                Player.PlayerBag() #display player bag
                print('There Was No Need to Use Any Items As the Door is Unlocked Already...') #inform player door already open
                time.sleep(2) #sleep to wait and space out code
                KeyUse = input('Would You Like to Enter the Room?\n[Yes] or [No]\n> ') #ask player option
                if KeyUse in Player.Yes: #if player says yes
                    self.Room2() #enter room
                elif KeyUse in Player.No: #if player says no
                    print('You Go Back to the Centre of Room...') #inform player of choice
                    time.sleep(2) #sleep to wait and space out code
                    self.Room1() #go back to centre of room
                else: #if none
                    print("Please Choose a Valid Option...") #inform of poor choice
                    Room1DoorChoice() #run options again
            elif DoorChoice in Player.Return: #if player chooses return
                Room1ReturnChoice = input('Are You Sure?\n[Yes] or [No]\n> ') #confirmation input
                if Room1ReturnChoice in Player.Yes: #if player chooses yes
                    self.Room1() #go back to centre of room
                elif Room1ReturnChoice in Player.No: #if player chooses no
                    self.Room1_West #go back to the west of the room
                else: #if none
                    print('Please Choose a Valid Choice...') #inform of poor choice
                    Room1DoorChoice() #run options again
            else: #if none of the above
                print("Please Choose a Valid Option...") #inform of poor choice
                time.sleep(2) #sleep to wait and space out code
                Room1DoorChoice() #run the options again
        
        print("You Are Met By a Door...") #setting the scene
        time.sleep(2) #sleep to wait and space out code
        Room1DoorChoice() #Run the options for the first time

##A Function to Open Room 1 South
    def Room1_South(self):
        print("This Takes You Back Out the Dungeon...") #inform player of choice being made
        time.sleep(2) #sleep to wait and space out code
        DungeonExit = input("Are You Sure You Want To Exit?\n[Yes] or [No]\n> ") #asking for confirmation
        if DungeonExit in Player.Yes: #if player says yes
            self.DungeonEntrance() #exit the dungeon
        elif DungeonExit in Player.No: #if player says no
            self.Room1() #go back to the centre of the room
        else: #if neither
            print("Please Choose a Valid Response...") #inform of poor choice
            self.Room1_South() #run the options again

##A Function to Call Room 2 in the Game Class
    def Room2(self):
        print('You Enter the Room, There is a Desk in the Centre...\nYou Also Notice a Man in the Corner of the Room...') #setting the scene
        Room2Choice = input('What Would You Like to Do?\n[Look] or [Move] or [Bag] or [Statistics]\n> ') #asking player of choice to be made
        if Room2Choice in Player.Move: #if player chooses to move
            Room2Direction = input('How Would You Like to Move?...\n[East] or [West] or [South]\n> ') #show movement options and receive answer
            if Room2Direction in Player.East: #if choice in east
                print('This Takes You to a Desk...') #go to desk, set scene
                answer = input('Would You Like to Go There?\n[Yes] or [No]\n> ') #ask player for confirmation
                if answer in Player.Yes: #if yes
                    self.Room2Desk() #go to the desk
                elif answer in Player.No: #if no
                    self.Room2() #go back to the start of the room
                else: #if neither
                    print('Please Choose a Valid Option...') #inform of poor choice
                    self.Room2() #start room again
        elif Room2Choice in Player.Look: #if player chooses look
            print('You Notice the Man in the Corner again, and Something Glistening in the Corner...') #look around the room
            if 'Key' not in Player.Inventory: #if no key in inventory
                print('You Notice the Man Trying to Get Your Attention...') #notice NPC
                ManChoice = input('Do You Wish to Approach Him?\n[Yes] or [No]\n> ') #ask player of choice
                if ManChoice in Player.Yes: #if player sayes yes
                    NPC.NPC() #run the NPC interaction
                elif ManChoice in Player.No: #if player says no
                    print('You Choose to Go Back Into the Room Entrance...') #inform player of choice
                    self.Room2() #run the room again
                else: #if neither
                    print('Please Choose a Valid Option...') #inform of poor choice
                    self.Room2() #
            else: #if none
                print('You See Nothin You Haven\'t Seen Already...') #inform player they've done everything
                time.sleep(2) #wait 2 seconds
        elif Room2Choice in Player.Bag: #if choice is bag
            Player.PlayerBag() #display bag
            self.Room2() #start the options again
        elif Room2Choice in Player.Statistics: #if choice is to see stats
            Player.TotalStatistics() #display the stats
            self.Room2() #start the choices again
        else: #if none
            print('Please Choose A Valid Option...') #inform of poor option choice
            self.Room2() #start options again

##The Desk within Room 2
    def Room2Desk(self):
        def Room2DeskChoice():#nested desk choice function
            Choice = input('What Would You Like to Do?\n[Look] or [Bag] or [Statistics]or Return\n> ') #desk options
            if Choice in Player.Look: #if player chooses to look
                pass
            elif Choice in Player.Bag: #if player chooses to view bag
                Player.PlayerBag() #display bag
                Room2DeskChoice() #start desk choice again
            elif Choice in Player.Statistics: #if player chooses to view stats
                Player.TotalStatistics() #display stats
                Room2DeskChoice() #run options again
            elif Choice in Player.Return: #if players chooses to return
                print('You Chose to Return...') #inform player of choice
                time.sleep(2) # wait 2 seconds
                self.Room2() #Go back to the start of the room
            else: #if no choices
                print('Please Choose A Valid Option...') #inform of poor choice
                Room2DeskChoice() #run choices again
        
        print('You Approach the Desk...') #setting the scene
        time.sleep(2) #sleep to wait and space out code
        print('You Notice a Number of Things on the Desk... But There Aren\'t Very Many Valuables...') #information on items
        Room2DeskChoice() #desk choice

##A Function to Call Room 3 Within the Game Class
    def Room3(self):
        def Room3Choice(): #nested function for choice in room 3
            answer = input('What Would You Like to Do?\n[Open] or [Look] or [Move] or [Bag] or [Statistics]\n> ') #player decisions
            if answer in Player.Open: #if player chooses to open chest
                self.Room3Chest() #run the chest function
            elif answer in Player.Move: #if player chooses to move
                Room1 = input('You Can Only Return... Are You Sure?\n[Yes] or [No]') #inform of directions available and confirm
                if Room1 in Player.Yes: #if yes
                    self.Room1() #go back to the other room
                elif Room1 in Player.No: #if no
                    Room3Choice() #start the choice again
                else: #if neither
                    print('Please Choose a Valid Option...') #inform of poor choice
                    time.sleep(2) #sleep to wait and space out code
                    Room3Choice() #run the options again
            elif answer in Player.Bag: #if choice player bag
                Player.PlayerBag() #display player bag
                Room3Choice() #run choices again
            elif answer in Player.Statistics: #if choice stats
                Player.TotalStatistics() #display player stats
                Room3Choice() #run options again
            else: #if none of the above
                print('Please Choose A Valid Option...') #inform of poor choice
                Room3Choice() #run options again

        print('You Enter the Eerie Room...') #settings the scene
        time.sleep(2) #sleep to wait and space out code
        print('It is Mostly Empty, There\'s a Small Light Shining Through...') #fuelling the imagination
        time.sleep(2) #sleep to wait and space out code
        print('In the Husk of the Light, You Notice Something...') #teeing up for reveal
        time.sleep(2) #sleep to wait and space out code
        print('You Notice a Chest...') #chest reveal
        time.sleep(2) #sleep to wait and space out code
        Room3Choice() #run the available options

##The Chest within Room 3
    def Room3Chest(self):
        def ChestChoice(): #nested choice function
            print('The Chest is Guarded with an Ancient Lock...') #information on the chest
            time.sleep(2) #sleep to wait and space out code
            print('You Must Unscramble the Word to Gain Access to What Lays Inside...') #information on the challenge
            time.sleep(2) #sleep to wait and space out code
            Open = input('Do You Wish to Attempt?\n[Yes] or [No]\n> ') #giving the player the option
            if Open in Player.Yes: #if the player chooses yes
                print('Hint: It\s One of Many Ancient Civilizations...') #display a hint
                time.sleep(2) #sleep to wait and space out code
                self.ChestRNG() #run the random scrambled word
            elif Open in Player.No: #if the player says no
                print('The Ancient Spirits Blow You Away!') #end the game in an interesting way
                time.sleep(2) #sleep to wait and space out code
                print('You\'re Blown Out the Dungeon, and Knock Yourself Out on Landing...') #add some spice
                time.sleep(2) #sleep to wait and space out code
                print('You Wake Up and There\'s No Dungeon in Sight, It Was All A Dream...') #crazy plot twists
                time.sleep(4) #sleep to wait and space out code
                print('Or Was It...') #get ready to start again from the beginning
                self.GameEnd() #run the game end function
            else: #if none of the above options
                print('Please Choose a Valid Choice...') #inform of poor choice
                ChestChoice() #run the choices again
        
        ChestChoice() #start the chest choice on function start

##Word Scramble for Chest Unlocking
    def ChestRNG(self):
        def ScrambleChoice(): #player input for challenge
            answer = input('What\'s Your Guess?\nYou Can Also Return By Typing\n[Return]\n> ') #asking for their guess
            answer.lower() #converting the string to all lower case to match list element
            if answer == self.Word: #if the answer is the same as the random word
                print('You Correctly Unlocked the Chest!!!') #inform the player of the success
                time.sleep(2) #sleep to wait and space out code
                Player.Inventory.append('Crown') #add item to inventory
                Player.Inventory.append('Crystal Skull') #add item to inventory
                Player.Inventory.append('Hoverboard') #add item to inventory
                Player.CoinCollect(random.randrange(500, 2000)) #collect random number of coins
                Player.PlayerBag() #display player bag
                time.sleep(2) #sleep to wait and space out code
                Player.ArmourCollect('Diamond Helmet', 100) #put on armour and add strength
                Player.ArmourCollect('Obsidian Chest Plate', 248) #put on armour and add strength
                Player.ArmourCollect('Marty McFly\'s Nike Mags', 5) #easter egg
                time.sleep(2) #wait 2 seconds
                print('You Completed the Dungeon!') #inform the player of completion
                time.sleep(2) #sleep to wait and space out code
                self.GameEnd() #run the game end script
            elif answer in Player.Return:
                print('The Ancient Spirits Blow You Away!') #game over
                time.sleep(2) #sleep to wait and space out code
                print('You\'re Blown Out the Dungeon, and Knock Yourself Out on Landing...') #a little dramatic flare
                time.sleep(2) #sleep to wait and space out code
                print('You Wake Up and There\'s No Dungeon in Sight, It Was All A Dream...') #add some spice
                time.sleep(4) #sleep to wait and space out code
                print('Or Was It...') #plot twist
                time.sleep(2) #sleep to wait and space out code
                self.GameEnd() #run the game end script
            else: #if noneof the above
                print('Not Quite, You\'re Nearly There!') #encourage the user
                ScrambleChoice() #run the choice again
            
        WordChoice = ['mayan', 'egyptian', 'roman', 'greek', 'aztec', 'incan', 'dinosaurs'] #choice of words for chest unlocking
        letters = [] #list to append individual letters to 
        self.Word = random.choice(WordChoice) #random word choice from list
        for letter in self.Word: #every letter in the word
            letters.append(letter) #append into a list
        random.shuffle(letters) #shuffle the letters to be random
        print(''.join(letters)) #join the letters together with no space to make it a string
        ScrambleChoice() #run the scrambled word answering for player

##A Selection of Code to Be Displayed at The End of the Game
    def GameEnd(self):
        print("Thanks for Playing...") #warm ending
        time.sleep(2) #sleep to wait and space out code
        print("See You Again Next Time!\n\n\n\n") #hopefully they will play again
        time.sleep(2) #sleep to wait and space out code
        print('Player: ' + self.PlayerName + ' Finished with the Following Items in Their Bag\n' + Player.PlayerBag()) #display items finished with in the current bag
        time.sleep(2) #sleep to wait and space out code
        print('Player: ' + self.PlayerName + ' Has Finished the Game With the Following Stats:') #inform stats are coming up
        time.sleep(2) #sleep to wait and space out code
        Player.TotalStatistics() #display ending stats
        time.sleep(5) #sleep to wait and space out code
        if 'Axolotl' in Player.Pet: #secret pet feature
            pass
        else: #if no secret pet
            pass #ignore
        time.sleep(45) #sleep to wait and space out code

##Initialising the Game Class        
if __name__ == '__main__':
    Game()