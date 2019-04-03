import random

choices = ['rock', 'paper', 'scissors']
keep_playing = True

while keep_playing:
    computer_choice_index = round(random.random() * 2)
    computer_choice = choices[computer_choice_index]

    human_choice = input('Choose your weapon...\n').lower()

    while human_choice not in choices:
        human_choice = input('Invalid choice. Please choose again.\n').lower()

    win_conditions =[
        ('rock', 'scissors'),
        ('scissors', 'paper'),
        ('paper', 'rock')
    ]

    if (human_choice, computer_choice) in win_conditions:
        winner = 'Player'
    elif (computer_choice, human_choice) in win_conditions:
        winner = "Computer"
    else:
        winner = None

    print(f'\nPlayer chose {human_choice}')
    print(f'Computer chose {computer_choice}\n')

    if winner:
        print(f'Winner is {winner}!\n\n')
    else:
        print('Its a tie!\n\n')

    continue_key = input('Type "q" to quit, type anything else to continue\n\n').lower()
    if continue_key == 'q':
        print('Thank you for playing :)')
        keep_playing = False





