from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  # Load the secret key from environment variable
jwt = JWTManager(app)

# Configure CORS to allow requests from multiple origins
CORS(app, resources={r"/api/*": {"origins": ["https://fitness-guru-theta.vercel.app", "http://localhost:3000"]}})

# Define the blueprint without the URL prefix
auth_bp = Blueprint('auth', __name__, url_prefix='/api')

# Mock user data (Replace with database in real projects)
users = {'user@example.com': 'password123',
         'sabarish@mail.com': '1234'}

@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if email not in users or users[email] != password:
        return jsonify({"msg": "Invalid credentials"}), 401

    access_token = create_access_token(identity=email)
    return jsonify({"token": access_token}), 200

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"msg": "Welcome! You have access to this protected route"}), 200

# Register the blueprint with the app
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)