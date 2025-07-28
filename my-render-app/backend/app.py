
from flask import Flask, jsonify
from flask_migrate import Migrate
from database.db import db
from models.User import User
from models.Rol import Rol
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///database/app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa la base de datos y migraciones
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/api', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the API!"})

if __name__ == '__main__':
    app.run(debug=True)