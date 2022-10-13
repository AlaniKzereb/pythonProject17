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

db.create_all()

user_john = User(id=1, name="John", age=30)
user_alice = User(id=2, name="Alice", age=18)

print(user_john, user_alice)

users = [user_john, user_alice]
db.session.add_all(users)

print(db.session.new)

db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
