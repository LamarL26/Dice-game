import random

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
    dice = [roll_dice(), roll_dice(), roll_dice()]
    print(f"Initial Roll: {dice}")

    # Check for tuple out (all three dice are the same)
    if dice[0] == dice[1] == dice[2]:
        print("Tuple out! No points this turn.")
        return 0

    rolls = 1  # Tracks the number of rolls (starts at 1 since the first roll is done)

    while rolls < 3:
        
        fixed = {i for i in range(3) if dice.count(dice[i]) > 1}
        print(f"Fixed dice: {[(i + 1, dice[i]) for i in fixed]}")
        # Identify fixed dice (if two dice are the same, they cannot be re-rolled)

        # Ask player to re-roll or stop
        choice = input(f"Roll #{rolls + 1}: Enter 'roll' to roll the dice again, or 'stop' to stop: ").strip().lower()
        if choice == 'stop':
            break
        elif choice == 'roll':
            for i in range(3):
                if i not in fixed:
                    dice[i] = roll_dice()
            print(f"New Roll: {dice}")
            rolls += 1  
            # Increment the roll count

            
            if dice[0] == dice[1] == dice[2]:
                print("Tuple out! No points this turn.")
                return 0
            # Check for tuple out again
        else:
            print("Invalid choice. Please enter 'roll' or 'stop'.")

    
    score = sum(dice)
    print(f"{player_name} ends the turn with a score of {score}.")
    return score
# Calculate score from dice

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
            score = int(input("\nEnter the target score (between 100 and 500): "))
            if 100 <= score <= 500:
                return score
            else:
                print("Score must be between 100 and 500.")
        except ValueError:
            print("Invalid input. Please enter a number.")


print("Welcome to the 'Tuple Out' Dice Game!")
print("Rules:")
print("- Roll three dice per turn.")
print("- If all three dice are the same, you 'tuple out' and score 0 for the round.")
print("- If two dice are the same, they are fixed and cannot be re-rolled.")
print("- You may roll up to 3 times per turn.")
print("- Your score for the turn is the sum of the three dice.")
# Game introduction


player_choice = input("\nDo you want to play the game? (yes/no): ").strip().lower()
if player_choice != "yes":
    print("Maybe next time. Goodbye!")
    exit()
    # Prompt to start the game


players = get_player_names()
target_score = get_target_score()
# Get players and target score


scores = {player: 0 for player in players}
# Initialize player scores

# Game loop
game_running = True
while game_running:
    for player in players:
       
        scores[player] += play_turn(player)
        print(f"Current Scores: {scores}")
         # Add points from the player's turn to their total score

        
        if scores[player] >= target_score:
            print(f"\n{player} wins the game with {scores[player]} points!")
            game_running = False
            break
        # Check for winning condition


print("\nFinal Scores:")
for player, score in scores.items():
    print(f"{player}: {score}")
print("The Game is over! Thanks for playing!")
# Final Scores