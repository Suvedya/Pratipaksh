# main.py

from flask import Flask
from routes.citation_routes import citation_routes

app = Flask(__name__)
app.register_blueprint(citation_routes)

if __name__ == "__main__":
    app.run(debug=True)
