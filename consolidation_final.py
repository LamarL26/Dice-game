import random #Imports random to use to generate random numbers generated on a 6 sided die.

import numpy as np #Imports numpy and uses np to call it in the program

import time #Imports time to be used to create suspense and tell the player how long they have been playing the game.

start_time = time.time() #creates a timer when the program starts

avg_score_array = np.array([]) #initializes an array using numpy that is GOING to be used to average out the scores of player1 and player 2 per round

def dicegame(): #turns the code below into a function so that it can be used multiple times

    diceroll = [random.randint(1,6), random.randint(1,6), random.randint(1,6)] #used to create the first 3 generated random values that each player gets

    print(diceroll)

    number_question = ""

#Creates string values of numbers as well as an exit to give a player multiple opportunities to reroll whichever dice they want if all 3 numbers are different
    while (diceroll[0] != diceroll[1] and diceroll[0] != diceroll[2] and diceroll[1] != diceroll[2] and number_question != "EXIT" ):
        number_question = input("At which index of the number would you like to reroll? Type EXIT if you want to keep your numbers. ")
        if (number_question) == "0":
            diceroll[0] = random.randint(1,6)
        elif (number_question) == "1":
            diceroll[1] = random.randint(1,6)
        elif (number_question) == "2":
            diceroll[2] = random.randint(1,6)
        print (diceroll)

#If-elif statements with a while loop that allows a player to reroll the last remaining dice if the other two dice values are the same. 
#If all 3 values end up being the same, 0 points are earned.
#The while loops below take into account if the user does not input N and checks if dice at specific indices are the same.

    if diceroll[0] == diceroll[1] == diceroll[2]:
        print("Oh no. Unlucky!. You have scored 0 points!")
        diceroll = [0,0,0]

    elif diceroll[0] == diceroll[1]:
        print("The matching numbers can not be changed.")
        question = input("Would you like to roll the remaining dice? Press Y for yes or N for no. *REMEMBER* if this last number is equal to the remaining numbers, your points will be 0. ")

        while diceroll[2] != diceroll[1] and question.upper() != "N": 
                if question.upper() == "Y":
                    diceroll[2] = random.randint(1,6)
                    print (f"Updated: {diceroll}")
                    if diceroll[0] == diceroll[1] == diceroll[2]:
                        print("Oh no. Unlucky!. You have scored 0 points!")
                        diceroll = [0,0,0]
                    else:
                        question = input("Would you like to roll the remaining dice? Press Y for yes or N for no. *REMEMBER* if this last number is equal to the remaining numbers, your points will be 0. ")
                else: question = input("Please type Y or N!")

    elif diceroll[0] == diceroll[2]:
        print("The matching numbers can not be changed.")
        question = input("Would you like to roll the remaining dice? Press Y for yes or N for no. *REMEMBER* if this last number is equal to the remaining numbers, your points will be 0. ")

        while diceroll[1] != diceroll[0] and question.upper() != "N":
                if question.upper() == "Y":
                    diceroll[1] = random.randint(1,6)
                    print (f"Updated: {diceroll}")
                    if diceroll[0] == diceroll[1] == diceroll[2]:
                        print("Oh no. Unlucky!. You have scored 0 points!")
                        diceroll = [0,0,0]
                    else:
                        question = input("Would you like to roll the remaining dice? Press Y for yes or N for no. *REMEMBER* if this last number is equal to the remaining numbers, your points will be 0. ")
                else: question = input("Please type Y or N!")

    elif diceroll[1] == diceroll[2]:
        print("The matching numbers can not be changed.")
        question = input("Would you like to roll the remaining dice? Press Y for yes or N for no. *REMEMBER* if this last number is equal to the remaining numbers, your points will be 0. ")

        while diceroll[0] != diceroll[1] and question.upper() != "N":
                if question.upper() == "Y":
                    diceroll[0] = random.randint(1,6)
                    print (f"Updated: {diceroll}")
                    if diceroll[0] == diceroll[1] == diceroll[2]:
                        print("Oh no. Unlucky!. You have scored 0 points!")
                        diceroll = [0,0,0]
                    else:
                        question = input("Would you like to roll the remaining dice? Press Y for yes or N for no. *REMEMBER* if this last number is equal to the remaining numbers, your points will be 0. ")
                else: question = input("please type Y or N!")
    #Creates the final result per player and prints out an fString.
    final_result = diceroll[0] + diceroll[1] + diceroll[2]
    global avg_score_array  #Set global variable to use the avg_score_array that is outside of the function
    avg_score_array = np.append(avg_score_array, final_result) #creates an array that adds in the average score of each round from the final result value
    print(f"This is the final sum of your 3 dice rolls {final_result}.") 
    return final_result

    
#Based off of the function created above, 2 players are created below.

def five_rounds(): #Creates a function called five_rounds that calls the dicegame function for two players

    print("player_one_turn")
    player_one_result = dicegame()

    print("Player_two_turn")
    player_two_result = dicegame()

    #Prints a final statement saying which player had a greater score leading to a win!
    if (player_one_result > player_two_result):
        print (f"{player_one_result} > {player_two_result} Player one wins!")
        return "Player One won"
    elif (player_one_result < player_two_result):
        print (f"{player_one_result} < {player_two_result} Player two wins!")
        return "Player Two won"
    else:
        print("You both tied")
        return "Players tied"
    
player_one_wins = 0 #initializes the amount of wins player one has won

player_two_wins = 0 #initializes the amount of wins player two has won

#for loop that adds 1 win depending on the player score per round.
for games_played in range(1,5):
     print("Game number: " + str(games_played))
     result = five_rounds()
     if (result == "Player One won"):
          player_one_wins += 1
     elif (result == "Player Two won"):
          player_two_wins += 1

#String values that are printed depending on which player has won more rounds.
if (player_one_wins > player_two_wins):
     print ("Player one won more rounds")
elif (player_one_wins < player_two_wins):
     print ("Player two won more rounds")
else:
     print ("You both tied together!")

#Boolean statement that changes depending on if the average score per round per player is greater than the average of rolling 3 dice (10.5).
above_average = False
if (np.average(avg_score_array) > 10.5):
     above_average = True
if (above_average):
    time.sleep(3) # Timer that is used to create suspense to see if the players average score is greater than 10.5.
    print("The average score for all of your games was: " + str(np.average(avg_score_array)) + ". This is above the average sum of 3 dice which is 10.5")
else:
    time.sleep(3)
    print("The average score for all of your games was: " + str(np.average(avg_score_array)) + ". This is equal to or below the average sum of 3 dice which is 10.5")

end_time = time.time() #Timer that is used to store the time that the game ended.

whole_time = end_time - start_time #The difference between the end and start times tells the player in seconds how long they played the game for.

print ("You played the dice game for " + str(whole_time) + " seconds.")

    
