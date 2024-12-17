import random 

# introduction to the program

print("\n[    TUPLE OUT    ]\n",
      "_____________________________________________\n",
        "\n\n")


# How many points would you like to play till? 
  # can not exceed 500, can not be lower than 10

continue_loop2 = True

while continue_loop2: 
    points = input("How many points would you like to play to?\n")
    int(points) 
    try:
      if int(points) <= 500 and int(points) >= 10: 
        point_confirm = f"The game will end when one of the players earns {points} points"
        print(point_confirm)
        continue_loop2 = False
      else: 
        point_confirm = f"The points must be between 10 to 500, no more and no less!"
        print(point_confirm)
    except ValueError: 
      print("Please enter an integer!")
  

# Rules of the game

print(f"""\n\n[    RULES   ]\n
      ______________________________________________________________________________________________________\n
      1. Player 1 rolls 3,  6 sided die
      2. if all the rolled dice end up being the same number, the player earns zero points and tuples out
      3. if two of the dice roll to be the same value, they can not be re-rolled and remain those numbers 
      4. Player 1 continues to roll the final dice as often as they like, attempting to get a high number that is NOT the same as the previous 2 die
      5. If the player is satisifed with their roll, they earn all the points
      6. If the player rolls the same number as the previous two dice, they tuple out and earn 0 points 
      7. Player 2 begins their roll
      8. First to {point_confirm} points wins! 
      ______________________________________________________________________________________________________""")


# define the die
# rolls 3 times and produces the results as a list

def roll_dice(num_dice): 
  """
  Given a number of dice, this function rolls any amount of die, 
  returning all the rolls as a list named rolls
  """
  roll = random.choices(range(1,7), k = num_dice) 
  print(f"you rolled {roll}")
  return roll

# # TESTS 
# roll_dice() ## no k =, no return
# type(roll_dice(4)) ## type list
# roll_dice(7) ## works YAYAYYAYA

# create a function to check for tupled die
def check_fixed(roll):
  """
  This function evaluates the dice roll outcomes and returns the fixed rolls and die that can be rerolled 
  """
  reroll = []
  if roll[0] == roll[1] and roll[1] == roll[2]:
    print("tupled! All dice are fixed")
  elif roll[0] == roll[1]:
    reroll = [roll.pop(2)]
    fixed_roll = roll
  elif roll[0] == roll[2]:
    reroll = [roll.pop(1)]
    fixed_roll = roll
  elif roll[1] == roll[2]:
    reroll = [roll.pop(0)]
    fixed_roll = roll
  else:
    reroll = roll
    fixed_roll = []
  
  print(f"{fixed_roll} can not be rerolled, {reroll} can be rerolled.")
  return fixed_roll, reroll

# TESTS
# roll = roll_dice(3)
# fixed_roll, reroll = check_fixed(roll)
# print(fixed_roll, reroll )


# main code
# Initialize players in a dictionary 

player_scores = {
   "Player 1": 0, 
   "Player 2": 0
   }
current_player = "Player 1" # set current player so it can alternate 

while all(score < int(points) for score in player_scores.values()): # loops until score >= points
    print(f"\n{current_player}'s turn!")

    roll_confirm = input(f"\n{current_player}, press 'r' to roll\n").lower()
    if roll_confirm == 'r':
        roll = roll_dice(3)  # Player rolls 3 dice
        fixed_roll, reroll = check_fixed(roll)  # Checks for fixed and rerolled dice
        
        while reroll:
            reroll_input = input("\nWould you like to reroll the remaining dice? [Y/N]\n").lower()
            if reroll_input == 'y':
                # Reroll only the dice that are left
                roll = fixed_roll + roll_dice(len(reroll))
                fixed_roll, reroll = check_fixed(roll)
            else:
                break  # Stop rerolling if player chooses not to reroll
        
        # Sum the points from the fixed dice (the dice that are not rerolled)
        round_score = sum(fixed_roll)
        player_scores[current_player] += round_score
        print(f"\n{current_player}'s score after this turn: {player_scores[current_player]}")
    
    else:
        print("\nInvalid input, moving to the next player.")

    # Check if the current player has won
    if player_scores[current_player] >= int(points):
        print(f"\n\n{current_player} wins with {player_scores[current_player]} points!")
        break

    # Switch to the other player
    current_player = "Player 2" if current_player == "Player 1" else "Player 1"
