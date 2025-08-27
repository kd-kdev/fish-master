# Version of Fish Master written using Python + Rich
import random
import time
import json
from collections import Counter
from threading import Timer
import rich
import curses
from rich.console import Console
from rich.panel import Panel


console = Console()
#fishDictionary = {}

listOfFish = []
id = 1

def welcome():
    return console.print(Panel.fit("Welcome to [bold blue]Fish Master[/bold blue], the CLI fishing game!"))
    
def mainMenu():
    command = int(input("""Please enter a number:
1. Start fishing
2. My fish
3. Shop
4. Help
5. Exit
6. generateFish (TEST)
7. printFishDict (TEST)
"""))
    response(command)


### Main menu
def response(command):
    match command:
        case 1:
            return fishingMinigame()
        case 2:
            return showFish()
        case 3:
            return showShop()
        case 4:
            return showHelp()
        case 5:
            return exitGame()
        case 6:
            return generateFish()
        case 7:
            return printFishDict()
        case _:
            return badInput()


### Main game

def fishGotAway():
    return print("the fish got away! :( ")

t = Timer(5, fishGotAway) # global timer for fish catch

def fishingMinigame():
    randomTime = random.randint(2,10)
    

    for i in range(randomTime):
        time.sleep(1)
        print(f"{i+1} bobbing...")


    t.start()
    pull = input("fish hooked!, you have 5 seconds to type 'pull' !\n")
    return caughtFish() if pull == "pull" else print("you fiddle with your fishing rod...") 

    
def caughtFish():
    t.cancel()
    print(f"Congrats you caught a fish!\nYou win!")
    time.sleep(3)
    return mainMenu()


def generateFish():
    #generates a fish that is generated if user completes fishing minigame successfully
    #should write to JSON file the generated fish

    # NOTE: THIS SHOULD BE USING A LIST OF LISTS, NOT A DICTIONARY, wrong datatype
    # NO, i CAN use a dictionary of dictionaries, i just don't know how to make each
    # dictionary with a unique ID & NOT overwrite other dicts, every dictionary should
    # be unique - ok this isn't exactly possible, since a dictionary CANNOT have
    # duplicate keys, it will always overwrite - so either lists or database
    # for my use case i could also just use SQLite or a DB
    def newFish():

        id = random.randint(1,300)
        randomWeight = random.randint(5,20)
        randomPrice = random.randint(1,50)

        fishList = [id, "brown-nose", randomWeight, randomPrice]

        return fishList

    listOfFish.append(newFish())
    time.sleep(1)
    return mainMenu()

def getAllFish():
    #function to get all fish from a JSON file & display them
    return 0

# TEST METHOD
def printFishDict():
    #print(listOfFish)
    print(*listOfFish, sep='\n') # will print the list vertically
    print(len(listOfFish)) # print number of fish (lists within the list)
    return mainMenu()

# Response functions

def showFish():
    return print("a list of caught fish with ascii art")

def showShop():
    return print("a list of shop items w prices")

def showHelp():
    return print("instructions on how to play the game")

def exitGame():
    return print("exiting...")

def badInput():
    print("please enter a valid number!")
    return mainMenu()

# Main entry point
def main():
    welcome()
    mainMenu()

if __name__ == '__main__':
	main()
