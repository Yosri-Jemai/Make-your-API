from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/id=<user_id>")
def get_user(user_id):
    try:
        user_id = int(user_id)  # Convert to integer
    except ValueError:
        return jsonify({"error": "Invalid user_id"}), 400  # Handle non-numeric IDs

    user_data = {
        "user_id": 10,
        "name" : "Yosri Jemai",
        "email" : "yosrii.jemaiii@gmail.com"
    }

    if user_id == user_data["user_id"]:
        return jsonify(user_data), 200
    else:
        return jsonify({"error": "Unauthorized"}), 401

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)