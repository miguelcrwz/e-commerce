from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

application = Flask(__name__)
application.config["SECRET_KEY"] = "miguelcrwz"
application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///e-commerce.db"

login_manager = LoginManager()
db = SQLAlchemy(application)
login_manager.init_application(application)
login_manager.login_view = "login"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), nullable = False, unique = True)
    password = db.Column(db.String(80), nullable = True)

class Product (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    price = db.Column(db.Float, nullable = False)
    description = db.Column(db.Text, nullable = True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@application.route("/") 
def initial():
    return "API UP"

@application.route("/login", methods = ["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username = data.get("username")).first()
    if user and data.get("password") == user.password:
        login_user(user)
        return jsonify({"message" : "Logged in successfully."})
    return jsonify({"message" : "Unauthorized. Invalid credentials."}), 401

@application.route("/logout", methods = ["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message" : "Logout successfully."})

@application.route("/api/products/add", methods = ["POST"])
def add_product():
    data = request.json
    if "name" in data and "price" in data:
        product = Product(name = data["name"], price = data["price"], description = data.get("description", ""))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message" : "Product registered successfully."})
    return jsonify({"message" : "Invalid product data."}), 400

@application.route("/api/products/delete/<int:product_id>", methods = ["DELETE"])
def delete_products(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message" : "Product deleted successfully."})
    return jsonify({"message" : "Product not found."}), 404

@application.route("/api/products/<int:product_id>", methods = ["GET"])
def get_products_details(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            "id" : product.id,
            "name" : product.name,
            "price" : product.price,
            "description" : product.description
        })
    return jsonify({"message" : "Product not found."}), 404

@application.route("/api/products/update/<int:product_id>", methods = ["PUT"])
def update_products(product_id):
    product = Product.query.get(product_id)
    if not product: 
        return jsonify({"message" : "Product not found."}), 404
    data = request.json
    if "name" in data:
        product.name = data["name"]
    if "price" in data: 
        product.price = data["price"]
    if "description" in data:
        product.description = data["description"]
    db.session.commit()
    return jsonify({"message" : "Product updated successfully."})

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
