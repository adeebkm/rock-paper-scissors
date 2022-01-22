from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")

    print("\nEnjoy!!!")
    player = input("Player , make your move: ").lower()
    if player == "quit" or player == "q":
        break

    rand_num = randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"Computer played {computer}")

    if player == computer:
        print("It is a TIE!")
    elif player == "rock":
        if computer == "scissors":
            print("Player WINS!!!")
            player_wins +=1
        else:
            print("Computer WINS!!!")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player WINS!!!")
            player_wins +=1
        else:
            print("Computer WINS!!!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("Player WINS!!!")
            player_wins +=1
        else:
            print("Computer WINS!!!")
            computer_wins += 1
    else:
        print("Please Enter a Valid Move!!!!")


if player_wins > computer_wins:
    print("CONGRATS, YOU WON!")
elif player_wins == computer_wins:
    print("IT'S A TIE")
else:
    print("OH NO:( THE COMPUTER WON")
    
print(f"FINAL SCORES... Player: {player_wins} Computer: {computer_wins}")


