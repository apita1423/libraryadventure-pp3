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
        time.sleep(0.02)


# ASCII title and art
def title():
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
    story_begins()


def story_begins():
    print()
    name = input(f"{Fore.YELLOW}Please enter your name: ").capitalize().strip()
    print()
    if name is "":
        print(f"{Fore.YELLOW}Welcome to the library Mysterious User! \n")
        print("Hope you find something special.")
    else:
        print(f"Welcome to the library {name}! \n")
        print("Hope you find something special.")
    time.sleep(2)
    print()
    adventure_begins()


def adventure_begins():
    typewriter("Let the adventure begin... \n")
    print()
    typewriter("As you walk through the aisle of books, a red book catches \n")
    typewriter("your eye. You pick it up and skim through, not realising \n")
    typewriter("that it's a magical book, and that it has picked you for a \n")
    typewriter("reason. You decide to sit down and begin to read the book. \n")
    typewriter("As you read the book, the library starts to disappear. \n")
    typewriter("You find yourself in a magical land and face-to-face with \n")
    typewriter("a wizard. The wizard has been hurt in a battle to bring \n")
    typewriter("magic back to the land. The wizard senses your powers \n")
    typewriter("growing and gives you his powers.")
    print()
    start_adventure()


def start_adventure():
    print()
    typewriter("Do you accept the wizard's gift? (yes/no) ")
    print()
    while True:
        print()
        answer = input("Type YES or NO: ").lower().strip()
        if answer == "yes":
            quest()
        elif answer == "no":
            print("Adventure Over! You're back in the library!")
            adventure_over()
        else:
            print("Please type YES or No ")
            continue


def quest():
    print()
    typewriter("Great! The crystal of the wizard's staff was hidden by his \n")
    typewriter("familiar: a cat. The townspeople are doing their best to \n")
    typewriter("hold off the evil demons. Many are saying that they \n")
    typewriter("saw the cat head toward Cassini's Temple. \n")
    print()
    typewriter("Do you follow the cat (1) or fight (2) together with the \n")
    typewriter("townspeople? Choose 1 or 2.")
    print()
    while True:
        print()
        answer = input("Follow (1) or Fight (2): ").lower().strip()
        if answer == "1":
            allies()
        elif answer == "2":
            print("You do not know how to use your power. You have died.")
            adventure_over()
        else:
            print("Please chose 1 or 2")
            continue


def allies():
    print()
    typewriter("Awesome! You chose to follow the cat and start your quest \n")
    typewriter("to the Cassini Temple. The cat has led you to the wizard's \n")
    typewriter("home. You find a note written to you to go into the \n")
    typewriter("Forgotten Forest and find allies to help you restore \n")
    typewriter("magic. \n")
    print()
    typewriter("Do you want to go on the adventure alone(1) or \n")
    typewriter("find allies(2)? Choose 1 or 2. ")
    print()
    while True:
        print()
        answer = input("Alone (1) or Allies (2): ").lower().strip()
        if answer == "1":
            print("Adventure Over! To win this battle you need allies.")
            adventure_over()
        elif answer == "2":
            intentions()
        else:
            print("Please chose 1 or 2")
            continue


def intentions():
    print()
    typewriter("Great! You begin your journey through the Forgotten \n")
    typewriter("Forest. You start to find allies, but be careful with \n")
    typewriter("their intentions. The Guardians of the Realm only want \n")
    typewriter("the crystal to become all-powerful, but the Band of \n")
    typewriter("Dragons want to help bring peace back to the \n")
    typewriter("land. What are your intentions? \n")
    print()
    typewriter("Do you join The Guardians of the Realm (1) or The Band \n")
    typewriter("of Dragons (2)? Choose 1 or 2. \n")
    print()
    while True:
        print()
        answer = input("Guardians of the Realm (1) or Band of Dragons (2): ")
        if answer == "1":
            print("Your intentions are not worthy of the crystal. \n")
            print("Adventure Over!")
            adventure_over()
        elif answer == "2":
            crystal()
        else:
            print("Please choose 1 or 2")
            continue


def crystal():
    print()
    typewriter("The journey has been long and treacherous, but with the \n")
    typewriter("help of your allies and the cat, you have found Cassini's \n")
    typewriter("Temple. The cat has also led you to the crystal that he \n")
    typewriter("hid. Now the crystal has tremendous power and it will only \n")
    typewriter("work if the person possessing it is worthy enough. \n")
    print()
    typewriter("Do you help restore magic (1) or take the crystal's power \n")
    typewriter("for yourself (2)? Choose 1 or 2. \n")
    print()
    while True:
        print()
        answer = input("Restore magic (1) or Take the crystal's power (2): ")
        if answer == "1":
            magic()
        elif answer == "2":
            print("Greed has consumed you. Power is too strong. \n")
            print("You have died. \n")
            adventure_over()
        else:
            print("Please choose 1 or 2")
            continue


def magic():
    print()
    typewriter("Hoorah! Together with your allies and the townspeople you \n")
    typewriter("have managed to kill the evil demons and bring peace \n")
    typewriter("and magic back to the land! Are you ready to go on your \n")
    typewriter("next adventure or go home? Choose 1 or 2. \n")
    print()
    typewriter("Go an another adventure (1) or go home (2)? \n")
    print()
    while True:
        print()
        answer = input("Adventure (1) or Home (2): \n")
        if answer == "1":
            typewriter("That's great! But, this adventure is in the \n")
            typewriter("middle of brewing.")
            time.sleep(4)
            title()
        elif answer == "2":
            typewriter("We will be here when you are ready to come back.")
            time.sleep(4)
            title()
        else:
            print("Please choose 1 or 2")
            break


def adventure_over():
    print()
    typewriter(f"{Fore.RED}You have lost your way. \n")
    typewriter("Wizard might just give you another chance. \n")
    typewriter("Play again? \n")
    while True:
        print()
        answer = input("Type YES or NO: \n").lower().strip()
        if answer == "yes":
            start_adventure()
        elif answer == "no":
            print("Game Over")
        else:
            print("Type YES or NO")
            break


title()
