# 1. Create a 2-D array and using a funtion print out the number of dimension of that array.
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])


def tell_dim(array):
    print('The number of dimensions is ', array.ndim)

tell_dim(a)

print('---------------------------------------------------')
# 2. You need to make a program that counts the number of vowels in a given text. The vowels are
# a,e,i,o,u.
# Take a string as input and output the number of vowels.


vowels = ['a', 'e', 'i', 'o', 'u']

input_Text = input('Enter a word to tell the number of vowels in it: ')

num_Vowels = 0

for letter in input_Text.lower():
    if letter in vowels:
        num_Vowels += 1

print(f'The number of vowels in \"{input_Text}" is {num_Vowels}')

print('---------------------------------------------')

# 3.Create a upside down pyamid object pattern using binary numbers "1,0".


n = 0
x = 7
index = 0
while n < 7:
    print(' ' * n, end='')
    binary = [1, 0]
    v = x - n
    while v > 0:
        print(binary[index], end='')
        index += 1
        if index == 2:
            index = 0

        v -= 1
    print()
    n += 1
    x -= 1
