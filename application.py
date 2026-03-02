from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///e-commerce.db"

db = SQLAlchemy(application)

class Product (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    price = db.Column(db.Float, nullable = False)
    description = db.Column(db.Text, nullable = True)

@application.route("/") 
def initial():
    return "API UP"

@application.route("/api/products/add", methods = ["POST"])
def add_product():
    data = request.json
    if "name" in data and "price" in data:
        product = Product(name = data["name"], price = data["price"], description = data.get("description", ""))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message" : "Product registered successfully."})
    return jsonify({"message" : "Invalid product data."}), 400

@application.route("/api/products", methods = ["GET"])
def get_products():
    products = Product.query.all()
    products_list = []
    for product in products:
        product_data = {
            "id" : product.id,
            "name" : product.name,
            "price" : product.price,
        }
        products_list.append(product_data)
    return jsonify(products_list)

if __name__ == "__main__":
    application.run(debug = True)
