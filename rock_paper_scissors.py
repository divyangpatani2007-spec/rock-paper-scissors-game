import random

print("===== ROCK PAPER SCISSORS GAME =====")

player_score = 0
computer_score = 0

while True:
    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "4":
        break

    if choice not in ["1", "2", "3"]:
        print("Invalid choice! Try again.")
        continue

    options = ["Rock", "Paper", "Scissors"]
    player = options[int(choice) - 1]
    computer = random.choice(options)

    print("Your choice:", player)
    print("Computer choice:", computer)

    if player == computer:
        print("It's a Draw!")

    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):

        print("You Win!")
        player_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("Your Score:", player_score)
    print("Computer Score:", computer_score)

print("\n===== FINAL SCORE =====")
print("Your Score:", player_score)
print("Computer Score:", computer_score)

if player_score > computer_score:
    print("Congratulations! You won the game.")
elif computer_score > player_score:
    print("Computer won the game.")
else:
    print("The game is a draw.")

print("Thank you for playing!")
