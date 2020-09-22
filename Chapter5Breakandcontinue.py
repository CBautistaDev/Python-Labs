'''A break statement in a loop causes the loop to exit immediately. A break statement can sometimes yield a loop that is easier to understand.'''

# empanada_cost = 3
# taco_cost = 4

# user_money = int(input('Enter money for meal: '))

# max_empanadas = user_money // empanada_cost
# max_tacos = user_money // taco_cost

# meal_cost = 0
# for num_tacos in range(max_tacos + 1):
#     for num_empanadas in range(max_empanadas + 1):
#         meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

#         # Find first meal option that exactly matches user money
#         if meal_cost == user_money:
#             break

#     # Find first meal option that exactly matches user money
#     if meal_cost == user_money:
#         break

# if meal_cost == user_money:
#     print('${} buys {} empanadas and {} tacos without change.'
#           .format(meal_cost, num_empanadas, num_tacos))
# else:
#     print('You cannot buy a meal without having change left over.')



''''Practice assisgnemnt'''

# stop = int(input())
# result = 0
# for a in range(4):
#     print(a, end=': ')
#     for b in range(3):
#         result += a + b
#         if result > stop:
#             print('-', end=' ')
#             continue
#         print(result, end=' ')
#     print()

'''"Simon Says" is a memory game where "Simon" outputs a sequence of 10 characters (R, G, B, Y) and the user must repeat the sequence. Create a for loop that compares the two strings. For each match, add one point to user_score. Upon a mismatch, end the game.

Sample output with inputs: 'RRGBRYYBGY' 'RRGBBRYBGY'
'''

user_score = 0
simon_pattern = input()
user_pattern = input()

for i in range(len(simon_pattern)):
    if user_pattern[i] == simon_pattern[i]:
        user_score += 1
    else:
        break


print('User score:', user_score)

