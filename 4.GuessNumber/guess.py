import random

# #guessing computers number
# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while (guess != random_number):
#         guess = int(input(f'Guess a number between 1 and {x}: '))
#         if guess < random_number:
#             print('Sorry, guess again. Too low.')
#         elif guess > random_number:
#             print('Sorry, guess again. Too high.')
    
#     print(f'Yoohoo, congrats. You have guessd the number {random_number} correctly!!!')

# guess(10)

#guessing our number by computer
def com_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print('Bohoo, The computer guessed your number, {guess}, correctly!!!')


com_guess(10)