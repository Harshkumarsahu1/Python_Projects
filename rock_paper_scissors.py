import random
player1 = ["Rock", "Paper", "Scissors"]
player2 = ["Rock", "Paper", "Scissors"]
player1_choice = random.choice(player1)
player2_choice = random.choice(player2)
print(f"Player 1 chooses: {player1_choice}")
print(f"Player 2 chooses: {player2_choice}")    
if player1_choice == player2_choice:
    print("It's a tie!")        
elif (player1_choice == "Rock" and player2_choice == "Scissors") or \
     (player1_choice == "Paper" and player2_choice == "Rock") or \
     (player1_choice == "Scissors" and player2_choice == "Paper"):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")