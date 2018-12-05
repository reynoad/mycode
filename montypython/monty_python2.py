#!/usr/bin/env python3
round = 0
while(True):
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of -----"')
    answer = input()
    if (answer =='Brian' or 'brian'):
        print('Correct')
        break
    elif (answer == 'shruberry'):
        print('YOu gave the super secret answer!')
        break
    elif(round == 3):
        print('Sorry, the answer was Brian.')
        break
    else:
        print('Sorry! Try again!')