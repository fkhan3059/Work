from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name']== name, items), None) #adding next means the function goes through one item, returns it and goes to the next one
        #adding none means, when the iteration ends, and there is no other items left to iterate, the code returns none
        return {'item': None}, 200 if item else 404 #HTTP error msg
    
    def post(self, name):
        if next(filter(lambda x: x['name']== name, items), None): #this means if the item exists when a user inputs it
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 #201 represent http status code that an item is created

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
app.run(port=5000, debug=True)
