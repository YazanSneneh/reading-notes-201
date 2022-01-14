# Ask the user for a string.
#  and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

user_string = input('Enter String to check if it\s palindrom or not: ')
palind_list = ''

for i in range(len(user_string)-1,-1,-1):
    palind_list += user_string[i]


if palind_list == user_string:
    print(f'user input is palindrome')
else:
    print('not palindrome')