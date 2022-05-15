import numpy as np
from guess_function import *


number_to_be_guessed = np.random.randint(0,21)
print(number_to_be_guessed)

def ask_user_for_number():
    user_guess = int(input("Enter a number \n"))
    return user_guess


def game():
    user_guess = ask_user_for_number()
    if number_to_be_guessed == user_guess:
        print("Wow you guessed it! \n")
        exit
    else:
        
        print("Oooh! Guess again")
        while number_to_be_guessed != user_guess:
                user_guess = ask_user_for_number()
                if number_to_be_guessed == user_guess:
                    print("Correct!")
                    exit()
                print('Ohh! That is not right. Please try again')
                print(guess_func(number_to_be_guessed,user_guess))


game()    



