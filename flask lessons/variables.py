a = 'hello'
print(a *5) # print hello 5 times
# .......................................................................................................
# create a program calculate the age user input in months days and seconds
user_age = int(input('Enter your age in years: '))
months= user_age* 12
days = months * 30
hours = days * 24
minutes = hours * 60
seconds = minutes * 60 
print(f'Your age in months: {months}')
print(f"your age in days is {days}")
print(f"your age in hours is {hours}")
print(f"your age in minutes is {minutes}")
print(f"your age in seconds is {seconds}")
# ..........................................................................................................
my_tupe= 3,
type(my_tupe)
# ..........................................................................................................
friends = ['one','two','three']
friends_new = [friend*2  for friend in friends ]
number = 10
user_input = input('Press Y or y if you want to play: ')
if user_input in {'Y','y'}:
    user_number = int(input('Enter A number: '))
    if user_number == number:
        print(f'{user_number:,%} is the correct answer!')
    else:
        print(f'your answer is{user_number: %}You got it wrong bud!')
print(friends_new)
# ..........................................................................................................
friends_list = [
    { 'name': 'Anna', 'age': 19, 'attendence': True},
    { 'name': 'Abdo', 'age': 29, 'attendence': False},
    { 'name': 'Fook', 'age': 16, 'attendence': False}
]

# print(friends_list[0].values())
for key, val in friends_list[1].items():
    print(f" key ==> {key} : val ==>{val}")
print('---------------------------------------------')
for key in friends_list[0]:
    print(f" key ==> {key} : val ==>{friends_list[0][key]}")
# ..........................................................................................................
friends = ['one','two','three']

one, _, three = friends

*h, t = friends

print(t)
# ..........................................................................................................
number = 10

for number in range(number):
    if number%5 ==0 and number%3==0:
        print('Fizzbuzz')
    elif number%5==0:
        print('fizz')
    elif number%3==0:
        print('buzz')
    else:
        print(number)