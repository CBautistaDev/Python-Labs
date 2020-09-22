# numbers = [8, 6, 5]
# for number in reversed(numbers):
#     print(number)


'''Gets the greates city distance and assisnged to variable to print. 
If another one is greater it will replace the current distance/best variables.'''

# cities = {
#     'Toronto': 982,
#     'Austin': 5259,
#     'Montreal': 3435,
#     'Chicago': 958,
#     'Paris': 584,
# }

# best = ''
# distance = 0
# for city in cities:
#     if cities[city] > distance:
#         best = city
#         distance = cities[city]
# print(best, distance)


channels = {
    'MTV': 35,
    'CNN': 28,
    'FOX': 11,
    'NBC': 4,
    'CBS': 12
}

''': A for loop assigns the loop variable with a dictionary's keys.'''

for c in channels:
    print('{} is on channel {}'.format(c, channels[c]))

    contact_emails = {
        'Sue Reyn': 's.reyn@email.com',
        'Mike Filt': 'mike.filt@bmail.com',
        'Nate Arty': 'narty042@nmail.com'
    }


'''Adding new contact to dictionary using input'''
new_contact = input()
new_email = input()
contact_emails[new_contact] = new_email

''' Your solution goes here '''
for contact in contact_emails:
    print('{} is {}'.format(contact_emails[contact], contact))


