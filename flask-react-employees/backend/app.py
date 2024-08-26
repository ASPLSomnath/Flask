from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employees.db"
app.config["SQLALCHEMY_TRACH_MODIFICATIONS"] = False

db = SQLAlchemy(app)

import routes

if __name__ == "__main__" :
    app.run(debug=True)