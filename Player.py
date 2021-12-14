class Player():
##A Collection of Variable Lists to Ease Player Selection and to Minimise Code Length in If Statements.
    North = ['North', 'north', 'N', 'n', 'NORTH']
    South = ['South', 'south', 'S', 's', 'SOUTH']
    East = ['East', 'east', 'E', 'e', 'EAST']
    West = ['West', 'west', 'W', 'w', 'WEST']
    Yes = ['Yes', 'yes', 'Y', 'y', 'YES']
    No = ['No', 'no', 'N', 'n', 'NO']
    Use = ['Use', 'use', 'U', 'u', 'USE']
    Move = ['Move', 'move', 'M', 'm', 'MOVE']
    Look = ['Look', 'look', 'L', 'l', 'LOOK']
    Return = ['Return', 'return', 'R', 'r', 'RETURN']
    Collect = ['Collect', 'collect', 'C', 'c', 'COLLECT']
    End = ['End', 'end', 'E', 'e', 'END']
    Key = ['Key', 'key', 'K', 'k', 'KEY']
    Bag = ['Bag', 'bag', 'b', 'B', 'BAG']
    Statistics = ['Statistics', 'statistics', 'S', 's', 'STATISTICS']
    ArmourChoice = ['Armour', 'armour', 'a', 'A', 'ARMOUR']

##Players Overall Stats... Including Coin Total, Health Total and Armour Total
    Coins = 0
    Health = 100
    Armour = 0

##Player Inventory
    Inventory = ['Snack']
    ArmourSet = []

##A function to Print the Players Total Statistics
    def TotalStatistics():
        print('\n\n\n#### Player Stats ####')
        print('####################')
        print("Coins: " + str(Player.Coins))
        print("Health: " + str(Player.Health))
        print("Armour: " + str(Player.Armour))
        print("Player Bag: " + str(Player.Inventory))
        print('Armour Set: ' + str(Player.ArmourSet))
        print('\n\n\n')

##A Function to Print the Players Bag at Any Time the Function is Called
    def PlayerBag():
        print('\n\n\n#### Player Bag ####')
        print('##################')
        print(str(Player.Inventory) + '\n\n\n')

##A Function to Allow the Player to Collect Armour, Used Cross Class To prevent Lenghty Game Code
    def ArmourCollect(Type, Weight):
        Player.ArmourSet.append(Type)
        Player.Armour += Weight
        print('Your Armour is Now: ' + str(Player.Armour))

##A Function to Allow Players to Collect Items Into Their Inventory, Used Cross Class to prevent Lengthy Game Code
    def ItemCollect(Type):
        Player.Inventory.append(Type)
        print(Player.PlayerBag())

##A Function Used to Collect Coins to Add to Their Score, Used Cross Class to Prevent Lengthy Game
    def CoinCollect(Amount):
        Player.Coins += Amount
        print('You Now Have ' + str(Player.Coins) + 'Coins...')