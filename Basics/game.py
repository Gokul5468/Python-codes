import random
def get_choices():
 player_choice = input("Enter a choice(rock,paper,scissor): ")
 computer_options = ["rock","paper","scissor"]
 computer_choice = random.choice(computer_options)
 choices = {"player": player_choice,"computer":computer_choice}
 return choices

# choices= get_choices()
# print(choices)

def check_win(player,computer):
    print(f"you choose {player} ,computer choose {computer}")
    if player == computer:
        return "it is tie!"
    elif player == "rock":
     if computer == "scissor":
        return "rock smahes scissor! you win!"
     else:
        return "paper covers the rock! you loose."
    elif player == "paper":
     if computer == "rock":
        return "paper cover rock! you win!"
     else:
        return "scissor cuts paper! you loose."
    elif player == "scissor":
     if computer == "paper":
        return "scissor cuts paper! you win!"
     else:
        return "rock breaks scissor! you loose."

choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)

