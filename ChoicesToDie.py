import time

health = 15

print("---Welcome to the most dangerous game.---")
name = input("Tell me your name first.\n")
age = int(input("And, your age also.\n"))
time.sleep(1)
print("Hello",name,", you are",age,"years old.")
time.sleep(1)

if age >= 15:
    print("As I told you, it a dangerous game. But, you are old enough to play.")
    time.sleep(1)
    wants_to_play = input("So, do you want to play. Remember its dangerous.?(Yes/No)\n")
    if wants_to_play.lower() == "yes":
        time.sleep(0.5)
        print("You are brave. Let's play.")

        choice1 = input("Choose : left or right?\n").lower()
        if choice1=="left":
            health -= 10

    else:
        time.sleep(0.5)
        print("You coward. I expected that.\nYou are fattu.\nFind some easy games kid. Bye.")
else:
    print("I told you, this is a dangerous game, you are not old enough to play this game.")
    print("Get bigger, older and have guts. Then, come back, baby.")
