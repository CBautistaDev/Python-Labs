'''The range() function allows counting in for loops as well. 
range() generates a sequence of integers between a starting integer that is 
included in the range, an ending integer that is not included in the range, and an integer step value. 
'''

'''For loop example: Calculating yearly savings.'''
'''Program that calculates savings and interest'''

# initial_savings = 10000
# interest_rate = 0.05

# years = int(input('Enter years: '))
# print()

# savings = initial_savings
# for i in range(years):
#     print(' Savings in year {}: ${:.2f}'.format(i, savings))
#     savings = savings + (savings*interest_rate)

# print('\n')


for i in range(0, -4, -1):
    print(i, end=' ')
