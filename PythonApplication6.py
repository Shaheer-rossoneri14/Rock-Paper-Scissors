'''Rock, Paper and Scissor 
1. Classic Rock, Paper and Scissor game.
2. You play against Computer.
3. Rock beats Scissors but loses to Paper.
4. Paper beats Rock but loses to Scissors.
5. Scissors beat Paper but loses to Rock.'''

import random
play_game = input('Are you ready?(y/n): ')

if (play_game == 'y'):
    c_answer = random.choice(['rock', 'paper', 'scissors'])
    u_answer = input('Choose one: rock, paper or scissors: ')
    c_point=0
    u_point=0

    if (c_answer == u_answer):
        c_point=c_point+0
        u_point=u_point+0
    elif (c_answer == 'rock'):
        if (u_answer == 'paper'):
            u_point=u_point+1
        else:
            c_point=c_point+1
    elif (c_answer == 'paper'):
        if (u_answer == 'rock'):
            c_point=c_point+1
        else: 
            u_point=u_point+1
    elif (c_answer == 'scissors'):
        if (u_answer == 'paper'):
            c_point=c_point+1
        else: 
            u_point=u_point+1
    else:
        print('Wrong input')

    if (c_point>u_point):
        print('Computer won by ' + str(c_point) + ' points. ')
    else:
        print('User won by ' + str(u_point) + ' points. ')

if (play_game == 'n'):
    print('Goodbye')
