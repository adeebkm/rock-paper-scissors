from random import randint
print("Rock...")
print("Paper...")
print("Scissors...")

print("\nEnjoy!!!")
player = input("Player , make your move: ").lower()

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
    else:
        print("Computer WINS!!!")
elif player == "paper":
    if computer == "rock":
        print("Player WINS!!!")
    else:
        print("Computer WINS!!!")
elif player == "scissors":
    if computer == "paper":
        print("Player WINS!!!")
    else:
        print("Computer WINS!!!")
else:
    print("Please Enter a Valid Move!!!!")


