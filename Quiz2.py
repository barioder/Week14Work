# You are given a program with two inputs: one as password and
# the second one as password repeat. Complete and call the given function
# to output "Correct" if password and repeat are equal, and output "Wrong", if they are not.


def auth(password, repeat_password):
    if password == repeat_password:
        return 'Correct'
    else:
        return 'Wrong'


password = input('Please Enter password: ')
repeat_password = input('Repeat password: ')

print(auth(password, repeat_password))


print('----------------------------------------------------------------------  ')
# you are making a phonebook. The contacts are stored in a dictionary,
# where the key is the name and the value is a list, representing the
# number and the email of the contact. You need to implement search:
# take the name of the contact as input and output the email.
# If the contact is not found, output "Not found".

phonebook = {'derrick': [774455445, 'derr@gmail.com'],
                'steven': [772214554, 'steve@gmail.com']

             }


search = input('enter name ')
search = search.lower()
names = []

for i in phonebook.keys():
    names.append(i)

if search in names:
    list_value = phonebook[search]
    print(list_value[1])

else:
    print('Not found')

print('--------------------------------------------------------------------------------')

# Create a nesting list that prints out the color and the car brand.

list2 = [['Blue', 'Benz'], ['Green', 'Jeep'], ['Yellow', 'Subaru']]

for i in list2:
    print(i)

print('--------------------------------------------------------------------------------')
# Create a game that the user plays the computer(CPU).

import random

user_play = int(input('Guess a number between 1 and 10 '))

pc_play = random.randint(1, 11)

if user_play == pc_play:
    print('User wins')
else:
    print('Play Again')
    print(f'Pc guessed {pc_play}')

print('--------------------------------------------------------------------------------')

# Create a lists called daysoftheweek = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
# you only could print out 3 days out that list.

daysoftheweek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

n = 3
while n > 0:


    print(daysoftheweek[n])

    n -= 1


# Bonus Question: Algorithm challenge: Create your own sorting algorithm.