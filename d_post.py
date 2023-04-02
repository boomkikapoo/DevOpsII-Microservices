from flask import Flask, request, jsonify
import datetime

import item_data as us

app = Flask(__name__)

@app.route('/item_post', methods=['POST'])
def register():
    
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    _user = us.item_name()
    data = [x for x in _user if x["name"]==name]
    
    if (data):
        return jsonify({'message': 'Cannot create user.'}), 401
    else:
        us.item_name_add(name,category,price,instock)
        return jsonify({'message': 'Created successfully.'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True) 