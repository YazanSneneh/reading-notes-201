
from user import User

def authinticate(username, password):
    current_user = User.get_user_by_username(username)
    if current_user and  current_user.password  == password:
        return current_user


def indentify(payload):
    user_id = payload['identity']
    return User.get_user_by_id(user_id)