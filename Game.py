import time
import random

from Player import Player
import NPC

#--Game Class-----------------------------------------------------------------------------------------------
class Game():

    Username = []
    Room1Item = ['Coins', 'Iron Helmet']
    Room2Item = ['Iron Sword']

    def __init__(self):
        self.GameStart()

    def GameStart(self):
        print("Welcome to Text Dungeon!\nThanks For Playing!")
        time.sleep(2)
        print("To Complete the Game Please Answer the Questions\nMake Sure This is With Valid Choices!")
        time.sleep(2)
        print("Your Choices Will Appear Like This: [Yes] or [No]")
        time.sleep(2)
        AskName = input('Would You Like to Use ' + Game.Username[0] + ' As Your Adventuring Name?\n[Yes] or [No]\n> ')
        if AskName in Player.Yes:
            self.PlayerName = Game.Username[0]
        elif AskName in Player.No:
            self.PlayerName = input('Would You Mind Giving Us Your Name For the Adventure?\n[This Can Be Any Name/Word!]\n> ')
        else:
            print('It Was a Yes or No Answer, So I assume that\'s a No...')
            self.PlayerName = Game.Username[0]
            return
        time.sleep(1)
        print('Well...' + self.PlayerName + '! That\'s a Wonderful Name... Let\'s Begin...')
        time.sleep(2)
        self.SceneSetting()

    def SceneSetting(self):
        print("You Awaken in a Small Forest Without Much to See Around You...")
        time.sleep(2)
        print("The Only Thing Clear to You for Miles Around is a Small Dungeon Ahead...")
        time.sleep(2)
        self.DungeonEntrance()

    def DungeonEntrance(self):
        def Entrance():          
            EntranceQ = input("The Time Comes...\nDo You Dare Enter?\n[Yes] or [No]\n> ")
            if EntranceQ in Player.Yes:
                self.Room1()
            elif EntranceQ in Player.No:
                self.GameEnd()
            else:
                print('Please Choose a Valid Option...')
                time.sleep(2)
        
        print("The Dungeon Looks Untouched but You Hear Hallowed Voices From Inside...\nYou Wonder If You Dare to Enter...")
        time.sleep(2)
        Entrance()

    def Room1(self):
        def RoomChoice():
            Room1FirstChoice = input("What Would You Like to Do?\n[Look] or [Move] or [Bag] or [Statistics]\n> ")
            if Room1FirstChoice in Player.Move:
                Room1DirectionChoice()
            elif Room1FirstChoice in Player.Look:
                print("You Look Around...\nYou See the Following Items...")
                print(Game.Room1Item)
                time.sleep(2)
                ItemChoice = input('What Would You Like to Do?\n[Collect] or [Return]\n> ')
                if ItemChoice in Player.Collect:
                    Item = input('What Would You Like to Collect?\n[Coins] or [Armour]\n> ')
                    if Item in Player.CoinsChoice:
                        if 'Coins' in Game.Room1Item:
                            Game.Room1Item.remove('Coins')
                            Player.CoinCollect(random.randrange(0, 100))
                        else:
                            print('Please Choose a Valid Option...')
                            RoomChoice()
                    elif Item in Player.ArmourChoice:
                        if 'Iron Helmet' in Game.Room1Item:
                            Game.Room1Item.remove('Iron Helmet')
                            Player.ArmourCollect('Iron Helmet', 10)
                    else:
                        print('Please Choose a Valid Option...')
                        RoomChoice()
                elif ItemChoice in Player.Return:
                    print('You Chose to Return...')
                    time.sleep(2)
                    RoomChoice()
                else:
                    print('Please Choose a Valid Option...')
                    RoomChoice()
                time.sleep(2)
                RoomChoice()
            elif Room1FirstChoice in Player.Bag:
                Player.PlayerBag()
                RoomChoice()
            elif Room1FirstChoice in Player.Statistics:
                Player.TotalStatistics()
                RoomChoice()
            else:
                print('Please Choose a Valid Option...')
                RoomChoice()

        def Room1DirectionChoice():
            Room1Choice = input("Which Direction Would You Like to Move?\n[North] or [South] or [West]\n> ")
            if Room1Choice in Player.West:
                self.Room1_West()
            elif Room1Choice in Player.North:
                self.Room1_North()
            elif Room1Choice in Player.South:
                self.Room1_South()
            else:
                print("Please Choose a Valid Option...")
                Room1DirectionChoice()
        
        print("You are Greeted by a Room...")
        time.sleep(2)
        print("The Room is Tiled with 2 Doors...")
        time.sleep(2)
        print("Walking to the North takes you to a Door...")
        time.sleep(2)
        print("Heading West Takes You to Another Door...")
        time.sleep(2)
        print("And Heading South Takes You Back Out the Dungeon...")
        time.sleep(2)
        RoomChoice()

    def Room1_North(self):
        def Room1NorthChoice():
            NorthDoorChoice = input('What Would You Like to Do?\n[Use] or [Return]\n> ')
            if NorthDoorChoice in Player.Use:
                print('You Chose to Use...')
                time.sleep(2)
                print('Your Bag Currently Contains:\n' + Player.PlayerBag())
                NorthDoorUse = input('What Would You Like to Use?\n> ')
                if NorthDoorUse in Player.Key:
                    if 'Key' in Player.Inventory:
                        Player.Inventory.remove('Key')
                        print("You Used the Key!")
                        time.sleep(2)
                        Player.PlayerBag()
                        time.sleep(2)
                        self.Room3()
                    elif 'Key' not in Player.Inventory:
                        print('You Do Not Have The Key and Must Find It First...\n')
                        time.sleep(2)
                        print('You Return to the Centre of the Room...')
                        self.Room1()
            elif NorthDoorChoice in Player.Return:
                self.Room1()
            else:
                print('Please Choose a Valid Option...')
                Room1NorthChoice()

        print('You Approach the Northern Door...')
        time.sleep(2)
        Room1NorthChoice()

    def Room1_West(self):
        def Room1DoorChoice():
            DoorChoice = input("What Would You Like to Do?\n[Use] or [Return]\n> ")
            if DoorChoice in Player.Use:
                print('You Look in Your Bag... \n')
                Player.PlayerBag()
                Use = input('What Would You Like to Use?\n')
                Player.PlayerBag()
                print('There Was No Need to Use Any Items As the Door is Unlocked Already...')
                time.sleep(2)
                KeyUse = input('Would You Like to Enter the Room?\n[Yes] or [No]\n> ')
                if KeyUse in Player.Yes:
                    self.Room2()
                elif KeyUse in Player.No:
                    print('You Go Back to the Centre of Room...')
                    time.sleep(2)
                    self.Room1()
                else:
                    print("Please Choose a Valid Option...")
                    Room1DoorChoice()
            elif DoorChoice in Player.Return:
                Room1ReturnChoice = input('Are You Sure?\n[Yes] or [No]\n> ')
                if Room1ReturnChoice in Player.Yes:
                    self.Room1()
                elif Room1ReturnChoice in Player.No:
                    self.Room1_West
                else:
                    print('Please Choose a Valid Choice...')
                    Room1DoorChoice()
            else:
                print("Please Choose a Valid Option...")
                time.sleep(2)
                Room1DoorChoice()
        
        print("You Are Met By a Door...")
        time.sleep(2)
        Room1DoorChoice()

##A Function to Open Room 1 South
    def Room1_South(self):
        print("This Takes You Back Out the Dungeon...")
        time.sleep(2)
        DungeonExit = input("Are You Sure You Want To Exit?\n[Yes] or [No]\n> ")
        if DungeonExit in Player.Yes:
            self.DungeonEntrance()
        elif DungeonExit in Player.No:
            self.Room1()
        else:
            print("Please Choose a Valid Response...")
            self.Room1_South()

##A Function to Call Room 2 in the Game Class
    def Room2(self):
        print('You Enter the Room, There is a Desk in the Centre...\nYou Also Notice a Man in the Corner of the Room...')
        Room2Choice = input('What Would You Like to Do?\n[Look] or [Move] or [Bag] or [Statistics]\n> ')
        if Room2Choice in Player.Move:
            Room2Direction = input('How Would You Like to Move?...\n[East] or [West] or [South]\n> ')
            if Room2Direction in Player.East:
                print('This Takes You to a Desk...')
                answer = input('Would You Like to Go There?\n[Yes] or [No]\n> ')
                if answer in Player.Yes:
                    self.Room2Desk()
                elif answer in Player.No:
                    self.Room2()
                else:
                    print('Please Choose a Valid Option...')
                    self.Room2()
        elif Room2Choice in Player.Look:
            print('You Notice the Man in the Corner again, and Something Glistening in the Corner...')
            if 'Key' not in Player.Inventory:
                print('You Notice the Man Trying to Get Your Attention...')
                ManChoice = input('Do You Wish to Approach Him?\n[Yes] or [No]\n> ')
                if ManChoice in Player.Yes:
                    NPC.NPC()
                elif ManChoice in Player.No:
                    print('You Choose to Go Back Into the Room Entrance...')
                    self.Room2()
                else:
                    print('Please Choose a Valid Option...')
                    self.Room2()
            elif 'Iron Sword' not in Player.ArmourSet:
                print('')
            else:
                print('You See Nothin You Haven\'t Seen Already...')
                time.sleep(2)
        elif Room2Choice in Player.Bag:
            Player.PlayerBag()
            self.Room2()
        elif Room2Choice in Player.Statistics:
            Player.TotalStatistics()
            self.Room2()
        else:
            print('Please Choose A Valid Option...')
            self.Room2()

    def Room2Desk(self):
        def Room2DeskChoice():
            Choice = input('What Would You Like to Do?\n[Look] or [Bag] or [Statistics]or Return\n> ')
            if Choice in Player.Look:
                pass
            elif Choice in Player.Bag:
                Player.PlayerBag()
                Room2DeskChoice()
            elif Choice in Player.Statistics:
                Player.TotalStatistics()
                Room2DeskChoice()
            elif Choice in Player.Return:
                Room2DeskChoice()
            else:
                print('Please Choose A Valid Option...')
                Room2DeskChoice()
        
        print('You Approach the Desk...')
        time.sleep(2)
        print('You Notice a Number of Things on the Desk... But There Aren\'t Very Many Valuables...')
        Room2DeskChoice()

##A Function to Call Room 3 Within the Game Class
    def Room3(self):
        def Room3Choice():
            answer = input('What Would You Like to Do?\n[Open] or [Look] or [Move] or [Bag] or [Statistics]\n> ')
            if answer in Player.Open:
                self.Room3Chest()
            elif answer in Player.Move:
                Room1 = input('You Can Only Return... Are You Sure?\n[Yes] or [No]')
                if Room1 in Player.Yes:
                    self.Room1()
                elif Room1 in Player.No:
                    Room3Choice()
                else:
                    print('Please Choose a Valid Option... Returning to Original Choice')
                    time.sleep(2)
                    Room3Choice()
            elif answer in Player.Bag:
                Player.PlayerBag()
                Room3Choice()
            elif answer in Player.Statistics:
                Player.TotalStatistics()
                Room3Choice()
            else:
                print('Please Choose A Valid Option...')
                Room3Choice()

        print('You Enter the Eerie Room...')
        time.sleep(2)
        print('It is Mostly Empty, There\'s a Small Light Shining Through...')
        time.sleep(2)
        print('In the Husk of the Light, You Notice Something...')
        time.sleep(2)
        print('You Notice a Chest...')
        time.sleep(2)
        Room3Choice()

    def Room3Chest(self):
        pass

##A Selection of Code to Be Displayed at The End of the Game
    def GameEnd(self):
        print("Thanks for Playing...")
        time.sleep(2)
        print("See You Again Next Time!\n\n\n\n")
        time.sleep(2)
        print('Player: ' + self.PlayerName + ' Finished with the Following Items in Their Bag\n' + Player.PlayerBag())
        time.sleep(2)
        print('Player: ' + self.PlayerName + ' Has Finished the Game With the Following Stats:')
        time.sleep(2)
        Player.TotalStatistics()
        time.sleep(45)

##Initialising the Game Class        
if __name__ == '__main__':
    Game()

