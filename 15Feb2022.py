# 1.2 friends want to play a dice game, but have lost the dice.
# Create a program to replace the dice. When the program is run, it should roll

from random import randint
num_of_players = int(input('Enter number of players '))
n = num_of_players
y = 1
while True:
    print('---------------------')
    print(f'player {y} to roll')
    play = input("enter 'r' to roll ")
    if play == 'r':
        num_Played = randint(1, 6)
        print('Your Dice value is', num_Played)
        y += 1

        if y > num_of_players:
            y = 1


    else:
        print('Thank you for playing')
        break


    player = 0
    num_Played = randint(1, 6)





# the dice and output the result of each dice.
#
# 2.Create a while loop that prints your name 5 times in uppercase letters.
#

name = 'Derrick'
n = 5
y = 0
while n > 0:
    y += 1
    print(f'{y}. {name.upper()}')
    n -= 1
# 3.Create a pyramid pattern object using the number 1.

