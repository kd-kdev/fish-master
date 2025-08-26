import random
import time
from threading import Timer
import rich
import curses
from rich.console import Console
from rich.panel import Panel
from pick import pick

console = Console()


console.print(Panel.fit("Welcome to [bold blue]Fish Master[/bold blue], the CLI fishing game!"))

title = 'Please select an option:'
options = ['Start fishing','My fish', 'Shop', 'Help', 'Exit']
option, index = pick(options, title , clear_screen=True)


### Main menu
def response(index):
    match index:
        case 0:
            return fishingMinigame()
        case 1:
            return print("show my fish")
        case 2:
            return print("Shop item 1 , 2 , 3 price")
        case 3:
            return print("Instructions on how to play")
        case 4:
            return print("exiting...")
        
        case _: # not needed since using pick doesn't allow you to choose wrong
            return print("please enter a valid number!")

### Functions

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

response(index)
