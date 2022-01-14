# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number,
#  then tell them whether they guessed too low, too high, or exactly right. 
#  (Hint: remember to use the user input lessons from the very first exercise)
import random


check_user_choice = True

user_choice = input('Guess number between 1 and 9 and, play y/Y : stop the game n/N ')
while check_user_choice:
    if user_choice in ('y','Y'):
        random_number = random.randint(1,9)
    
        user_number = int(input('Guess a number: '))

        if user_number == random_number:
            print('exactly right')
            user_choice = input(' play again y : stop the game n ')
        elif user_number > random_number:
            print('Your Guess is too high')
            user_choice = input(' play again y : stop the game n ')
        elif user_number < random_number:
            print('Your Guess is too low')
            user_choice = input(' play again y : stop the game n ')

    elif user_choice in ('n','N'):
        check_user_choice = False
        print('Thanks for playing')