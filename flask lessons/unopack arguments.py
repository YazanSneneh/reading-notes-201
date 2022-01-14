def args_unpack(*args):
    for num in args:
        print(num)

args_unpack(1,2,3,4)
# ............................................................
def list_unpack(one, two, three):
    print(one)
    print(two)
    print(three)

nums = [1,2,3]
list_unpack(*nums)
# ............................................................
def dict_unpack(x,y):
    print(x + y)

my_dict = {'x':5, 'y':10, 'x':55}
dict_unpack(**my_dict)
# ............................................................
# k arguments
def k_arguemnts(**kargs):
    for key, val in kargs:
        print(f'{key} : {val}')

dict_m={'name':'Yazan','age':30}
k_arguemnts(name = dict_m['name'], age = dict_m['age'])
k_arguemnts(**dict_m)
# ............................................................
def args_kargs(*args, **kargs):
    for arg in args:
        print(arg)
    print(kargs)


args_kargs(1,2,3,4, name ='yazan',age=30)