from ASCII import logo
from helpers import background_story
import os

print(logo)
def menu():
    while True:
        print(
        "Welcome to our game. Write down: \n >>1 to start the game \n >>2 to read FAQ \n >>3 to see scoretable \n >>4 to exit game")
        choice_1 = input("What do you choose? ")
        if choice_1 == "4":
            from ASCII import chicken
            print("Pity..")
            print(chicken)
        elif choice_1 == "2":
            from FAQ import FAQ
            print(FAQ)
        elif choice_1 == "3":
            from scoreboard import scorebard
            print(scorebard)
        elif choice_1 == "1":
            print("Our journy beggins..")
            break
        else:
            print("Invalid choice, please try again.")
menu()

background_story()

print("Choose your role:")

from Characters import Character
from Characters import Archaeologist
from Characters import Merchant

print(Character.get_description(Archaeologist))
print("<-----><-----><----->")
print(Character.get_description(Merchant))

def choose_your_class():
    choice_2 = input("Which character do you choose? For Archeologist write down 'A'. For Merchant write down 'M' :")
    if choice_2 == 'A':
        print("<-----><-----><----->")
        print("You chose Archeologist!")
        with open("chosen_class.txt", "w") as file:
            file.write("A")
        return True
    elif choice_2 == 'M':
        print("<-----><-----><----->")
        print("You chose Merchant!")
        with open("chosen_class.txt", "w") as file:
            file.write("M")
        return True
    else:
        print("Invalid choice. Please write down 'A' for Archeologist or 'M' for Merchant.")
        return choose_your_class()

walidacja = choose_your_class()

from helpers import choosing_difficulty
if walidacja == True:
    choosing_difficulty()

walidacja = choosing_difficulty()
#TODO doubling output

with open("chosen_class.txt", "r") as file:
    chosen_hero = file.read().strip()

from helpers import next_step
if walidacja == True:
    next_step()