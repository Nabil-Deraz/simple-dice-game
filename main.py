# Needed to create random numbers to simulate dice roll
import random

# Initialise player scores to 0
p1_score = 0
p2_score = 0

# Repeat game 10 times
for i in range(5):

  # Generate random numbers between 1 and 6 for each player.
  p1_value = random.randint(1, 6)
  p2_value = random.randint(1, 6)

  # Display the values
  print("Player 1 rolled: ", p1_value)
  print("Player 2 rolled: ", p2_value)

  # Selection: based on comparison of the values, take the appropriate path through the code.
  if p1_value > p2_value:
    print("player 1 wins.")
    player1_score = p1_score + 1  # This is how we increment a variable
  elif p2_value > p1_value:
    print("player 2 wins")
    p2_score = p2_score + 1
  elif p1_value==p2_value:
     p1_value = random.randint(1, 6)
     p2_value = random.randint(1, 6)

  input("Press enter to play another round")  # Wait for user input to proceed.

print("Game Over")
if (p1_score > p2_score):
  print("Player 1 wins with score: ", p1_score,
        ",and Player 2 score is: ", p2_score)

else:
  print("Player 2 wins with score:  ", p2_score,
        ",and Player 1 score is: ", p1_score)
