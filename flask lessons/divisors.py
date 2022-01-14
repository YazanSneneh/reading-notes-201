# Create a program that asks the user for a number 
# then prints out a list of all the divisors of that number. 
# (divisor, a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
user_number = int(input('Enter a number to find it\'s divisors: '))
divisors = []
for i in range(2, user_number):
    if user_number%i ==0:
        divisors.append(i)

print(divisors)