import random


while True:
    option = ["Rock", "Paper", "Scissors"]
    print ("\n It is Game time!!!\n")
    computer = random.choice(option)

    player = None
    while player not in option:
        player = input("Rock, Paper, Scissors? \n").capitalize()
        
    
    if player == computer:
        print ("CPU:",computer, "Player:",computer, "\n It is a tie.\n")

    if player == "Rock":
        if computer == "Paper":
            print ("CPU:",computer, "Player:",player, "\n You lose")
        if computer == "Scissors":
            print ("CPU:",computer, "Player:",player, "\n You win")

    elif player == "Paper":
        if computer == "Scissors":
            print ("CPU:",computer, "Player:",player, "\n You lose")
        if computer == "Rock":
            print ("CPU:",computer, "Player:",player, "\n You win")

    elif player == "Scissors":
        if computer == "Rock":
            print ("CPU:",computer, "Player:",player, "\n You lose")
        if computer == "Paper":
            print ("CPU:",computer, "Player:",player, "\n You win")

    play_again = input("Play Again? (Yes/No): \n ").lower()
    if play_again != "yes":
        break

print ("Game Over")