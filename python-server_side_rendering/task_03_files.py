from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
        items = data.get("items")
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    # Get query arguments from url
    source_query = request.args.get('source') 
    id_query = request.args.get('id') 

    if source_query == 'json':
        # Parse json data
        with open('products.json', 'r') as f:
            data = json.load(f)
        print(f"data in json is {data}")
    elif source_query == 'csv':  
        # Parse csv data
        with open('products.csv', 'r') as f:
            data = list(csv.DictReader(f))
        print(f"data in csv is {data}")
    else:
        # Invalid source
        return render_template('product_display.html', products='Wrong source')


    if id is not None:
        for product in data:
            if product['id'] == id_query:
                return render_template('product_display.html', products=[product])
        # Id provided but not found
        return render_template('product_display.html', products='Product not found')

    return render_template('product_display.html', products=data)

        
if __name__ == '__main__':
    app.run(debug=True, port=5000)