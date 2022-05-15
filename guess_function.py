def guess_func(number_to_be_guessed, user_number):
    yes_no = input("Would you like a guess?")
    hint= ''
    if yes_no.lower() == 'yes':
        if ((user_number %2 == 0 and number_to_be_guessed %2 == 0) or (user_number %2 != 0 and number_to_be_guessed %2 != 0)) and number_to_be_guessed > user_number:
        
            hint = 'You guess should be higher than '
        elif ((user_number %2 == 0 and number_to_be_guessed %2 == 0) or (user_number %2 != 0 and number_to_be_guessed %2 != 0)) and number_to_be_guessed < user_number:
        
            hint = 'You guess should be lower than '
        elif user_number %2 == 0 and number_to_be_guessed %2 != 0:
            hint= 'The number is odd'
        elif user_number %2 != 0 and number_to_be_guessed %2 == 0:
            hint= 'The number is even'
    else:
        pass

    if number_to_be_guessed - user_number == 1 or user_number - number_to_be_guessed == -1:
        print("You are so close!")
    return hint

