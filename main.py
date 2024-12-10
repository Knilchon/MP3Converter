from flask import Flask
from converter import install

# Create a Flask app instance
app = Flask(__name__)

# Define a simple route
@app.route("/<id>")
def home(id):
    return install(id)

if __name__ == "__main__":
    app.run(debug=True)
