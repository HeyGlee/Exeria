# Main file for game
from time import sleep as wait  # <- for more interactive gameplay
from lib.entity_lib import Character    # <- gets the user's class
from index.item_lib import items
import random   # <- random logic

def main():


    def wait_for_input() -> str:
        while True:
            try:
                selected = int(input("Please enter a number: "))
                if 0 < selected < 5:
                    return selected
                print("ERROR: number needs to be between 1-4!!")
            except TypeError:
                print("ERROR: Please enter a number 1-4!!")
            
    def intro() -> object:  # determines the character
        print("GAME: Welcome to EXERIA!")
        wait(1.2)
        name = input("GAME: Please enter your name: ")
        print("GAME: Now, select your class: ")
        wait(1.2)
        print("1) Newbie: has nothing but a sword")
        wait(1.2)
        print("2) Buffed: starts off with extra health")
        wait(1.2)
        print("3) Mage: starts off with extra mana")
        wait(1.2)
        print("4) Rich: starts off with 150 coins")
        selected = wait_for_input()

        def display_selected(class_name):
            print(f"GAME: So {name}, you have selected the {class_name}")
            wait(1.2)
            print("GAME: Creating character.", end="")
            wait(0.8)
            print(".",end="")
            wait(0.8)
            print(".")
            wait(1.2)
            print("GAME: Character created!") 


        match selected:
            case 1:
                display_selected("newbie class")
                return Character(name, 1, 100, 100, 100, 100, 
                                 1, 0, 1, 1, None, None, None, None, items["Wooden sword"])
            case 2:
                display_selected("buffed class")
                return Character(name, 1, 190, 190, 100, 100, 
                                 1, 0, 1, 1, None, None, None, None, items["Wooden sword"])
            case 3:
                display_selected("mage class")
                return Character(name, 1, 100, 100, 190, 190, 
                                 1, 0, 1, 1, None, None, None, None, items["Wooden sword"])
            case 4:
                display_selected("rich class")
                return Character(name, 1, 100, 100, 100, 100, 
                                 1, 150, 1, 1, None, None, None, None, items["Wooden sword"])
    

    user = intro()


if __name__ == "__main__":
    main()