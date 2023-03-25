from getpass import getpass as input

print("EPIC 🪨  📄 ✂️  BATTLE")

print("Select your move (R, P, or S)")

player1 = input("Player 1 > ")
player2 = input("Player 2 > ")

if player1 == "R" and player2 == "P":
  print("Player 1's 🪨  is smothered by Player 2's 📄!")
elif player1 == "P" and player2 == "S":
  print("Player 1's 📄 is teared by Player 2's ✂️!")
elif player1 == "S" and player2 == "R":
  print("Player 1's ✂️  is destroyed by player 2's 🪨!")
elif player1 == "P" and player2 == "R":
  print("Player 2's 🪨  is smothered by Player 1's 📄!")
elif player1 == "S" and player2 == "P":
  print("Player 2's 📄  is teared by Player 1's ✂️!")
elif player1 == "R" and player2 == "S":
  print("Player 2's ✂️  is broked by Player 1's 🪨!")
elif player1 == player2:
  print("It is a draw. Try again!")
else:
  print("Seems like someone put the wrong input. Try again!")