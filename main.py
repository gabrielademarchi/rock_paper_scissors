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

options = [rock, paper, scissors]
options_str = ['r', 'p', 's']

player_index = int(input(
    'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))

if (player_index >= 3 or player_index < 0):
    print('You typed an invalid number, you lose!')
else:
    player = options[player_index-1]
    computer_choice = random.randint(0, 2)
    computer = options[computer_choice]

    player_str = options_str[player_index-1]
    computer_str = options_str[computer_choice]

    print(player)
    print('Computer chose:')
    print(computer)

    if (player_str == 'r' and computer_str == 's') or (player_str == 's' and computer_str == 'p') or (player_str == 'p' and computer_str == 'r'):
        print('You win!')
    elif player_str == computer_str:
        print('It\'s a draw')
    else:
        print('You lose')
