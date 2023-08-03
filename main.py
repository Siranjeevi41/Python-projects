from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Change the database URI as needed
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(200))
    updated_date = db.Column(db.DateTime)
    created_date = db.Column(db.DateTime)
    profile_image = db.Column(db.LargeBinary)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    address = data.get('address')

    if not (first_name and last_name and email):
        return jsonify({"message": "First name, last name, and email are required fields"}), 400

    try:
        new_user = User(first_name=first_name, last_name=last_name, email=email, address=address)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully", "user_id": new_user.id}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Email already exists"}), 409

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to create user", "error": str(e)}), 500

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    return jsonify({"user_id": user.id, "first_name": user.first_name, "last_name": user.last_name,
                    "email": user.email, "address": user.address, "updated_date": user.updated_date,
                    "created_date": user.created_date}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
