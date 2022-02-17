import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print('shape of array')
print(a.shape)

print('reshape')
print(a.reshape(3, 2))

print('flatten the array')

print(a.ravel())

print('Transpose')
print(a.transpose())

# arange

z = np.arange(0, 20, 2)

print(z)
print(z.reshape(2, 5))
h = np.arange(15)

print(h)

y = np.arange(1, 20, 2)

print(y)

# indexing arrays

b = np.array([[1, 2, 3], [4, 5, 6]])

print(b[0][2])
print(b[1])




# create a function that tranforms an array from rows to columns

def trans(array):
    return array.transpose()


c = np.array([[2, 5, 6, 10], [12, 14, 18, 20]])

print(trans(c))

print('-------------------------------------------------')
# create an array, using the if statment find out if the number of dimensions is correct

array1 = np.array([[[2, 6, 7, 10], [11, 25, 27, 30]]])

if array1.ndim == 4:
    print('Correct Number of dimensions')

else:
    print('Not the correct number of dimensions')


print('-------------------------------------------------')
# convert a list into an array and add two brackets to that new array

list1 = [1, 3, 5, 8, 10, 12]


array2 = np.array(list1, ndmin = 2)
print(array2)

# print(array2.reshape(2, 3))


print('-------------------------------------------------')
# create 2 d arrays and multiply each of them

array_a = np.array([[1, 2, 3], [4, 5, 6]])
array_b = np.array([[7, 9, 10], [12, 14, 17]])

print(array_a * array_b)

print('-------------------------------------------------')

# create a right side triangle using the sign $
n = input('Enter number of rows ')
z = 1
for i in range(int(n)):
    print('$'*z)
    z += 1
