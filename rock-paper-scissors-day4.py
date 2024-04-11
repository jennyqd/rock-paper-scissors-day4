
import random

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

list = [rock, paper, scissors]

player1_input = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors. \n"))

print(player1_input)
print(list[player1_input])


player2_input = random.randint(0, 2)
print(player2_input)
print(list[player2_input])


if player1_input == player2_input:
    print("It's a draw")
elif player1_input == 0 and player2_input == 2:
    print("You win")
elif player1_input == 1 and player2_input == 0:
    print("You win")
elif player1_input == 2 and player2_input == 1:
    print("You win")
else:
    print("You lose")







# Rock wins against scissors 
# Scissors wins against paper
# Paper wins against rock 