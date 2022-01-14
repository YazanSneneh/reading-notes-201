# write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_than_five = [i for i in a if i<5]

# for i in a:
#     if i<5:
#         less_than_five.append(i)


print(less_than_five)