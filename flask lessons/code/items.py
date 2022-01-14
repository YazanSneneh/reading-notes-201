
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
# ----------------------------------------------------- Items Resource --------------------------------------------------
class Items(Resource):
    def get(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        update_item_query = "select * from items"
        result = cursor.execute(update_item_query)
        if result:
            items = []
            for item in result:
                items.append(item)
            connection.commit()
            connection.close()
            return {"items": items}

# --------------------------------------------------- Item Resource -----------------------------------------------------
class Item(Resource):
# ----------------------------------------------------- Get method ------------------------------------------------------
    @jwt_required()
    def get(self,name):
        item = self.find_by_name(name)
        if item:
            return item
        return {name: "item not found"}

# ----------------------------------------------------- Post Method -------------------------------------------------------

    def post(self,name):
        
        item = self.find_by_name(name)
        if item:
            return {"item": "item already exists in store"}, 400 # something wrong with request.

        parse = reqparse.RequestParser()
        parse.add_argument("name", type=str, help="Please insert a cool name here", )
        parse.add_argument("price", type=float, help="add a reasonable price please", )
        item = parse.parse_args()

        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()

            insert_query = "insert into items values(null,?,?)"
            cursor.execute(insert_query, (item['name'], item['price']))

            connection.commit()
            connection.close()
            return item, 201
        except:
            return {"message": "internal server error"}, 500 

# ----------------------------------------------------- Delete Method ------------------------------------------------------
    def delete(self,name):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        delete_item_query = "delete from items where name=?"
        cursor.execute(delete_item_query, (name,))

        connection.commit()
        connection.close()
        return {"item":"item has been removed"}

# ------------------------------------------------------- Put Method ----------------------------------------------------------
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price', 
            type=float,
            required= True,
            help= "argument cannot be blank !",
        )

        parser.add_argument('name',
            type=str,
            required = False,
            help="Please add name attribute"
        )

        data = parser.parse_args()

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        update_item_query = "update items set name=? , price=?"
        cursor.execute(update_item_query,(data['name'], data['price']) )
        connection.commit()
        connection.close()

        return {name: "item has been updated "}
        # for i in items:
        #     if i['name'] == name:
        #         i.update(data)
        #         return i
        # return {name: "Item does not exist"}

# -------------------------------------------- select item by name query --------------------------------------------------
    @classmethod
    def find_by_name(self, name):
        connection = sqlite3.connect('database.db')
        cursor=connection.cursor()

        select = 'select * from items where name=?'
        result = cursor.execute(select, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {"item": {"name": row[1], "price": row[2]}}