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
playerMoney = 0
TIME_UPPER_LIMIT = 15
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
    randomTime = random.randint(1, TIME_UPPER_LIMIT)

    for i in range(randomTime):
        time.sleep(1)
        print(f"{i+1} bobbing...")

    try:
        pull = pyip.inputStr(prompt="fish caught!\nyou have 5 seconds to type 'pull' to catch the fish!\n", timeout=5, default="this is the default!", limit=2)
        if pull == "pull":
            caughtFish()
        else:
            fishGotAway()
    except pyip.TimeoutException:
        fishGotAway()
        
    
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

def sellAllFish():
    global playerMoney
    if listOfFish:
        totalSum = 0
        for i in listOfFish:
            #print(i)
            #print(i[2])
            totalSum = totalSum + i[2]
            
        playerMoney += totalSum
        print(f"You sold {len(listOfFish)} fish for {playerMoney} gold!")
    else:
        print("No fish to sell!")

# SHOP

def showShop():

        # Shop menu
    def responseShop(commandShop):
        match commandShop:
            case 1:
                return upgradeBait()
            case 2:
                return upgradeRod()
            case 3:
                return upgradeBoat()
            case 4:
                return sellAllFish()
            case 5:
                return mainMenu()
            case _:
                return badInput()

    commandShop = int(input(f"""\nYou have {playerMoney} gold.\nPlease enter a number:
1. Upgrade bait (100 gold)
2. Upgrade rod (200 gold)
3. Upgrade boat (500 gold)
4. Sell all fish
5. Exit shop
"""))
    responseShop(commandShop)


def upgradeBait():
    global TIME_UPPER_LIMIT
    if playerMoney >= 100:
        print("Bait upgraded!")
        TIME_UPPER_LIMIT = TIME_UPPER_LIMIT - 1
    else:
        print("Not enough gold, sell more fish!\n")
        showShop()
    
    time.sleep(1)
    return mainMenu()

def upgradeRod():
    global TIME_UPPER_LIMIT
    if playerMoney >= 200:
        print("Rod upgraded!")
        TIME_UPPER_LIMIT = TIME_UPPER_LIMIT - 2
    else:
        print("Not enough gold, sell more fish!\n")
        showShop()

    time.sleep(1)
    return mainMenu()

def upgradeBoat():
    global TIME_UPPER_LIMIT
    if playerMoney >= 500:
        print("Boat upgraded!")
        TIME_UPPER_LIMIT = TIME_UPPER_LIMIT - 6
    else:
        print("Not enough gold, sell more fish!\n")
        showShop()
    time.sleep(1)
    return mainMenu()



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