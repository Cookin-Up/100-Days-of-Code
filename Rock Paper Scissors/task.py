rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

choices = ['rock', 'paper', 'scissors']

computer_choice = random.choice(choices)

player_choice = input("Choose 'rock', 'paper', or 'scissors': ")
player_choice = player_choice.lower()

if player_choice == 'rock':
    print(rock)
elif player_choice == 'paper':
    print(paper)
elif player_choice == 'scissors':
    print(scissors)
else:
    print("choose rock, paper or scissors")

if computer_choice == 'rock':
    print("computer chooses rock", rock)
elif computer_choice == 'paper':
    print("computer chooses paper", paper)
elif computer_choice == 'scissors':
    print("computer chooses scissors", scissors)

if player_choice == 'rock' and computer_choice =='rock':
    print("draw")
elif player_choice == 'scissors' and computer_choice =='rock':
    print("computer wins")
elif player_choice == 'paper' and computer_choice =='rock':
    print("player wins")
elif player_choice == 'rock' and computer_choice =='paper':
    print("computer wins")
elif player_choice == 'scissors' and computer_choice =='paper':
    print("player wins")
elif player_choice == 'paper' and computer_choice =='paper':
    print("draw")
elif player_choice == 'rock' and computer_choice =='scissors':
    print("player wins")
elif player_choice == 'scissors' and computer_choice =='scissors':
    print("draw")
elif player_choice == 'paper' and computer_choice =='scissors':
    print("computer wins")