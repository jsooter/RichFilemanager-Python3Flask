import os
from flask import Flask, request, send_from_directory
from jinja2 import Markup, PackageLoader, Environment, FileSystemLoader, ChoiceLoader
dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'static')
app = Flask(__name__)

from .File import bluePrint as fileBluePrint
app.register_blueprint(fileBluePrint)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
