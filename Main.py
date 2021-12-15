##import of standard modules
from os import write
import tkinter as tk
from tkinter import Label, ttk
from tkinter.constants import BOTH, LEFT

##import of game related classes
from Game import Game

##login class
class Login():

##initialising window
    def __init__(self):
        self.Window()

##Login Window Function
    def Window(self):
        self.App = tk.Tk() #Creating Tkinter Window
        self.App.title('Text Dungeon | Login') #Setting Window Title
        self.App.geometry('1040x510') #Setting Window Resolution

        CreateFrame = ttk.Frame(self.App) #Creating frame for profile creation widgets
        LoginFrame = ttk.Frame(self.App) #Creating frame for login widgets

        CreateFrame.pack(side='left', fill='both', expand=True) #packing the frames
        LoginFrame.pack(side='right', fill='both', expand=True) #packing the frames

        UserLabel = tk.Label(CreateFrame, text='Please Choose a Username') #configuring create username label
        self.CreateUsername = tk.Entry(CreateFrame, width=30) #configuring create username entry box
        PassLabel = tk.Label(CreateFrame, text='Please Choose a Password') #configuring create password label
        self.CreatePassword = tk.Entry(CreateFrame, width=30, show='*') #configuring create password entry box
        ConfirmLabel = tk.Label(CreateFrame, text='Please Confirm Password') #configuring password confirmation label
        self.ConfirmUsername = tk.Entry(CreateFrame, width=30, show='*') #configuring password confirmation entrybox
        Confirm = tk.Button(CreateFrame, text='Confirm', command=self.RunCreate) #configuring confirm button
        self.CreateError = tk.Label(CreateFrame, text=" ") #configuring creation error message

        UsernameLabel = tk.Label(LoginFrame, text='Enter Username') #configuring login username label
        self.Username = tk.Entry(LoginFrame, width=30) #configuring login username entry box
        PasswordLabel = tk.Label(LoginFrame, text='Enter Password') #configuring login password label
        self.Password = tk.Entry(LoginFrame, width=30, show='*') #configuring password entry box
        Submit = tk.Button(LoginFrame, text='Login', command=self.RunLogin) #configuring submit button
        self.ErrorLabel = tk.Label(LoginFrame, text=" ") #configuring error label

        UserLabel.grid(row=0, column=0) #laying out user creation label
        self.CreateUsername.grid(row=1, column=0) #laying out user creation box
        PassLabel.grid(row=2, column=0) #laying out user password label
        self.CreatePassword.grid(row=3, column=0) #laying out user password box
        ConfirmLabel.grid(row=4, column=0) #laying out user password confirm label
        self.ConfirmUsername.grid(row=5, column=0) #laying out user password confirm box
        Confirm.grid(row=6, column=0) #laying out confirm button
        self.CreateError.grid(row=7, column=0) #laying out creation error label

        UsernameLabel.grid(row=0, column=0) #laying out user login label
        self.Username.grid(row=1, column=0) #laying out user login entry
        PasswordLabel.grid(row=2, column=0) #laying out user login password label
        self.Password.grid(row=3, column=0) #laying out user login password entry
        Submit.grid(row=4, column=0) #laying out submit button
        self.ErrorLabel.grid(row=5, column=0) #laying out login error message

        self.App.mainloop() #Activating Tkinter Window, putting it in loop

##Login Script for Existing Users
    def RunLogin(self):
        UserID = self.Username.get() #get username entry and set variable
        self.UserPass = self.Password.get() #get password entry and set variable
        UserFile = UserID + '.txt' #setting the variable for File Name

        try: #opening try loop
            with open('G:\My Drive\Programming Concepts\Text Dungeon\\' + UserFile, "r") as File: #opening file to read
                for line in File: #telling the program to look for something for every line in the file
                    usercheck, passcheck = line.split(',') #split the line at the comma in the files and set them to the 2 variables
            if UserID == usercheck: #if the entered username matches the username in the file
                if self.UserPass == passcheck: #if the entered password matches the one in the associated file
                    print("Success") #print success in the console
                    self.ErrorLabel.config(text='Success') #change the error message label to read success
                    self.App.destroy() #close the login application
                    Game.Username.append(UserID) #assign the username to a list in the Game class
                    Game() #initialise the game class
                else: #if none of the above password criteria are met
                    print("Wrong Password") #error message to console
                    self.ErrorLabel.config(text='Incorrect Password') #change error message to alert the user
            else: #if none of the above username criteria are met
                print("User ID Not Found") #print error message to console
                self.ErrorLabel.config(text='Incorrect Username') #change error label to alert user
        except: #if try fails
            print('User Not Found') #print error message to console
            self.ErrorLabel.config(text='User Not Found') #alert the user they need to make a profile

##Create Profile Script for New Users
    def RunCreate(self):
        UserID = self.CreateUsername.get() #get the creation username
        self.CreatePass = self.CreatePassword.get() #get the creation password
        self.ConfirmPass = self.ConfirmUsername.get() #get the confirmed creation password
        UserFile = UserID + '.txt' #set a variable to the expected file name

        try: #open try loop
            with open('G:\My Drive\Programming Concepts\Text Dungeon\\' + UserFile, "w") as File: #write to a file made with the variable file name
                if self.CreatePass == self.ConfirmPass: #if the passwords match
                    print("Success") #print success to console
                    File.write(UserID + ',' + self.CreatePass) #write the username and password to the specified file
                    self.CreateError.config(text='User Created!') #change error message to show user creation
                    self.App.destroy() #close login app
                    Game.Username.append(UserID) #append username to list in Game class
                    Game() #initialise game class
                else: #if passwords don't match
                    print("Passwords Don't Match") #print error message to console
                    self.CreateError.config(text='Passwords Don\'t Match') #change error message to alert user
        except: #if try fails
            print('Failed to Create User') #print error message to console

##Running Class on File Run
if __name__ == '__main__':
    Login()