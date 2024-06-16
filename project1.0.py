import random
import time

def commentary(Runs, name):
    switcher = {
        0: name + " went for a great defence",
        1: name + " took a single",
        2: "2 runs .... great running by " + name + "!",
        3: "Risky play by " + name + "...but took 3 runs",
        4: "What a shot by " + name + "! 4 runnnssssssssssss!!",
        6: name + " !! went high and gone for a SIX!!!!!"
    }
    return switcher.get(Runs, "nothing")

def get_valid_input(prompt, valid_choices):
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_choices:
                return choice
            else:
                print("Invalid input. Please enter one of the following: ", valid_choices)
        except ValueError:
            print("Invalid input. Please enter a number.")

Name1 = input("Enter player 1 name: ")
Name2 = input("Enter player 2 name: ")
print("Toss the coin...")
ran = [Name1, Name2]
toss_winner = random.choice(ran)
choice = input(toss_winner + " choose Head/Tails (H/T): ").upper()
toss_result = random.choice(['H', 'T'])
print("Tossing...")
time.sleep(2)

if (choice == 'H' and toss_result == 'H') or (choice == 'T' and toss_result == 'T'):
    print(toss_winner + " won the toss")
    decision = get_valid_input(toss_winner + "....do you choose Batting or Bowling?(1 for Batting / 2 for Bowling): ", [1, 2])
else:
    toss_loser = Name2 if toss_winner == Name1 else Name1
    print(toss_loser + " won the toss")
    decision = get_valid_input(toss_loser + "....do you choose Batting or Bowling?(1 for Batting / 2 for Bowling): ", [1, 2])

if decision == 1:
    first_batter = toss_winner
    second_batter = Name2 if first_batter == Name1 else Name1
    print(f"{first_batter} chose to bat first")
    print(f"{second_batter} will bowl first")
else:
    second_batter = toss_winner
    first_batter = Name2 if second_batter == Name1 else Name1
    print(f"{second_batter} chose to bowl first")
    print(f"{first_batter} will bat first")

print("Let's begin the game")

seconds = [1, 2, 3]
first_batter_score = 0
second_batter_score = 0
first_batter_out = False
second_batter_out = False
first_batter_century = False
second_batter_century = False
first_batter_half_century = False
second_batter_half_century = False

# First batting session
print(f"{first_batter} is batting")
while not first_batter_out:
    time.sleep(random.choice(seconds))
    runs = get_valid_input(f"Enter runs for {first_batter} (0, 1, 2, 3, 4, 6): ", [0, 1, 2, 3, 4, 6])
    bowl = random.choice([0, 1, 2, 3, 4, 6])
    if runs != bowl:
        print(commentary(runs, first_batter))
        first_batter_score += runs
        if first_batter_score >= 100 and not first_batter_century:
            print(f"{first_batter} scored a century!")
            first_batter_century = True
        elif first_batter_score >= 50 and not first_batter_half_century:
            print(f"{first_batter} scored a half-century!")
            first_batter_half_century = True
        print("Score is:", first_batter_score)
    else:
        print(first_batter + " is out")
        first_batter_out = True
        print(f"{first_batter}'s Score = {first_batter_score}")

# Second batting session
print(f"{second_batter} is batting")
while not second_batter_out:
    time.sleep(random.choice(seconds))
    runs = get_valid_input(f"Enter runs for {second_batter} (0, 1, 2, 3, 4, 6): ", [0, 1, 2, 3, 4, 6])
    bowl = random.choice([0, 1, 2, 3, 4, 6])
    if runs != bowl:
        print(commentary(runs, second_batter))
        second_batter_score += runs
        if second_batter_score >= 100 and not second_batter_century:
            print(f"{second_batter} scored a century!")
            second_batter_century = True
        elif second_batter_score >= 50 and not second_batter_half_century:
            print(f"{second_batter} scored a half-century!")
            second_batter_half_century = True
        print("Score is:", second_batter_score)
    else:
        print(second_batter + " is out")
        second_batter_out = True
        print(f"{second_batter}'s Score = {second_batter_score}")

print("Game over")
if first_batter_score > second_batter_score:
    print(f"{first_batter} wins by {first_batter_score - second_batter_score} runs")
elif second_batter_score > first_batter_score:
    print(f"{second_batter} wins by {10 - second_batter_score} wickets")
else:
    print("It's a tie!")
