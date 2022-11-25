import random

def play():
    user = input("What is yor choice\n 'r' for rock, 'p' for paper, 's' for secissors:")
    computer = random.choice(['r','p','s'])
    print(f'Computer choose: {computer}')

    if user == computer:
        return 'It\'s a tie'
 
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())