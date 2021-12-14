from os import write
import tkinter as tk
from tkinter import Label, ttk
from tkinter.constants import BOTH, LEFT

from Game import Game

class Login():

    def __init__(self):
        self.Window()

    def Window(self):
        self.App = tk.Tk()
        self.App.title('Text Dungeon | Login')
        self.App.geometry('1040x510')

        CreateFrame = ttk.Frame(self.App)
        LoginFrame = ttk.Frame(self.App)

        CreateFrame.pack(side='left', fill='both', expand=True)
        LoginFrame.pack(side='right', fill='both', expand=True)

        UserLabel = tk.Label(CreateFrame, text='Please Choose a Username')
        self.CreateUsername = tk.Entry(CreateFrame, width=30)
        PassLabel = tk.Label(CreateFrame, text='Please Choose a Password')
        self.CreatePassword = tk.Entry(CreateFrame, width=30, show='*')
        ConfirmLabel = tk.Label(CreateFrame, text='Please Confirm Password')
        self.ConfirmUsername = tk.Entry(CreateFrame, width=30, show='*')
        Confirm = tk.Button(CreateFrame, text='Confirm', command=self.RunCreate)
        self.CreateError = tk.Label(CreateFrame, text=' ')

        UsernameLabel = tk.Label(LoginFrame, text='Enter Username')
        self.Username = tk.Entry(LoginFrame, width=30)
        PasswordLabel = tk.Label(LoginFrame, text='Enter Password')
        self.Password = tk.Entry(LoginFrame, width=30, show='*')
        Submit = tk.Button(LoginFrame, text='Login', command=self.RunLogin)
        self.ErrorLabel = tk.Label(LoginFrame, text=" ")

        UserLabel.grid(row=0, column=0)
        self.CreateUsername.grid(row=1, column=0)
        PassLabel.grid(row=2, column=0)
        self.CreatePassword.grid(row=3, column=0)
        ConfirmLabel.grid(row=4, column=0)
        self.ConfirmUsername.grid(row=5, column=0)
        Confirm.grid(row=6, column=0)
        self.CreateError.grid(row=7, column=0)

        UsernameLabel.grid(row=0, column=0)
        self.Username.grid(row=1, column=0)
        PasswordLabel.grid(row=2, column=0)
        self.Password.grid(row=3, column=0)
        Submit.grid(row=4, column=0)
        self.ErrorLabel.grid(row=5, column=0)

        self.App.mainloop()

    def RunLogin(self):
        self.UserID = self.Username.get()
        self.UserPass = self.Password.get()
        UserFile = self.UserID + '.txt'

        try: 
            with open('G:\My Drive\Programming Concepts\Text Dungeon\\' + UserFile, "r") as File:
                for line in File:
                    usercheck, passcheck = line.split(',')
            if self.UserID == usercheck:
                if self.UserPass == passcheck:
                    print("Success")
                    self.ErrorLabel.config(text='Success')
                    self.App.destroy()
                    Game()
                else:
                    print("Wrong Password")
                    self.ErrorLabel.config(text='Incorrect Password')
            else:
                print("User ID Not Found")
                self.ErrorLabel.config(text='Incorrect Username')
        except:
            print('User Not Found')
            self.ErrorLabel.config(text='User Not Found')

    def RunCreate(self):
        self.UserID = self.CreateUsername.get()
        self.CreatePass = self.CreatePassword.get()
        self.ConfirmPass = self.ConfirmUsername.get()
        print(self.UserID)
        print(self.CreatePass)
        print(self.ConfirmPass)
        UserFile = self.UserID + '.txt'

        try: 
            with open('G:\My Drive\Programming Concepts\Text Dungeon\\' + UserFile, "w") as File:
                if self.CreatePass == self.ConfirmPass:
                    print("Success")
                    File.write(self.UserID + ',' + self.CreatePass)
                    self.CreateError.config(text='User Created!')
                    Game()
                else:
                    print("Passwords Don't Match")
                    self.CreateError.config(text='Passwords Don\'t Match')
        except:
            print('Failed to Create User')

if __name__ == '__main__':
    Login()