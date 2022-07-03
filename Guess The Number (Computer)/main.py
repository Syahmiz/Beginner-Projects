import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))

        if guess < random_number:
            print('Sorry, the number is too low.')
        elif guess > random_number:
            print('Sorry, the number is too high.')

    print(f'Congratulation, you have guessed it right with the number {random_number}')

guess(10)