import random
import time
from threading import Timer


print("Welcome to FishMaster, the CLI fishing game!")
print("Enter a number:")

command = int(input("""
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
            return "show my fish"
        case 3:
            return "Shop item 1 , 2 , 3 price"
        case 4:
            return "Instructions on how to play"
        case 5:
            return "exiting..."
        
        case _:
            return "please enter a valid number!"

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

response(command)
