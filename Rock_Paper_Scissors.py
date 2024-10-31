import random
#function to get computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"]).lower()

#function to get determine the winner between the player and the computer (rules)    
def get_winner(player, computer):
    if player == computer:
        return "It's a TIE"
    elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        return "You WIN"
    else:
        return "You LOSE"
#function to initiate the game 
def gameplay():
    player_choice = (input("Input Your Choice (Rock / Paper / Scissors): ")).lower()
    if player_choice not in ("rock", "paper", "scissors"):
        return "Invalid Choice. Try Again."
    
    computer_choice = get_computer_choice()

    print(f"Computer chose: {computer_choice.capitalize()}")
    print(get_winner(player_choice, computer_choice))

gameplay()