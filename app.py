# Let's add some more excitement to this challenge and make the game multiplayer, where the computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like you. Your interaction in the game will be through the console (Terminal).

# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

import random

def main():
    print("Welcome to Rock, Paper, Scissors!")
    player_score = 0
    computer_score = 0
    while True:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue
        if player_choice == computer_choice:
            print("It's a tie!")
        elif player_choice == "rock" and computer_choice == "scissors":
            print("You win!")
            player_score += 1
        elif player_choice == "paper" and computer_choice == "rock":
            print("You win!")
            player_score += 1
        elif player_choice == "scissors" and computer_choice == "paper":
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            computer_score += 1
        print(f"Player: {player_score}, Computer: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    
if __name__ == "__main__":
    main()