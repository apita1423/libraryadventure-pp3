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


# ASCII title and art
print(r"""
  _      _ _                 
 | |    (_) |                    
 | |     _| | _  _ __ __ _ _ __ _   _ 
 | |    | | '_ \| '__/ _` | '__| | | |
 | |____| | |_) | | | (_| | |  | |_| |
 |______|_|_.__/|_|  \__,_|_|   \__, |
                                 __/ |
                                |___/ 
""")

print(r"""
              _                 _                  
     /\      | |               | |                 
    /  \   __| |_   _____ _ __ | |_ _   _ _ __ ___ 
   / /\ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \
  / ____ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/
 /_/    \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|
 """)

print(fr"""{Fore.RED}
    .--.                   .---.

   .---|__|           .-.     |~~~|

.--|===|--|_          |_|     |~~~|--.

|  |===|  |'\     .---!~|  .--|   |--|

|%%|   |  |.'\    |===| |--|%%|   |  |

|%%|   |  |\.'\   |   | |__|  |   |  |

|  |   |  | \  \  |===| |==|  |   |  |

|  |   |__|  \.'\ |   |_|__|  |~~~|__|

|  |===|--|   \.'\|===|~|--|%%|~~~|--|

^--^---'--^    `-'`---^-^--^--^---'--' hjw
""")
print()


# the library needs to know your name
name = input(f"{Fore.YELLOW}Please enter your name: ").capitalize().strip()
print(f"Welcome to the library {name}! Hope you find something special.")
time.sleep(3)
print()


# the story begins
def story_begins():
    typewriter("Let the adventure begin... \n")
    typewriter("As you walk through the aisle of books, a red book catches \n")
    typewriter("your eye. You pick it up and skim through, not realising \n")
    typewriter("that it's a magical book, and that it has picked you for a \n")
    typewriter("reason. You decide to sit down and begin to read the book. \n")
    typewriter("As you read the book, the library starts to disappear. \n")
    typewriter("You find yourself in a magical land and face-to-face with \n")
    typewriter("a wizard. The wizard has been hurt in a battle to bring \n")
    typewriter("magic back to the land. The wizard senses your powers \n")
    typewriter("growing and gives you his powers.")
    start_adventure()
    print()


def start_adventure():
    print()
    typewriter("Do you accept the wizard's gift? (Y/N) ")
    print()
    while True:
        print()
        answer = input("Type 'Y' for YES or 'N' ").lower.strip
        if answer == "Y":
            quest()
        elif answer == "N":
            print("Adventure Over! You're back in the library!")
        else:
            print("Please type 'Y' for YES or 'N' for No").lower.strip


def quest():
    typewriter("Great! The crystal of the wizard's staff was hidden by his /n")
    typewriter("familiar: a cat. The townspeople are doing their best to /n")
    typewriter("to hold off the evil demons. Many are saying that they /n")
    typewriter("saw the cat head toward Cassini's Temple")
    print()
    while True:
        print("Choose 1 or 2")
        choice = ("Cassini's Temple (1) or Fight (2)").lower().strip()
        if choice == "1":
            allies()
        elif choice == "2":
            print("You do not know how to use your power. You have died.")
        else:
            print("Please choose 1 or 2")


story_begins()
