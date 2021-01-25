#This script takes handles the code that the user enters in different ways.


#importing things.
import os
import time


#Boolean that determines if the main loop is going to run or if the program is going to stop.
run = True
runn = True
runnn = True

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
        runn = False
    if text == "exit":
        runn = False

    if text == "Quit":
        runn = False
    if text == "quit":
        runn = False

    if text == "Stop":
        runn = False
    if text == "stop":
        runn = False
    while runn == True:
        text = input("Enter string here: ")
        if text == "Exit":
            runn = False
        if text == "exit":
            runn = False

        if text == "Quit":
            runn = False
        if text == "quit":
            runn = False

        if text == "Stop":
            runn = False
        if text == "stop":
            runn = False

        if text == "continue":
            runn = False
            clear()
        if text == "Continue":
            runn = False
            clear()


clear()
runn = True
#Asking the user what they would like to do with the string they will enter later.
if run == True and runn == True:
    print("What would you like to do?\n\nEnter \"1\" if you want to remove all spaces from your string of choice\n")

    text = input("Enter string here: ")

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

    if text == "1":
        clear()
    else:
        while runnn == True:
            text = input("Enter string here: ")
            if text == "Exit":
                runnn = False
                run = False
            if text == "exit":
                runnn = False
                run = False

            if text == "Quit":
                runnn = False
                run = False
            if text == "quit":
                runnn = False
                run = False

            if text == "Stop":
                runnn = False
                run = False
            if text == "stop":
                runnn = False
                run = False
            if text == "1":
                runnn = False

clear()
print("You have entered \"space remover\" mode")
time.sleep(3)

#Main program loop.
while run == True:

    text = input("Enter string here: ")

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

    thing = text.replace(" ", "")

    print(thing)

