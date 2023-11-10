# Main file for game
from time import sleep as wait  # <- for more interactive gameplay
from lib.entity_lib import Character    # <- gets the user's class
from index.item_lib import items
import random   # <- random logic

def main():


    def wait_for_input() -> str:
        while True:
            selcted = input("Please enter a number: ")
            if 0 < selcted < 5:
                return selcted
            
    def intro() -> object:  # determines the character
        print("GAME: Welcome to EXERIA!")
        wait(1.2)
        name = input("GAME: Please enter your name: ")
        print("GAME: Now, select your class: ")
        wait(1.2)
        print("1) Newbie: has nothing but a sword")
        wait(1.2)
        print("1) Buffed: starts off with extra health")
        wait(1.2)
        print("1) Mage: starts off with extra mana")
        wait(1.2)
        print("1) Rich: starts off with 150 coins")
        selected = wait_for_input()
        match selected:
            case "1":
                return Character(name, 1, 100, 100, 100, 100, 
                                 1, 0, 1, 1, None, None, None, None, items["Wooden sword"])
            case "2":
                return Character(name, 1, 190, 190, 100, 100, 
                                 1, 0, 1, 1, None, None, None, None, items["Wooden sword"])
            case "3":
                return Character(name, 1, 100, 100, 190, 190, 
                                 1, 0, 1, 1, None, None, None, None, items["Wooden sword"])
            case "4":
                return Character(name, 1, 100, 100, 100, 100, 
                                 1, 150, 1, 1, None, None, None, None, items["Wooden sword"])
    

    user = intro()


if __name__ == "__main__":
    main()