# 1 Which statement is a Tuple?

("Jim", "Jack", "Bill")

# 2 Which one is a Float?

2.0

2/4

# 3 Create a dictionary that prints out keys and values

names = {1: 'Derrik', 2: 'Steven', 3: 'Anna'}

for key, value in names.items():
    print(key, value)

print('---------------------------------------------------')
# 4 Create a class function of your top 3 Music Artist

class musicians:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def artist(self):
        print(f'{self.name} is a {self.country}')

musician1 = musicians('Radio', 'Ugandan')
musician2 = musicians('Fik Fameica', 'Ugandan')
musician3 = musicians('Chameleon', 'Ugandan')

musician1.artist()
musician2.artist()
musician3.artist()

# 5 Create a bubblesort Algorithm




# 6 Create an array and reshape it to 6-D array

# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#
# [[[[[[]]]]]]
#
# newarr = arr.reshape(2, 3, 2)

# print(newarr)


# 7 Which symbol returns a remainder?

# %

print('--------------------------------------------------')
# 8 Create a function that prints out only odd numbers,

def oddNums(x):
    for i in range(1, x):
        if i%2 == 1:


            print(i)
oddNums(int(input('Give a limit ')))

print('----------------------------------------------------')

# 9 Which statement gives you a syntax error?

# Print("Hello")

# 10 Create a list and find the total sum of the list


list1 = [2, 2, 5, 9, 12, 15]

sum = sum(list1)

print(sum)


print('----------------------------------------------')
# 11 Create a "T" shape object using the letter "T"

n = 6
t = 5
while n > 0:
    if n == 6:
        print('T '*t)
    if n != 6:
        print(' '*3,'T \r')

    n -= 1

z = 10
while z > 0:

    print(" \n")

    z -= 1








y = ('Jim', 'Jack', 'Bill')
print(f'y is of {type(y)}')


x = (4, 5, 7), (8, 9, 10)
print(f'x is of {type(x)}')

# print(f'x is of {type(x)}')