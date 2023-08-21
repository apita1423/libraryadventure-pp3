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


# ASCII title and book art. Iniital of book art creator is shown on the side
# title() function starts the program.
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


# story_begins() prompts the user to input their name so they can be
# welcomed into the library. If the user does not want to add their
# name, it will still welcome them but it would say mysterious user.
def story_begins():
    print()
    name = input(f"{Fore.YELLOW}Please enter your name: ").capitalize().strip()
    print()
    if name == "":
        print(f"{Fore.YELLOW}Welcome to the library Mysterious User! \n")
        typewriter("Hope you find something special.")
    else:
        print(f"Welcome to the library {name}! \n")
        typewriter("Hope you find something special.")
    time.sleep(2)
    print()
    adventure_begins()


# adventure_begins() gives a back story to the text adventure game and
# initiates the game with the start_adventure().
def adventure_begins():
    print()
    typewriter("Let the adventure begin... \n")
    print()
    typewriter("As you walk through the aisle of books, a red book catches \n")
    typewriter("your eye. You pick it up and skim through, not realising \n")
    typewriter("that it's a magical book and that it has picked you for a \n")
    typewriter("reason. You decide to sit down and begin to read the book. \n")
    typewriter("As you read the book, the library starts to disappear. \n")
    typewriter("You find yourself in a magical land and face-to-face with \n")
    typewriter("a wizard. The wizard has been hurt in a battle to bring \n")
    typewriter("magic back to the land. The wizard senses your powers \n")
    typewriter("growing and gives you his powers.")
    print()
    start_adventure()


# start_adventure() begins the game with a question following the back story.
# It allows the user to type yes or no. If they type yes it continues to
# the next part of the game. If they press no it gives them a adventure
# over statement and takes the user back to the beginning.
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
            print(f"{Fore.RED}Adventure Over! You're back in the library!")
            time.sleep(4)
            title()
        else:
            print("Please type YES or No ")
            continue


# quest() happens when the user has typed yes in the start_adventure()
# question. Here the user is given a snippet of the rest of story with
# a question at the end. The question allows for two answers 1 or 2.
# If they chose the correct answer it prompts the next part of the story.
# If the user chooses the wrong answer they get an adventure over statement
# and a chance to play again.
def quest():
    print()
    typewriter("Great! The crystal of the wizard's staff has been hidden \n")
    typewriter("by his familiar: a cat. The townspeople are doing their \n")
    typewriter("best to hold off the evil demons. Many are saying \n")
    typewriter("that they saw the cat head toward Cassini's Temple. \n")
    print()
    typewriter("Do you follow (1) the cat or fight (2) together \n")
    typewriter("with the townspeople? Choose 1 or 2.")
    print()
    while True:
        print()
        answer = input("Follow (1) or Fight (2): ").lower().strip()
        if answer == "1":
            allies()
        elif answer == "2":
            print(f"{Fore.RED}You do not know how to use your power yet. \n")
            print(f"{Fore.RED}You have died!")
            adventure_over()
        else:
            print("Please chose 1 or 2")
            continue


# allies() happens after the user input the correct answer in the quest()
# function. The action here is the same as quest(). Continuing the story,
# the user again needs to decide which choice they are going to pick. If the
# user choses the right choice it prompts intentions. If the user choses the
# wrong answer, they are prompt with adventure over statement and a chance
# to start over.
def allies():
    print()
    typewriter("Awesome! You chose to follow the cat and start your quest \n")
    typewriter("to Cassini's Temple. The cat has led you to the \n")
    typewriter("wizard's home. You find a note written to you to travel \n")
    typewriter("into the Forgotten Forest and find allies to help you \n")
    typewriter("restore magic. \n")
    print()
    typewriter("Do you want to go on the adventure alone (1) or \n")
    typewriter("find allies (2)? Choose 1 or 2. ")
    print()
    while True:
        print()
        answer = input("Alone (1) or Allies (2): ").lower().strip()
        if answer == "1":
            print(f"{Fore.RED}Adventure Over! \n")
            print(f"{Fore.RED}To win this battle you need allies.")
            adventure_over()
        elif answer == "2":
            intentions()
        else:
            print("Please chose 1 or 2")
            continue


# intentions() is what comes after the correct answer was picked in allies().
# It does the same has the previous codes. It continues the story and
# the user needs to chose the correct answer. If correct answer is picked
# it prompts the next part of the storyline. If the incorrect answer is
# picked it gives them an adventure over statement and allows the user
# to play again.
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
            print(f"{Fore.RED}Adventure Over! \n")
            print(f"{Fore.RED}Your intentions are not worthy.")
            adventure_over()
        elif answer == "2":
            crystal()
        else:
            print("Please choose 1 or 2")
            continue


# crystal() is the continuing storyline from intentions(), if the user chose
# the correct answer. It also gives two options to pick and if the wrong
# answer is chosen it hints that the adventure is over and also prompts the
# user if they want to play again.
def crystal():
    print()
    typewriter("The journey has been long and treacherous, but with the \n")
    typewriter("help of your allies and the cat, you have found Cassini's \n")
    typewriter("Temple. The cat has also led you to the crystal that he \n")
    typewriter("hid. Now the crystal has tremendous power. What would \n")
    typewriter("you do with the crystal's power? \n")
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
            print(f"{Fore.RED}Greed has consumed you. \n")
            print(f"{Fore.RED}The power is too strong and you have died. \n")
            adventure_over()
        else:
            print("Please choose 1 or 2")
            continue


# magic() is the last part of the storyline. The user's choice is different
# here. Once they have reached last part of the story they are asked if
# they want to go on another adventure or go home. If they choose another
# adventure they are prompted with a statement saying the adventure is brewing
# (or in the making). If they use to go home they are back at the beginning of
# the game.
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


# adventure_over is a function used for when users pick the wrong answer.
# They are allowed to start over. If they decide not to play again they are
# prompted with a GAME OVER! and the game starts over from the beginning. If
# they chose yes they are brought back to the start_adventure() question.
# This function is placed in the wrong answers through the story.
def adventure_over():
    print()
    typewriter("You have lost your way. Let's see if the wizard will give \n")
    typewriter("you another chance. \n")
    print(f"{Fore.GREEN}Play again? \n")
    while True:
        print()
        answer = input("Type YES or NO: \n").lower().strip()
        if answer == "yes":
            adventure_begins()
        elif answer == "no":
            print(f"{Fore.RED}GAME OVER!")
            time.sleep(4)
            title()
        else:
            print("Type YES or NO")
            break


# title() calls the function to start the game
title()
