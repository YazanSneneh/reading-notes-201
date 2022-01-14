# Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?
user_number = int(input('Enter a number to check if it\'s even or odd: '))

if user_number%4==0:
    print('number is even and multiple of 4 as well')
elif user_number%2==0:
    print('Your Number is even')
else:
    print('Number is odd')