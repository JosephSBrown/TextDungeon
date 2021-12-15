##importing standard modules
import time
import random

##importing classes for game purposes
from Player import Player
import Game

##NPC class
class NPC():

##initialising interaction
    def __init__(self):
        self.InitialInteraction()

##initial interaction
    def InitialInteraction(self):
        print('Hey!!!') #Getting Players Attention
        time.sleep(2) #Wait 2 seconds
        print('Hey!!!') #Players Attention
        time.sleep(2) #Wait 2 seconds
        self.KeyInteraction() #run next section

##interaction to inform about the key
    def KeyInteraction(self):
        question = input('Have You Tried to get into the Northern Room?\n[Yes] or [No]\n> ') #input for different interactions
        if question in Player.Yes: #if input answer is in yes commands
            print('Ah So You\'re Aware You Require the Key to Get in...') #teeing up for the next part
            self.KeyReveal() #run key reveal
        elif question in Player.No: #if answer is in no commands
            print('Ah Then I have some Information for you!') #inform player of information
            time.sleep(2) #wait 2 seconds
            print('You Require the Key to get into the Northern Most Room of the Dungeon!') #inform player of key requirement
            time.sleep(2) #wait 2 seconds
            print('But Worry Not...') #teeing up for next section
            self.KeyReveal() #run key reveal
        else: #if not one of the aforementioned
            print('Please Choose a Valid Option...') #inform player to choose a new option
            self.KeyInteraction() #run the choice again

##interaction to reveal he owns the key
    def KeyReveal(self):
        print('I am the one who has the key right now...') #the reveal
        time.sleep(2) #wait 2 seconds
        print('But I will Only Give it to You on One Condition...') #the twist
        time.sleep(2) #wait 2 seconds
        print('If You Answer My Question...') #lining up the challenge
        time.sleep(2) #wait 2 seconds
        Q = input('Are You Up for the Challenge?\n[Yes] or [No]\n> ') #ready to accept challenge
        if Q in Player.Yes: #if the player agrees
            self.KeyRiddle() #run anogram riddle
        elif Q in Player.No: #if player says no
            print('That\'s Unfortunate...') #NPC acts sad
            time.sleep(2) #wait 2 seconds
            print('Have Fun Trying to get into the North Room Without It!!!') #tease/taunt
            time.sleep(2) #wait 2 seconds
            print('Off to the Start of the room again for you!') #plot twist sent back to the start
            Game.Game.Room2() #thrown back into the start of room 2
        else: #if none of these options
            print('Please Choose a Valid Option...') #choose one mentioned
            self.KeyReveal() #run options again

##riddle for the player to get the key
    def KeyRiddle(self):
        def ScrambleChoice(): #nested function for player interaction
            answer = input('What\'s Your Guess?\n> ') #guess input
            answer.lower() #convert answer to all lowercase to match list
            if answer == self.Word: #if the guess is the same as the chosen word
                print('You\'re Correct!') #tell the player they succeeded
                time.sleep(2) #wait 2 seconds
                print('Here\'s the Key...') #inform the player 
                Player.Inventory.append('Key') #add the key to inventory
                Player.PlayerBag() #function to display player bag
                print('Use it Wisely...') #wary statement
                time.sleep(2) #wait 2 seconds
                print('I\'m Sending You Back to the Other Room, but Come Back and Explore if You Want!') #polite ending to interaction
                time.sleep(3) #wait 3 seconds
                Game.Game.Room1(self) #sent back to the first room
            elif answer in Player.Return: #if answer is in return command list
                print('That\'s Okay, I\'ll Still Be Here When You\'re Ready') #inform player he'll still be there
                Game.Game.Room2(self) #put them back in the start of room 2
            else: #if none of the other options
                print('Not Quite, You\'re Nearly There!') #encourage player to continue
                ScrambleChoice() #run nested function again
            
        print('You must Unscramble the Word Given to You...\nYou can quit at anytime by typing\n[Return]') #inform player of the challenge
        time.sleep(2) #wait 2 seconds
        print('Here\'s Your Word...') #inform player the word is coming
        WordChoice = ['treasure', 'winner', 'python', 'dungeon'] #list of word options
        letters = [] #create new list
        self.Word = random.choice(WordChoice) #random selection of words from list
        for letter in self.Word: #for every letter in the random word
            letters.append(letter) #add each letter into a new list as separate elements
        random.shuffle(letters) #shuffle to random letters
        print(''.join(letters)) #print the list and join without spaces
        ScrambleChoice() # run the guess interaction


if __name__ == '__main__':
    NPC()