from  flask import Flask, jsonify, request
from  flask import render_template

app = Flask(__name__)

from products import products 
# Con esto estoy importando el archivo products.py

@app.route('/')
def ping():
    # return jsonify({"message": "PONG"})
    return render_template('index.html')


@app.route('/products')
def getProducts():
        return jsonify({"products": products}) #Esto nos va permitir traer los productos
    

@app.route('/products/<string:product_name>') 
#Esto es un parametro <string:product_name>
def getProduct(product_name):
    # print (product_name)
    productsFound = [product for  product in products if product['name'] == product_name]
    # return 'Recibido'
    # Este siguiente codigo nos va permitir hacer si se encuentra 
    # Un producto
    if(len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "Product not Found"})

    # return jsonify({'product': productsFound[0]})

# Esta ruta nos va permitir crear  dato
@app.route('/products', methods=['POST'])
def addProduct():
    print(request.json)

#De esta forma creamos un producto  
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }

# De esta forma estamos añadiendo un nuevo producto 
# A mi otro archivo
    products.append(new_product)
    return jsonify({"message": "Product added succefully", "products": products})


#como podemos actualizar un datos 
#Se debe crear otra ruta. Ejemplo 
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [ product for product in products if product['name'] == product_name ]
    productFound[0]['name']     = request.json['name']
    productFound[0]['price']    = request.json['price']
    productFound[0]['quantity'] = request.json['quantity']

    return jsonify({
         "message": "Product Updated",
         "product": productFound[0]
    })

    return jsonify({"message": "Product not Found!! "})


#Para eliminar tambien podemos crear otra ruta 
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            'message': 'Product Deleted',
            'products': products
        })



        # return 'Datos recibidos'
    




if __name__ == "__main__":
    app.run(debug = True, port= 5000)