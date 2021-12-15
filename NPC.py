import time
import random

from Player import Player
import Game

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
            answer = input('What\'s Your Guess?\n> ')
            answer.lower()
            if answer == self.Word:
                print('You\'re Correct!')
                time.sleep(2)
                print('Here\'s the Key...')
                Player.Inventory.append('Key')
                Player.PlayerBag()
                print('Use it Wisely...')
                time.sleep(2)
                print('I\'m Sending You Back to the Other Room, but Come Back and Explore if You Want!')
                time.sleep(3)
                Game.Game.Room1(self)
            elif answer in Player.Return:
                print('That\'s Okay, I\'ll Still Be Here When You\'re Ready')
                Game.Game.Room2(self)
            else:
                print('Not Quite, You\'re Nearly There!')
                ScrambleChoice()
           
        
        print('You must Unscramble the Word Given to You...\nYou can quit at anytime by typing [Return]')
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

if __name__ == '__main__':
    NPC()