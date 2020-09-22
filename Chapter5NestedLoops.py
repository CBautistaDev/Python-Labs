'''A nested loop is a loop that appears as part of the body of another loop. 
The nested loops are commonly referred to as the outer loop and inner loop.'''

"""
Program to print all 2-letter domain names.

Note that ord() and chr() convert between text and the ASCII or Unicode encoding:
-  ord('a') yields the encoded value of 'a', the number 97.
-  ord('a')+1 adds 1 to the encoded value of 'a', giving 98.
-  chr(ord('a')+1) converts 98 back into a letter, producing 'b'
"""
# print('Two-letter domain names:')

# letter1 = 'a'
# letter2 = '?'
# while letter1 <= 'z':  # Outer loop
#     letter2 = 'a'
#     while letter2 <= 'z':  # Inner loop
#         print('{}{}.com'.format(letter1, letter2))
#         letter2 = chr(ord(letter2) + 1)
#     letter1 = chr(ord(letter1) + 1)

'''Here is a nested loop example that graphically depicts an integer's magnitude by using asterisks, creating what is commonly called a histogram:

Run the program below and observe the output. Modify the program to print one asterisk per 5 units. So if the user enters 40, print 8 asterisks
'''
# num = 0
# while num >= 0:
#     num = int(input('Enter an integer (negative to quit):\n'))

#     if num >= 0:
#         print('Depicted graphically:')
#         for i in range(num):
#             print('*', end=' ')
#         print('\n')

# print('Goodbye.')
# 2
# i1 = 1
# while i1 < 19:
#     i2 = 3
#     while i2 <= 9:
#         print('{}{}'.format(i1, i2), end=' ')
#         i2 = i2 + 3
#     i1 = i1 + 10


'''Given the number of rows and the number of columns, write nested loops to print a rectangle.

Sample output with inputs: 2 3
* * * 
* * *
'''

# num_rows = int(input())
# num_cols = int(input())

# for i in range(num_rows):
#     print('*', end=' ')
#     for j in range(num_cols):
#         print('*', end=' ')
#     print()

'''
Given num_rows and num_cols, print a list of all seats in a theater. Rows are numbered, columns lettered, as in 1A or 3E. Print a space after each seat.

Sample output with inputs: 2 3
1A 1B 1C 2A 2B 2C
'''

'''found in stackoverflow'''
# num_rows = 2
# num_cols = 3

# rows = 1  # create a number to start counting from for rows
# while rows <= num_rows:  # start iterating through number of rows
#     cols = 1  # create a number to start counting from for columns
#     alpha = 'A'  # starting point for alphabet
#     while cols <= num_cols:  # iterates through number of columns
#         print('%s%s' % (rows, alpha), end=' ')
#         cols += 1  # number of columns needs to increase
#         alpha = chr(ord(alpha) + 1)  # alphabet needs to increase
#     rows += 1  # number of rows needs to increase
# print()
'''mysample'''
# num_rows = int(input())
# num_cols = int(input())

# # Note 1: You will need to declare more variables
# # Note 2: Place end=' ' at the end of your print statement to separate seats by spaces
# rows = 1
# while rows <= num_rows:
#     cols =1 
#     letter = 'A'
#     while cols <= num_cols:
#         print('{}{} '.format(rows,letter), end='')
#         cols += 1
#         letter = chr(ord(letter)+1)
#     rows += 1

# print()
