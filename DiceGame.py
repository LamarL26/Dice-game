import random

# Function to simulate dice rolls
def roll_dice(num_dice=3):
    """Rolls the specified number of dice and returns a list of results."""

    # The 'randint' function generates random integers between 1 and 6 (inclusive)
    # The list comprehension creates a list of random numbers based on the number of dice
    return [random.randint(1, 6) for _ in range(num_dice)]

# Function to calculate if dice are "fixed"
def check_fixed_dice(dice):
    """Identifies fixed dice based on matching values."""

    # Creates a dictionary that counts the occurrences of each die value

    counts = {num: dice.count(num) for num in dice} 

    # Identifies dice that appear exactly twice, which are considered "fixed"

    fixed = [num for num, count in counts.items() if count == 2]
    return fixed

# Main gameplay function
def tuple_out_game():
    """Runs the Tuple Out Dice Game."""
    # Welcoming the players to the game

    print("Welcome to the 'Tuple Out' Dice Game!")




    # Asking for the number of players (1 or 2)

    num_players = int(input("Enter number of players (1 or 2): "))

    # Set a target score that players need to reach to win (50 points)

    target_score = 50
    scores = [0] * num_players

    # Game loop
    while max(scores) < target_score:
        # Loop through each player and give them a turn


        for player in range(num_players):
            print(f"\nPlayer {player + 1}'s turn:")

            # Roll 3 dice at the start of each player's turn

            dice = roll_dice()
            print(f"Initial roll: {dice}")

            while True:
                fixed = check_fixed_dice(dice)

            # Check if all 3 dice are the same (Tupled out condition)
            # If all dice are the same, the player loses this turn with a score of 0

                if len(fixed) == 1 and dice.count(fixed[0]) == 3:
                    print("Tupled out! You score 0 points this turn.")
                    scores[player] += 0
                    break

                print(f"Fixed dice: {fixed if fixed else 'None'}")
                reroll = input("Do you want to re-roll any unfixed dice? (y/n): ").lower()
                if reroll == "y":
                    dice = [random.randint(1, 6) if num not in fixed else num for num in dice]
                    print(f"Re-rolled dice: {dice}")
                else:
                    
                 # If the player chooses not to re-roll, calculate their score for the turn

                    turn_score = sum(dice)
                    scores[player] += turn_score
                    print(f"You scored {turn_score} points this turn.")
                    break

            print(f"Player {player + 1}'s total score: {scores[player]}")
            if scores[player] >= target_score:
                print(f"Player {player + 1} wins with a score of {scores[player]}!")
                return

# Run the game
if __name__ == "__main__":
    tuple_out_game()
