from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'My beautiful store',
        'items': [
            {
                'name': 'My item',
                'price': 15
            }
        ]
    }



]

#post: we receive data
#get: we send back data

@app.route('/')
def home():
    return render_template('index.html')

#post /store data: {name:}
@app.route('/store', methods= ['POST'])
def create_store():
    request_data = request.get_json() #the user in the browser gives us some data i.e. a store name to create a new store
    new_store = {'name': request_data['name'], 'items': []} #we are retrieving the store name data that user input in the previous step
    stores.append(new_store)
    return jsonify(new_store)

#get /store/<string: name>
@app.route('/store/<string:name>')
def get_store(name):
    #iterate over stores, if the store matches, return it, if dont match, return error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store is not found'})

#comment 1

#get /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores}) 

#post /store/<string: name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods= ['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {'name': request_data['name'], 'price': request_data['price']}
            store['items'].append(new_item)
            return jsonify(store)
    return jsonify({'message': 'store not found'})

#get /store/<string: name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})



app.run(port=5000)
