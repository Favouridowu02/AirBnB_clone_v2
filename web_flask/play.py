from flask import Flask
from flask_cors import CORS # type: ignore

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def helloWorld():
    return "Hello, cross-origin-world!"