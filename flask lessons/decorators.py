import functools

user = {'name': "Hana'a", 'role': 'admin', 'is_egestered': True}

user2 = {'name': "Yaz", 'role': 'guest', 'is_egestered': False}


def user_checker(access_level):
    def check_user(fun):
        @functools.wraps(fun)
        def nested(*arg):
            if user['role'] == access_level:
                return fun(*arg)
            else:
                return "User is not regestered"
        return nested
    return check_user

@user_checker('admin')
def get_password(arg):
        return "234"


print(get_password('s'))