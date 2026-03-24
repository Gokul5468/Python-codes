import random
def get_choices():
 player_choice = input("Enter a choice(rock,paper,scissors):")
 computer_options = ["rock","paper","scissor"]
 computer_choice = random.choices(computer_options)
 choices = {"player": player_choice,"computer":computer_choice}
 return choices

choices= get_choices()
print(choices)
