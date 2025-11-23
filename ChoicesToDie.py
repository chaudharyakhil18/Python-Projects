import time
import sys

# Optional: Add colors for a more visual experience
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

health = 15

def slow_print(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

slow_print(f"{Color.CYAN}--- Welcome to the Most Dangerous Game ---{Color.RESET}")
name = input("Tell me your name: ")
age = input("And your age: ")

while not age.isdigit():
    age = input("Enter a valid number for age: ")
age = int(age)

slow_print(f"Hello {name}, you are {age} years old.\n")

if age < 16:
    slow_print(f"{Color.RED}You are too young to play this dangerous game!{Color.RESET}")
    quit()

slow_print("You are old enough, but are you brave enough?")
want = input("Do you want to play? (yes/no): ").lower()

if want not in ["yes", "y"]:
    slow_print("Fair enough! Come back when you're ready for danger.")
    quit()

slow_print(f"\nGreat! You have {Color.GREEN}{health} health{Color.RESET}. Survive wisely...")
time.sleep(1)

# FIRST CHOICE
choice1 = input("\nPath splits: left or right? ").lower()
if choice1 == "left":
    health = 0
    slow_print(f"{Color.RED}There was a hidden ditch. You fell and died instantly!{Color.RESET}")
else:
    slow_print("You enter a dark forest...")

    # SECOND CHOICE
    choice2 = input("Go THROUGH the forest or go AROUND it? ").lower()
    if choice2 == "through":
        health -= 10
        slow_print(f"{Color.YELLOW}A lion attacked you! -10 HP{Color.RESET}")
        slow_print(f"Health remaining: {Color.GREEN}{health}{Color.RESET}")

        # THIRD CHOICE
        slow_print("\nYou reach a river.")
        choice3 = input("Swim across or take a boat? (swim/boat): ").lower()

        if choice3 == "swim":
            health -= 10
            slow_print(f"{Color.RED}Piranhas attacked you... You lost the rest of your health!{Color.RESET}")
        else:
            slow_print(f"{Color.GREEN}The boatman was kind and helped you cross safely!{Color.RESET}")
            slow_print("You see a castle... You walk inside and find treasure! 🏆")
            slow_print(f"{Color.GREEN}You Win!{Color.RESET}")
            quit()

    else:
        health = 0
        slow_print(f"{Color.RED}A giant bear was waiting for you. You didn’t survive...{Color.RESET}")

# Ending based on health
if health <= 0:
    slow_print(f"{Color.RED}GAME OVER!{Color.RESET}")
else:
    slow_print(f"{Color.GREEN}You narrowly survived with {health} health!{Color.RESET}")
    slow_print("Congrats... but danger still awaits... 👀")
