import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, Integer, String

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)


db.drop_all()
db.create_all()

user_john = User(id=1, name="John", age=30)
user_alice = User(id=2, name="Alice", age=18)

print(user_john, user_alice)

users = [user_john, user_alice]
db.session.add_all(users)

print(db.session.new)

db.session.commit()

@app.route("/users/first")
def get_user_first():
    user = User.query.first()

    return json.dumps({
        "id": user.id,
        "name": user.name,
        "age": user.age
        })

@app.route("/users/count")
def get_user_count():
    user_count = User.query.count()

    return json.dumps(user_count)

@app.route("/users")
def get_users():
    user_list = User.query.all()
    user_response = []

    for user in user_list:
        user_response.append(
            {"id": user.id,
             "name": user.name,
             "age": user.age

            }
        )

    return json.dumps(user_response)


@app.route("/users/<int:sid>")
def get_user(sid: int):
    user = User.query.get(sid)

    if user is None:
        return "user not found"

    return json.dumps({
        "id": user.id,
        "name": user.name,
        "age": user.age
        })



if __name__ == '__main__':
    app.run(debug=True)
