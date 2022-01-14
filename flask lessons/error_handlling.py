try:
    user = input('Enter a number')
    print (user + 5)
except BaseException as e:
    print('type error')
    print( e)
