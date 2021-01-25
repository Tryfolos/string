#This script takes handles the code that the user enters in different ways.


#importing things.
import os
import time
import sys


#Variable that determines what mode the main loop at the end will run in.
mode = False

#Function for clearing the terminal.
def clear():
    os.system('cls||clear')


#Clearing terminal
clear()

#First print. Makes some important statements. Explains to the user how to quit.
print("Important information:\n\nIf you enter one of the following words at any point, the program will close immediately:\n\nExit\n\nexit\n\nQuit\n\nquit\n\nStop\n\nstop\n\nIf you would like to continue, simply enter the word \"Continue\" or \"continue\"\n")

#Taking input from user.
text = input("Enter string here: ")

#Checking if the user wants to quit.
if text == "Exit":
    run = False
if text == "exit":
    run = False

if text == "Quit":
    run = False
if text == "quit":
    run = False

if text == "Stop":
    run = False
if text == "stop":
    run = False

#If the user entered something irrelevant he/she will be prompted again.
#If the user enteres continue the next part will enter.
if text == "continue" or text == "Continue":
    clear()
else:
    if text == "Exit":
        sys.exit()
    if text == "exit":
        sys.exit()

    if text == "Quit":
        sys.exit()
    if text == "quit":
        sys.exit()

    if text == "Stop":
        sys.exit()
    if text == "stop":
        sys.exit()
    while True:
        text = input("Enter string here: ")
        if text == "Exit":
            sys.exit()
        if text == "exit":
            sys.exit()

        if text == "Quit":
            sys.exit()
        if text == "quit":
            sys.exit()

        if text == "Stop":
            sys.exit()
        if text == "stop":
            sys.exit()

        if text == "continue":
            clear()
            break
        if text == "Continue":
            clear()
            break

clear()

#Asking the user what they would like to do with the string they will enter later.
print("What would you like to do?\n\nEnter \"1\" if you want to remove all spaces from your string of choice\n\nEnter \"2\" if you want to replace all spaces with \"FUCK\"\n")

text = input("Enter string here: ")

if text == "Exit":
    sys.exit()
if text == "exit":
    sys.exit()

if text == "Quit":
    sys.exit()
if text == "quit":
    sys.exit()

if text == "Stop":
    sys.exit()
if text == "stop":
    sys.exit()

if text == "1":
    clear()
    mode = 1
if text == "2":
    clear()
    mode = 2

while mode == False:
    text = input("Enter string here: ")
    if text == "Exit":
        sys.exit()
    if text == "exit":
        sys.exit()

    if text == "Quit":
        sys.exit()
    if text == "quit":
        sys.exit()

    if text == "Stop":
        sys.exit()
    if text == "stop":
        sys.exit()
    if text == "1":
        mode = 1
        break
    if text == "2":
        mode = 2
        break

clear()
if mode == 1:
    print("You have entered \"Space remover\" mode")
    time.sleep(3)
if mode == 2:
    print("You have entered \"FUCK\" mode")
    time.sleep(3)
clear()

#Main program loop.
while True:
    if mode == 1:
        text = input("Enter string here: ")

        if text == "Exit":
            sys.exit()
        if text == "exit":
            sys.exit()

        if text == "Quit":
            sys.exit()
        if text == "quit":
            sys.exit()

        if text == "Stop":
            sys.exit()
        if text == "stop":
            sys.exit()

        thing = text.replace(" ", "")

        print(f"\nThis is what your string looks like without spaces: \n\n{thing}")
        time.sleep(5)
        clear()

    if mode == 2:
        text = input("Enter string here: ")

        if text == "Exit":
            sys.exit()
        if text == "exit":
            sys.exit()

        if text == "Quit":
            sys.exit()
        if text == "quit":
            sys.exit()

        if text == "Stop":
            sys.exit()
        if text == "stop":
            sys.exit()

        thing = text.replace(" ", " FUCK ")

        print(f"\nThis is what your string looks like with FUCK instead of spaces: \n\n{thing}")
        time.sleep(6)
        clear()
