'''
5.14 LAB: Convert to binary
Write a program that takes in a positive integer as input, and 
outputs a string of 1's and 0's representing 
the integer in binary. For an integer x, the algorithm is:
'''
x = int(input())

while x > 0:
    print(x % 2, end='')
    x = x//2
print()

'''
5.15 LAB: Count input length without spaces, periods, or commas
Given a line of text as input, output the number of characters excluding spaces, periods, or commas.
''' 

user_text = input()
user_text = user_text.replace(',','')
user_text = user_text.replace('.', '')

user_text = user_text.split(' ')

print(sum(len(i) for i in user_text))


'''Another simpler way '''
user_text = input()
count = 0
for x in user_text:
    if not(x in " .,"):
        count += 1
print(count)


'''
5.16 LAB: Password modifier
Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it 
stronger by replacing characters using the key below, and by appending "q*s" to the end of the input string.

i becomes !
a becomes @
m becomes M
B becomes 8
o becomes 
'''
word = input()
password = ''

for x in word:
    if(x == 'i'):
        password += "!"
    elif(x == 'a'):
        password += "@"
    elif (x == 'm'):
        password += "M"
    elif (x == 'B'):
        password += "8"
    elif (x == 'o'):
        password += "."
    else:
        password += x
password += "q*s"
print(password)
'''
5.17 LAB: Output range with increment of 10

Write a program whose input is two integers. Output the first integer and 
subsequent increments of 10 as long as the value is less than or equal to the second integer.
'''
userinputone = int(input())
userinputtwo = int(input())

error = False

if userinputtwo < userinputone:
    print('Second integer can\'t be less than the first.')
    error = True

if error == False:
    while userinputone <= userinputtwo:
       print(userinputone, '', end='')
       userinputone = userinputone + 10
    print()

'''
5.18 LAB: Print string in reverse
Write a program that takes in a line of text as input, and outputs that line of text in reverse. The program repeats, ending when the user enters "Quit", "quit", or "q" for the line of text.

'''
word = input()

while word not in ('Quit', 'quit', 'q'):
  print(word[::-1])
  
word = input()

'''5.19 LAB: Countdown until matching digits
'''
num = int(input())
if(num >= 20 and num <= 98):
   firstDigit = num // 10
   secondDigit = num % 10
   while(firstDigit != secondDigit):
       print(num)
       num = num - 1
       firstDigit = num // 10
       secondDigit = num % 10
   print(num)
else:
    print('Input must be 20-98')

'''
5.21 LAB: Smallest and largest numbers in a list
Write a program that reads a list of integers into a list
 as long as the integers are greater than zero, then 
outputs the smallest and largest integers in the list.
'''
user_input = int(input())
list = []

while user_input > 0:
   list.append(user_input)
   user_input = int(input())

print(min(list), max(list))

'''
5.22 LAB: Output values in a list below a user defined amount
Write a program that first gets a list of integers from input
. The input begins with an integer indicating the number of integers 
that follow. Then, get the last value from the input, which indicates a
 threshold. Output all integers less than or equal to that last threshold 
 value.'''
number_inlist = int(input())

list = []
max_numbers = 5
while number_inlist > 0:
    input_numbers = int(input())
    list.append(input_numbers)
    number_inlist -= 1

list.sort()
max_number = int(input())

for i in list:
    if i < max_number:
        print(i)
