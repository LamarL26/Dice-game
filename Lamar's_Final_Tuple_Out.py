# Lamar Logan
# INST126
# Prof. Jackson
# Date: 12/14/2024

import random
import pandas as pd
import time

def roll_dice():
    """

    Simulates rolling a single die.

    """
    return random.randint(1, 6)

def play_turn(player_name):
    """

    Handles a single player's turn. Limits the rolls to 3 times.

    """
    print(f"\n{player_name}'s Turn!")
    dice = [roll_dice(), roll_dice(), roll_dice()]  # First roll
    print(f"Roll: {dice}")
    time.sleep(1)  # Add a delay for dramatic effect

    # Check for tuple out (all three dice are the same)
    if dice[0] == dice[1] == dice[2]:
        print("Tuple out! No points this turn.")
        return 0

    rolls = 1  # Tracks the number of rolls (starts at 1 since the first roll is done)

    while rolls < 3:
        choice = input(f"Roll #{rolls + 1}: Enter 'roll' to roll the dice again, or 'stop' to stop: ").strip().lower()
        if choice == 'stop':
            break
        elif choice == 'roll':
            dice = [roll_dice() for _ in range(3)]  # Re-roll all dice
            print(f"New Roll: {dice}")
            time.sleep(1)  # Add a delay for dramatic effect
            rolls += 1
            if dice[0] == dice[1] == dice[2]:
                print("Tuple out! No points this turn.")
                return 0
        else:
            print("Invalid choice. Please enter 'roll' or 'stop'.")
    
    score = sum(dice)
    print(f"{player_name} ends the turn with a score of {score}.")
    return score

def get_player_names():
    """

    Prompts for and returns a list of player names.

    """
    while True:
        try:
            num_players = int(input("\nEnter the number of players (2-5): "))
            if 2 <= num_players <= 5:
                break
            else:
                print("Please enter a valid number between 2 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    players = []
    for i in range(num_players):
        name = input(f"Enter the name of Player {i + 1}: ")
        players.append(name.strip())
    return players

def get_target_score():
    """

    Prompts for a valid target score within the range.

    """
    while True:
        try:
            score = int(input("\nEnter the target score (between 25 and 300): "))
            if 25 <= score <= 300:
                return score
            else:
                print("Score must be between 25 and 300.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Game introduction
print("\nWelcome to the 'Tuple Out' Dice Game!\n",
      "______________________________________")

print("Rules:")
print("- Roll three dice per turn.")
print("- If all three dice are the same, you 'tuple out' and score 0 for the round.")
print("- Choose a score between 25 and 300 to play up to.")
print("- You may roll up to 3 times per turn.")
print("- Your score for the turn is the sum of the three dice.")

player_choice = input("\nDo you want to play the game? (Y/N): ").strip().lower()
if player_choice == "n":
    print("Ok, no worries! Maybe next time. Goodbye!")
    exit()
elif player_choice != "y":
    print("Invalid input. Please enter 'Y' or 'N'.")
    exit()

print("Sounds great! Let's play!")

# Get the player names and the target score
players = get_player_names()
target_score = get_target_score()

# Initialize player scores
scores = {player: 0 for player in players}

# This is the overall game loop
game_running = True
while game_running:
    for player in players:
        scores[player] += play_turn(player)
        print(f"Current Scores: {scores}")
        
        # Check for winning condition once a player reaches the target score
        if scores[player] >= target_score:
            print(f"\n{player} wins the game with {scores[player]} points!")
            game_running = False
            break

# Display final scores
print("\nFinal Scores:")
for player, score in scores.items():
    print(f"{player}: {score}")
print("The game is over! Thanks for playing!")
