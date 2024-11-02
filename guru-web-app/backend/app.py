from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from auth import auth_bp  # Import the blueprint
import os

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  # Change this to a strong secret key
jwt = JWTManager(app)
CORS(app)

# Register the blueprint with the app
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)