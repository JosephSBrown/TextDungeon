##import of existing modules
import time

##import of classes for purpose of the game
import Game

##Player Class
class Player():
##A Collection of Variable Lists to Ease Player Selection and to Minimise Code Length in If Statements.
    North = ['North', 'north', 'N', 'n', 'NORTH'] #Command List Moving North
    South = ['South', 'south', 'S', 's', 'SOUTH'] #Command List Moving South
    East = ['East', 'east', 'E', 'e', 'EAST'] #Command List Moving East
    West = ['West', 'west', 'W', 'w', 'WEST'] #Command List Moving West
    Yes = ['Yes', 'yes', 'Y', 'y', 'YES'] #Command List Saying Yes
    No = ['No', 'no', 'N', 'n', 'NO'] #Command List Saying No
    Use = ['Use', 'use', 'U', 'u', 'USE'] #Command List Saying Use
    Move = ['Move', 'move', 'M', 'm', 'MOVE'] #Command List Saying Move
    Look = ['Look', 'look', 'L', 'l', 'LOOK'] #Command List Saying Look
    Return = ['Return', 'return', 'R', 'r', 'RETURN'] #Command List Saying Return
    Collect = ['Collect', 'collect', 'C', 'c', 'COLLECT'] #Command List Saying Collect
    End = ['End', 'end', 'E', 'e', 'END'] #Command List Saying End
    Key = ['Key', 'key', 'K', 'k', 'KEY'] #Command List Saying Key
    Bag = ['Bag', 'bag', 'b', 'B', 'BAG'] #Command List Saying Bag
    Statistics = ['Statistics', 'statistics', 'S', 's', 'STATISTICS'] #Command List Saying Statistics
    ArmourChoice = ['Armour', 'armour', 'a', 'A', 'ARMOUR'] #Command List Saying Armour
    CoinsChoice = ['Coins', 'coins', 'c', 'C', 'COINS'] #Command List Saying Coins
    Open = ['Open', 'open', 'O', 'o', 'OPEN'] #Command List Saying Open

##Players Overall Stats... Including Coin Total, Health Total and Armour Total
    Coins = 0 #Overall Coin Total Variable
    Health = 100 #Overall Health Total Variable
    Armour = 0 #Overall Armour Total Variable

##Player Inventory
    Inventory = ['Snack'] #Players Inventory (Also Known as Player Bag)
    ArmourSet = [] #List Containing Players Armour Collected Through the Game
    Pet = [] #Secret Feature for Collecting Pets
    RareEncounter = ['Axolotl']

##A function to Print the Players Total Statistics
    def TotalStatistics():
        print('\n\n\n#### Player Stats ####') 
        print('####################')
        print("Coins: " + str(Player.Coins)) #Displays Player Coins Total
        print("Health: " + str(Player.Health)) #Displays Players Health Total
        print("Armour: " + str(Player.Armour)) #Displays Player Armour Total
        print("Player Bag: " + str(Player.Inventory)) #Shows Current Inventory
        print('Armour Set: ' + str(Player.ArmourSet)) #Shows Current Armour
        print('\n\n\n')

##A Function to Print the Players Bag at Any Time the Function is Called
    def PlayerBag():
        print('\n\n\n#### Player Bag ####')
        print('##################')
        print(str(Player.Inventory) + '\n\n\n') #Shows Current Inventory

##A Function to Allow the Player to Collect Armour, Used Cross Class To prevent Lenghty Game Code
    def ArmourCollect(Type, Weight):
        Player.ArmourSet.append(Type) #Appends Armour Type to the Armour List
        Player.Armour += Weight #Adds Armour Strength to the Armour Variable
        print('Your Armour is Now: ' + str(Player.Armour)) #Displays the Current Armour Variable

##A Function to Allow Players to Collect Items Into Their Inventory, Used Cross Class to prevent Lengthy Game Code
    def ItemCollect(Type):
        Player.Inventory.append(Type) #Appends Items to the Players Bag
        print(Player.PlayerBag()) #Displays Player Bag Function

##A Function Used to Collect Coins to Add to Their Score, Used Cross Class to Prevent Lengthy Game
    def CoinCollect(Amount):
        Player.Coins += Amount #Adds Specified Number of Coins
        print('You Now Have ' + str(Player.Coins) + ' Coins...') #Displays Coins

##Shows Current Pets, Only Used In End Game to Remain Secret Feature
    def PetCheck():
        print('\n\n\n#### Pets ####')
        print('##################')
        print(str(Player.Pet) + '\n\n\n') #Displays Current Pets

#Secret Pet Encounter in Room2 Desk Drawer
    def RarePetEncounter():
        if 'Axolotl' in Player.RareEncounter: #only run following code if don't have axolotl
            Brave = input('Do You Dare Open the Draw?\n[Yes] or [No]\n> ') #Player Input to Enter Drawer
            if Brave in Player.Yes: #If Statement for Yes Select
                print('You See Something Small Moving Around in the Drawer') #Scene Setting
                time.sleep(2) #Sleep Feature, adds Suspense
                Arfa = input('It\'s a Small Axolotl, Would You Like to Take Him?\n[Yes] or [No]\n> ') #input to collect pet
                if Arfa in Player.Yes: #if statement for pet collection
                    Player.Pet.append('Axolotl') #appends axolotl to the Pet List
                    print('You Acquired an Axolotol as a Pet!') #Informs Player of Action that happened
                elif Arfa in Player.No: #If Player Chooses No and irs in list
                    print('You Chose Not to Collect the Axolotl...') #informing player of choice
                    time.sleep(2) #sleep feature, adds suspense
                    print('You\'re returning to the desk...') #informing player of next move
                    Game.Game.Room2Desk() #returning to desk
            elif Brave in Player.No: #if statement for not checking drawer
                print('You Chose Not to Check...') #informing user of choice
                Game.Game.Room2Desk() #Back to Desk
            else: #final else
                print('Please Choose a Valid Choice...') #informing of invalid choice
                Player.RarePetEncounter() #runs section of code again from choice
        else: #already have axolotl so ignore if statement
            print('Maybe You Were Just Seeing Things...') #inform player choice means nothing
            Game.Game.Room2Desk() #back to the desk