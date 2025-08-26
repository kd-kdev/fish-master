# Version of Fish Master written using Python + Rich
import random
import time
from threading import Timer
import rich
import curses
from rich.console import Console
from rich.panel import Panel


console = Console()

console.print(Panel.fit("Welcome to [bold blue]Fish Master[/bold blue], the CLI fishing game!"))
command = int(input("""
Please enter a number:
1. Start fishing
2. My fish
3. Shop
4. Help
5. Exit
"""))


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
    return print(f"Congrats you caught a fish!\nYou win!")


# Response functions

def showFish():
    curses.endwin()
    return print("a list of caught fish with ascii art")

def showShop():
    return print("a list of shop items w prices")

def showHelp():
    return print("instructions on how to play the game")

def exitGame():
    return print("exiting...")

def badInput():
    return print("please enter a valid number!")


response(command)
