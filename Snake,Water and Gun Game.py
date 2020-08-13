import random  # Importing the random for later use
list = ["S","W","G"]
player = input("Enter your name :\t").upper()

total_chances = 10
number_of_chances = 0
computer_points = 0
human_points = 0
print(f"Wel come {player} to snake,water,gun game.")
print("S for snake \nW for water \nG for gun")

while number_of_chances<total_chances:
    h_input = input(":\t").upper()
    c_input = random.choice(list)


    if h_input == c_input:
        print(f"Tie Both get 0 points")
        print(f"{player} guess {h_input} and computer guess {c_input}")

    # If user input S
    elif h_input == "S" and c_input == "G":
        computer_points = computer_points + 1
        print(f"{player} guess {h_input} and computer guess {c_input}")
        print(f"Computer point is {computer_points}")

    elif h_input == "S" and c_input == "W":
        human_points = human_points + 1
        print(f"{player} guess {h_input} and the computer guess {c_input}")
        print(f"{player} point is {human_points}")

    # if human input W
    elif h_input == "W" and c_input == "S":
        computer_points = computer_points + 1
        print(f"{player} guess {h_input} and computer guess {c_input}")
        print(f"Computer point is {computer_points}")

    elif h_input == "W" and c_input == "G":
        human_points = human_points + 1
        print(f"{player} guess {h_input} and the coputer guess {c_input} ")
        print(f"{player} points is  {human_points}")

    # if human guess G
    elif h_input == "G"and c_input == "W":
        computer_points = computer_points + 1
        print(f"{player} guess is {h_input} and computer guess {c_input}")
        print(f"Computer point is {computer_points}")

    elif h_input == "G" and c_input == "S":
        human_points = human_points + 1
        print(f"{player} guess is {h_input} and computer guess {c_input}")
        print(f"{player} point is {human_points}")

    else:
        print("Your input is wrong !!!")


    number_of_chances = number_of_chances + 1
    print(f"\t{total_chances - number_of_chances} chances left out of  {total_chances} !")

if human_points>computer_points:
        print(f"{player} won !")
elif computer_points>human_points:
        print("Computer won !")

print(f"{player} total ponits is {human_points} and computer total points is {computer_points} !")
