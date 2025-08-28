# Version of Fish Master written using Python + Rich
import random
import time
import json
from collections import Counter
import threading
from threading import Timer
import rich
from rich.console import Console
from rich.panel import Panel
import pyinputplus as pyip

# Globals
console = Console()
listOfFish = []
FISH_NAMES = {'Brown nose': 1,
              'Sand fin': 1.2,
              'Mudrunner': 1.5,
              'Som': 2,
              'Crud maker': 3,
              'High gill': 2.5,
              'Small tail': 2.2,
              'Tabber': 2,
              'Spacer': 2
              }

def welcome():
    return console.print(Panel.fit("Welcome to [bold blue]Fish Master[/bold blue], the CLI fishing game!"))
    
def mainMenu():
    command = int(input("""\nPlease enter a number:
1. Start fishing
2. My fish
3. Shop
4. Help
5. Exit
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
        case _:
            return badInput()


### Main game

def fishGotAway():
    print("the fish got away! :( ")
    return mainMenu()



def fishingMinigame():
    randomTime = random.randint(1,8)

    for i in range(randomTime):
        time.sleep(1)
        print(f"{i+1} bobbing...")

    try:
        pull = pyip.inputStr(prompt="fish caught!\ntype 'pull' to catch fish!\n", timeout=5, default="this is the default!", limit=2)
        if pull == "pull":
            caughtFish()
        else:
            fishGotAway()
    except pyip.TimeoutException:
        fishGotAway()
        

        # input is a blocking call that halts execution until the user provides
        # input & presses Enter
        # if pull == "pull":
        #     caughtFish()
        # else:
        #     print("you fiddle with your fishing rod...") 
    
#    return fishGotAway()

# if you don't exit this function properly, it will just start going down the list &
# executing everything else!


    
def makeFish():
    randomName = random.choice(list(FISH_NAMES))
    randomWeight = random.randint(1,30)
    price = round((FISH_NAMES[randomName] * randomWeight), 3)

    fishList = [randomName, randomWeight, price]
    return fishList



def generateFish():
    #generates a fish that is generated if user completes fishing minigame successfully
    #should write to JSON file the generated fish

    
    listOfFish.append(makeFish())
    time.sleep(1)
    return mainMenu()

def getAllFish():
    #function to get all fish from a JSON file & display them
    return 0


def caughtFish():
    print(f"You caught a fish!")
    generateFish()
    time.sleep(2)
    return mainMenu()


# Response functions

def showFish():
    print(*listOfFish, sep='\n') # will print the list vertically
    print(f"Number of fish: {len(listOfFish)}")
    return mainMenu()

def showShop():
    return print("a list of shop items w prices")

def showHelp():
    return print("instructions on how to play the game")

def exitGame():
    print("exiting...")
    return quit()

def badInput():
    print("please enter a valid number!")
    return mainMenu()


# Main entry point
def main():
    welcome()
    mainMenu()

if __name__ == '__main__':
	main()