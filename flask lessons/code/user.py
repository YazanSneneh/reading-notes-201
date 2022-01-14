import sqlite3
from flask_restful import Resource, reqparse
class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password


    @classmethod
    def get_user_by_username(cls,username):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        
        select = 'select * from users where username=?'
        result = cursor.execute(select, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None


        connection.commit()
        connection.close()
        return user

    @classmethod
    def get_user_by_id(cls,_id):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        select = "select * from users where id=?"
        result = cursor.execute(select,(_id,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None
        
        connection.close()
        return user


class UserRegister(Resource):
    # get user input from /regester url
    parse = reqparse.RequestParser()
    parse.add_argument(
        'username',
        type=str,
        required=True,
        help="This feild should not be empty!"
    )
    parse.add_argument(
        "password",
        type= str,
        required = True,
        help="please make sure password is not empty"
    )

    def post(self):
        # check if user in database
        data = UserRegister.parse.parse_args()

        if User.get_user_by_username(data['username']):
            return {"Message": "username already in use"}

        # insert user into database
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        insert_user = "insert into users values(null,?, ?)"
        cursor.execute(insert_user,(data['username'], data['password']))
        connection.commit()
        connection.close()

        return {"message": "User created succefully"}