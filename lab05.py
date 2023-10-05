"""
Author:         Landon Thomas
Date:           10/4/23
Assignment:     Lab 05
Course:         CPSC1051
Lab Section:    004

CODE DESCRIPTION:
This code is intended to prompt the user to enter a square size and enter the correct values of a magic square.
The code will then display the user created square and determine if it is magic or not, as well as verifying
if the sqaure is of the correct format.
"""

print("Welcome to the Magic Square!")

print('Enter in the magic square size you would like:')
size = int(input())
while size <= 0:
    print('Please enter in a number that is greater than 0')
    print('Enter in the magic square size you would like:')
    size = int(input())

magic_number = (size / 2) * (size**2 + 1)
print(f'The magic number for size {size} is {magic_number:.0f}.')

print('Enter in the values separated by spaces: ')
list1 = input()
list_1 = []
for i in list1.split():
    list_1.append(int(i))

print('Your square:')
"""declare square/2D list and place values into it"""
input_square = [[ '' for i in range(size)] for j in range(size)]
num = 0
for i in range(size):
    for j in range(size):
        input_square[i][j] = list_1[num]
        num += 1
"""display square"""
for i in range(size):
    for j in range(size):
        print(input_square[i][j], end='')
    print()
square_value = True
"""determine if square has correct input"""
count = 0
for i in range(1, size**2 + 1):
    list_1.count(i)
    if list_1.count(i) == 1:
        count += 1

if count != size**2:
    square_value = False
    print(f'The input cannot be a magic square! There must be one of each value from 1 to {size**2}.')
"""determine sums of rows and validate them"""
num_row = 0
for row in input_square:
    if sum(row) != magic_number:
        square_value = False
        print(f'Row {num_row} does not work! These are the values in row {num_row}: ', end = '')
        for col in row:
            print(f'{col} ', end = '')
    num_row += 1
    print()

"""determine sums of columns and validate them"""
col_num = 0
sum = 0
for x in range(size):
    column = []
    for i in range(size):
        for j in range(size):
            if j == (col_num):
                column.append(input_square[i][j])
                sum += input_square[i][j]
    if sum != magic_number:
        square_value = False
        print(f'Column {col_num} does not work! These are the values in column {col_num}: ', end = '')
        for y in range(size):
            print(f'{column[y]} ', end ='')
        print()
    col_num += 1
    sum = 0
"""validate the first diagonal"""
diag1 = []
sum_diag1 = 0
for i in range(size):
    for j in range(size):
        if i == j:
            diag1.append(input_square[i][j])
            sum_diag1 += input_square[i][j]


if sum_diag1 != magic_number:
    square_value = False
    print('Diagonal 1 does not work! ')
    print('These are the values in diagonal 1: ', end = '')
    for i in range(size):
        print(f'{diag1[i]} ', end = '')
    print()

"""validate second diagonal"""
diag2 = []
sum_diag2 = 0
num2 = size - 1
for i in range(size):
    for j in range(size):
        if j == num2:
            diag2.append(input_square[i][j])
            sum_diag2 += input_square[i][j]
    num2 -= 1

if sum_diag2 != magic_number:
    square_value = False
    print('Diagonal 2 does not work! ')
    print('These are the values in diagonal 2: ', end = '')
    for i in range(size):
        print(f'{diag2[i]} ', end = '')
    print()

if square_value:
    print('This is a magic square!')
else:
    print('This is not a magic square!')
