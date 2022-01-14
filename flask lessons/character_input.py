# Create a program that asks the user to enter their name and their age.
# Print out a message:
#     addressed to them that tells them the year that they will turn 100 years old.
name = input('Enter your name: ')
age = int(input('Enter your age: '))
years_remaining = 100 - age
year_age_is_hundred = 2021 + years_remaining
print(f'You will become 100 years old in {year_age_is_hundred}')