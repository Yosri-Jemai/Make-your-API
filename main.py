from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/id=<user_id>")
def get_user(user_id):
    #static data
    user_data = {
        "user_id": user_id,
        "name" : "Yosri Jemai",
        "email" : "yosrii.jemaiii@gmail.com"
    }

    # returning dictionary in json format
    return jsonify(user_data), 200


if __name__ == '__main__':
    app.run(debug=True)