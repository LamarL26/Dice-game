# Lamar Logan
# INST126
# Prof. Jackson
# 12/14/2024

# Tuple Out Dice Game

# Description
"Tuple Out" is a turn-based dice game where players aim to reach a target score by rolling three dice per turn. The game includes strategic decisions like re-rolling dice and avoiding a "tuple out" (all three dice showing the same number). Perfect for competitive fun with 2–5 players!

---

How to play:
1. Players take turns rolling three dice.
2. If all three dice show the same number, the player "tuples out" and scores 0 for the round.
3. If two dice match, they are fixed and cannot be re-rolled.
4. Players can re-roll the remaining dice up to 2 additional times or stop early.
5. The score for a turn is the sum of the three dice unless the player tuples out.
6. The first player to reach or exceed the target score wins!

---

# Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/tuple-out.git
   ```
2. Navigate to the project directory:
   ```bash
   cd tuple-out
   ```
3. Ensure you have Python installed (version 3.6+ recommended).

4. Run the game:
   ```bash
   python Lamar's_Final_Tuple_Out.py
   ```

---

# Usage
1. Start the game by answering 'Y' to play or 'N' to exit.
2. Enter the number of players (2–5).
3. Input the names of all players.
4. Set a target score between 25 and 300.
5. Players take turns rolling the dice and trying to maximize their score.
6. The game announces the winner once a player reaches or exceeds the target score.

---

# Features
- Multiplayer Support: Play with 2–5 players.
- Custom Target Score: Adjust the winning score between 25 and 300.
- Strategic Gameplay: Decide whether to re-roll or stop to optimize your score.
- Randomized Dice Rolls: Adds an element of chance to each turn.

---

# Example
Here's a sample session:

```
Welcome to the 'Tuple Out' Dice Game!
______________________________________

Rules:
- Roll three dice per turn.
- If all three dice are the same, you 'tuple out' and score 0 for the round.
- If two dice are the same, they are fixed and cannot be re-rolled.
- Choose a score between 25 and 300 to play up to.
- You may roll up to 3 times per turn.
- Your score for the turn is the sum of the three dice.

Do you want to play the game? (Y/N): Y
Enter the number of players (2-5): 3
Enter the name of Player 1: Alice
Enter the name of Player 2: Bob
Enter the name of Player 3: Charlie
Enter the target score (between 25 and 300): 50

Alice's Turn!
Initial Roll: [3, 4, 4]
Fixed dice: [(2, 4), (3, 4)]
Roll #2: Enter 'roll' to roll the dice again, or 'stop' to stop: roll
New Roll: [5, 4, 4]
Alice ends the turn with a score of 13.

Current Scores: {'Alice': 13, 'Bob': 0, 'Charlie': 0}
```

---

# Contributing
Contributions are welcome! I'm open to taking constructive feedback. :
1. Fork this repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request for review.

---

# License
This project is licensed under the MIT License. 
