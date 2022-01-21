print("Rock...")
print("Paper...")
print("Scissors...")

print("\nRULES:\n1)input should be in lowercase\n2)Dont cheat")

player1 = input("Player 1, make your move: ")
print("***************NO CHEATING!!***************\n" * 20)
player2 = input("Player 2, make your move: ")


if player1 == "rock":
    if player2 == "scissors":
        print("Player 1 WINS!!!")
    elif player2 == "paper":
        print("Player 2 WINS!!!")
elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 WINS!!!")
    elif player2 == "scissors":
        print("Player 2 WINS!!!")
elif player1 == "scissors":
    if player2 == "paper":
        print("Player 1 WINS!!!")
    elif player2 == "rock":
        print("Player 2 WINS!!!")
elif player1 == player2:
    print("It is a TIE!")
else:
    print("something went wrong\nCHECK RULES!!!!")


