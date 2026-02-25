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

if __name__ == "__main__":
    application.run(debug = True)
