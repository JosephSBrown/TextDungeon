import time
import random

from Player import Player
from Game import Game

class NPC():

    def __init__(self):
        self.InitialInteraction()

    def InitialInteraction(self):
        print('Hey!!!')
        time.sleep(2)
        print('Hey!!!')
        time.sleep(2)
        self.KeyInteraction()

    def KeyInteraction(self):
        question = input('Have You Tried to get into the Northern Room?\n[Yes] or [No]\n> ')
        if question in Player.Yes:
            print('Ah So You\'re Aware You Require the Key to Get in...')
            self.KeyReveal()
        elif question in Player.No:
            print('Ah Then I have some Information for you!')
            time.sleep(2)
            print('You Require the Key to get into the Northern Most Room of the Dungeon!')
            time.sleep(2)
            print('But Worry Not...')
            self.KeyReveal()
        else:
            print('Please Choose a Valid Option...')
            self.KeyInteraction()

    def KeyReveal(self):
        print('I am the one who has the key right now...')
        time.sleep(2)
        print('But I will Only Give it to You on One Condition...')
        time.sleep(2)
        print('If You Answer My Question...')
        time.sleep(2)
        Q = input('Are You Up for the Challenge?\n[Yes] or [No]\n> ')
        if Q in Player.Yes:
            self.KeyRiddle()
        elif Q in Player.No:
            print('That\'s Unfortunate...')
            time.sleep(2)
            print('Have Fun Trying to get into the North Room Without It!!!')
            time.sleep(2)
            print('Off to the Start of the room again for you!')
            Game.Room2()
        else:
            print('Please Choose a Valid Option...')
            self.KeyReveal()

    def KeyRiddle(self):
        def ScrambleChoice():        
            if self.Word == 'treasure':
                answer = input('What\'s Your Guess?\n> ')
                if answer == 'treasure':
                    print('You\'re Correct!')
                    time.sleep(2)
                    print('Here\'s the Key...')
                    Player.Inventory.append('Key')
                elif answer == 'exit':
                    print('That\'s Okay, I\'ll Still Be Here When You\'re Ready')
                    Game.Room2()
                else:
                    print('Not Quite, You\'re Nearly There!')
                    ScrambleChoice()
        
        print('You must Unscramble the Word Given to You...')
        time.sleep(2)
        print('Here\'s Your Word...')
        WordChoice = ['treasure', 'winner', 'python', 'dungeon']
        letters = []
        self.Word = random.choice(WordChoice)
        for letter in self.Word:
            letters.append(letter)
        random.shuffle(letters)
        print(''.join(letters))
        ScrambleChoice()