# import modules
import time
import sys
import colorama
from colorama import Fore
colorama.init(autoreset=True)


# typewriter effect
# code taken from Learn Learn Scratch Tutorials - YouTube link in README
def typewriter(effect):
    for char in effect:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)


# the library needs to know your name
name = input("Please enter your name: ").capitalize().strip()
print(f"Welcome to the library {name}! Hope you find something special.")


# the story begins
def story_begins():
    typewriter("As you walk through the aisle of books, a red book catches \n")
    typewriter("your eye. You pick it up and skim through, not realising \n")
    typewriter("that it's a magical book, and that it has picked you for a \n")
    typewriter("reason. You decide to sit down and begin to read the book. \n")
    typewriter("As you read the book, the library starts to disappear. \n")
    typewriter("You find yourself in a magical land and fact-to-face with \n")
    typewriter("a wizard. The wizard has been hurt in a battle to bring \n")
    typewriter("magic back to land. The wizard senses your powers growing \n")
    typewriter("gives you his powers.")