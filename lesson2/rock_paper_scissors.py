import random
import getpass
import csv


choices = ['rock', 'paper', 'scissors']
keep_playing = True
player_count = 0
player2_count = 0
computer_count = 0
h_or_c = ('h','c')
scoreboard_dict = {'Player1 Score' : '0', 'Computer Score' : '0'}
against_human_or_computer = input("Are you playing against human(h) or computer(c)? ").lower().strip()
while against_human_or_computer not in h_or_c:
    print("please enter 'h' or 'c'")
    against_human_or_computer = input("Are you playing against human(h) or computer(c)? ").lower().strip()

while keep_playing:
    computer_choice_index = round(random.random() * 2)
    computer_choice = choices[computer_choice_index]

    human_choice = getpass.getpass('Choose your weapon player1...\n').lower()

    while human_choice not in choices:
        human_choice = getpass.getpass('Invalid choice player1. Please choose again.\n Choose between rock, paper or scissors \n').lower()

    win_conditions = [
        ('rock', 'scissors'),
        ('scissors', 'paper'),
        ('paper', 'rock')
    ]

    if against_human_or_computer == 'c':
        computer_choice_index = round(random.random() * 2)
        computer_choice = choices[computer_choice_index]

        if (human_choice, computer_choice) in win_conditions:
            winner = 'Player'
            player_count += 1
            scoreboard_dict['Player1 Score'] = player_count
        elif (computer_choice, human_choice) in win_conditions:
            winner = "Computer"
            computer_count += 1
            scoreboard_dict['Computer Score'] = computer_count
        else:
            winner = None
        print(f'\nPlayer chose {human_choice}')
        print(f'Computer chose {computer_choice}\n')
        if winner:
            print(f'Winner is {winner}!\n\n')
        else:
            print('Its a tie!\n\n')

        for key, value in scoreboard_dict.items():

            print(key,value)

    elif against_human_or_computer == 'h':
        if 'Player2 Score' not in scoreboard_dict.keys():
            scoreboard_dict.update({'Player2 Score': '0'})
        player2_choice = getpass.getpass('Choose your weapon player2...\n').lower()
        while player2_choice not in choices:
            player2_choice = getpass.getpass('Invalid choice player2. Please choose again.\n Choose between rock, paper or scissors\n').lower()
        if (human_choice, player2_choice) in win_conditions:
            winner = 'Player1'
            player_count += 1
            scoreboard_dict['Player1 Score'] = player_count
        elif (player2_choice, human_choice) in win_conditions:
            winner = "Player2"
            player2_count += 1
            scoreboard_dict['Player2 Score'] = player2_count

        else:
            winner = None
        print(f'\nPlayer1 chose {human_choice}')
        print(f'Player2 chose {player2_choice}\n')
        if winner:
            print(f'Winner is {winner}!\n\n')
        else:
            print('Its a tie!\n\n')

        if 'Computer Score' in scoreboard_dict.keys():
            del scoreboard_dict['Computer Score']
        for key, value in scoreboard_dict.items():

            print(key,value)



    continue_key = input('Type "q" to quit, type anything else to continue\n\n').lower()
    if continue_key == 'q':
        print('Thank you for playing :)')
        keep_playing = False

    with open('scores.csv', 'w') as f:
        for key in scoreboard_dict.keys():
            f.write("%s,%s\n" % (key, scoreboard_dict[key]))


