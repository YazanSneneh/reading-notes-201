from typing import List

def add(*num) ->int:
    return  sum(num[0])

def sub(*num: int) ->int:
    total = 0
    for n in num[0]:
        return num

def mult(*num: List[int]) ->int:
    total = 1
    for n in num[0]:
        total = total * n
    return total

def divide(num: int, num2: int) ->int:
    return num /num2

def calc( *num, operator):
        return operator(num)

result = calc(5, 4, 8, 1, operator = mult)
print(result)