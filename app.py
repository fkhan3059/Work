from flask import Flask

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


#post /store data: {name:}
@app.route('/store', methods= ['POST'])
def create_store():
    pass
#get /store/<string: name>
@app.route('/store/<string: name>')
def get_store(name):
    pass

#get /store
@app.route('/store')
def get_stores():
    pass

#post /store/<string: name>/item {name:, price:}
@app.route('/store/<string: name>/item', methods= ['POST'])
def create_item_in_store(name):
    pass

#get /store/<string: name>/item
@app.route('/store/<string: name>/item')
def get_item_in_store(name):
    pass

app.run(port=5000)
