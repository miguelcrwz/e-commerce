from flask import Flask, request, jsonify

application = Flask(__name__)

@application.route("/") 
def initial():
    return "API UP"

if __name__ == "__main__":
    application.run(debug = True)
