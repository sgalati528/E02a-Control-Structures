#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')#prints 'Greetings' in window
colors = ['red','orange','yellow','green','blue','violet','purple']#list of colors
play_again = ''#establishing empty variable
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'):#if the player has not said no to playing again
    match_color = random.choice(colors)#selects a random string from the list of
    #colors to put in the variable match_color
    count = 0#makes variable count 0
    color = ''#establishing empty variable
    while (color != match_color):#while the color entered doesn't =match_varible
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()#strips color of letter cases
        count += 1#adds 1 to count
        if (color == match_color):#if the color entered matches match_color
            print('Correct!')#prints 'Correct!' in window
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
#prints 'Sorry, try again. You have guessed (number in var. count) times.' in window
    print('\nYou guessed it in {} tries!'.format(count))#prints 'You guessed it in
    #(numberin var. count) tries!' on a new line'

    if (count < best_count):#if the count is lower than the best_count
        print('This was your best guess so far!')#prints 'This was your best guess so far!'
        #in window
        best_count = count#changes best_count to previous count

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()
#asks player if they want to play again and they would type 'yes' or 'no' in response
print('Thanks for playing!')#prints 'Thanks for playing!' in window
